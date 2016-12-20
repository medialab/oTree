$(function (window, undefined) {
  /**
   * Timer for measuring user input speed.
   */
  var Timer = (function () {
    var startTime = new Date().getTime();
    var elapsed = 0;

    // Starts the timer.
    function start() {
      startTime = new Date().getTime();
    };

    // Stops the timer.
    function stop() {
      elapsed = new Date().getTime() - startTime;
    }

    // Return elapsed time.
    function getElapsed() {
      return elapsed;
    }

    // Public API.
    return {
      start: start,
      stop: stop,
      getElapsed: getElapsed,
    };
  })();

  window.IAT = (function (window, undefined) {
    /**
     * Reference to UI pieces manipulated via jQuery.
     */
    var $uiCategoryLeft = $('.left'),
        $uiCategoryRight = $('.right'),
        $uiStimuli = $('.stimuli'),
        $uiWrongAnswerCross = $('.wrong-answer'),
        $window = $(window),
        $pauseMessage = $('.pause-message'),
        mightBeUsingTablet = false,
        PAUSE_SCREEN_DELAY = 5000;

    var answerStore = {
      successes: [],
      failures: [],
    };

    var toCSV = {
      successes: [
        'Trial ID,Player ID in group,Code,Label,Time started' +
        'Left category,Right category,Stimuli word' +
        'Correct position,Correct category,Time taken'
      ],
      failures: [
        'Trial ID,Player ID in group,Code,Label,Time started,Left category' +
        'Right category,Stimuli word,Correct position' +
        'Correct category,Failed by time out,Time taken'
      ],
      meta: [
        'Player ID in group,Code,Label,Time started,Trials order,Error Percentage,Platform'
      ]
    };

    /**
     * Informations to be taken from config.
     */
    var keyCodeLeft = null,
        keyCodeRight = null,
        answerTimeLimit = null,
        leftAndRightKeys = {},
        participant = {},
        pauseScreens = [];

    /**
     * Update text on UI - left and right category, stimuli word.
     * Deal differenly if the data set is a pause message: display message
     * and framing words grabbed for the *next* incoming trial.
     *
     * @param  {Object} trial         Trial data.
     * @param  {Object} queue        The entire payload of trials.
     * @param  {int}    trialIndex   Index of currently shown trial/screen.
     * @return {void}
     */
    function updateUIText(trial, queue, trialIndex) {
      if (!isPauseScreen(trial)) {
        hidePauseMessage();
        $uiCategoryLeft.html(trial._left);
        $uiCategoryRight.html(trial._right);
        $uiStimuli.html(trial._stimuli);
      } else {
        showPauseMessage(
          trial.message[lang],
          trial.cta,
          {
            'left': queue[trialIndex+1]._left,
            'right': queue[trialIndex+1]._right
          }
        );
      }
    }

    /**
     * Show pause message screen.
     *
     * @param  {string} msg   Message to display.
     * @param  {string} cta   CTA to display after reading time out.
     * @param  {Object} words The left/right words to display.
     * @return {void}
     */
    function showPauseMessage(msg, cta, words) {
      $uiCategoryLeft.html(words.left);
      $uiCategoryRight.html(words.right);
      $uiStimuli.html('');
      $pauseMessage.html(msg);
      $pauseMessage.show();

      setTimeout(function () {
        $pauseMessage.html($pauseMessage.html() + cta)
      }, PAUSE_SCREEN_DELAY)
    }

    /**
     * Hide pause message screen.
     *
     * @return {void}
     */
    function hidePauseMessage() {
      $pauseMessage.hide(0, function () {
        $pauseMessage.html('');
      });
    }

    /**
     * Display big red cross for wrong answer.
     *
     * @param  {boolean} shouldDisplay
     * @return {void}
     */
    function displayWrongAnswerFeedback(shouldDisplay) {
      if (shouldDisplay) {
        $uiWrongAnswerCross
          .css('display', 'block')
          .stop()
          .animate({opacity: 1}, 100);
      } else {
        $uiWrongAnswerCross
          .animate({opacity: 0}, 100, function () {
            $uiWrongAnswerCross.css('display', 'none');
          });
      }
    }

    /**
     * Capitalize first letter.
     *
     * @param  {string} str Input string.
     * @return {string} Capitalized string.
     */
    function capitalize(str) {
      return str.length > 0 ? str[0].toUpperCase() + str.slice(1) : str;
    }

    /**
     * Shuffle an array using de-facto unbiased Fisher-Yates (aka Knuth) dedicated algorithm.
     * @see https://bost.ocks.org/mike/shuffle/
     *
     * @param  {Array} arr The array to shuffle.
     * @return {Array} A new array based on the first one, with shuffled values.
     */
    function shuffleArray(arr) {
      var currentIndex = arr.length, temporaryValue, randomIndex;

      // While there remain elements to shuffle...
      while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = arr[currentIndex];
        arr[currentIndex] = arr[randomIndex];
        arr[randomIndex] = temporaryValue;
      }

      return arr;
    }

    /**
     * Given an array of even numbers of letters (each representing a trial set),
     * shuffle and return a new array of them.
     *
     * @param  {Array} order Array of letters.
     * @return {Array} Array of shuffled letters.
     */
    function shuffleTrialPairs(order) {
      var reordered = [];

      order.map(function (letter, index, array) {
        reordered.push(shuffleArray(array.splice(0, 2)));
        if (array.length === 2) reordered.push(shuffleArray(array));
      });

      reordered = [].concat.apply([], shuffleArray(reordered));

      return reordered;
    }

    /**
     * Randomize set of trials.
     *
     * @param  {order} order String of letters where each letter is attached to a set of trials.
     * @return {Array} Array of letters, randomized from the first order.
     */
    function randomizeTrialsSets(order) {
      var reordered = [],
          order = order.split(''),
          beginTrial = null,
          midTrial = null;

      // First round is practice round. Leave it as is.
      if (order[0] === 'A') {
        beginTrial = order.shift();
      }

      if (order[order.length-1] === 'F') {
        midTrial = order.splice(order.indexOf('D'), 1)[0]
      }


      // If remaining letters form an even set, we can simply randomize each pairs.
      // If it's an odd pair, kick out the tail round, shuffle, then add it back.
      reordered = reordered.concat(shuffleTrialPairs(order));
      if (midTrial) {
        if (reordered[1] === 'B' || reordered[1] === 'C') {
          reordered.unshift(beginTrial)
          reordered.splice(3, 0, midTrial)
        } else {
          reordered.unshift(midTrial)
          reordered.splice(3, 0, beginTrial)
        }
      } else {
        reordered.unshift(beginTrial)
      }

      return reordered;
    }

    /**
     * Prepare the processed, usable trials.
     *
     * @param  {Object} data  Raw JSON data.
     * @param  {string} order The order of passage, such as "A B C D"...
     * @param  {string} lang  Language code to base sets on.
     * @return {Array}  The ready-to-use, stack of trial objects.
     */
    function prepareTrials(data, order, lang) {
      var preparedTrials = [],
          id = 0;

      // Boolean switch: starts truthy and gets toggled when we place
      // a pause screen before a new set of trials.
      // Gets toggled back to falsy when we get the inverted order.
      var toggleOrderFlag = true;

      // Push opening pause screen in.
      preparedTrials.push({
        message: pauseScreens.message[0],
        cta: pauseScreens.cta[lang]
      });

      // Randomize orders of set of trials,
      // then arrange the trials based on given order.
      randomizeTrialsSets(order).forEach(function (character, i) {
        shuffleArray(data.trials[character].displayed).forEach(function (displayed, j) {
          function getLocalizedValue(trial, field, lang) {
            if (trial[field] && trial[field][lang]) {
              return trial[field][lang];
            }
            throw new Error(
              'Cannot get localized value for trial. Make sure you are using ' +
              '2 characters formatted locale (e.g. "en", not "en-us") in your ' +
              'configuration (check value for OTREE_LANGUAGE_CODE).'
            )
          }

          // Whenever j === 0, we are at the very beginning of a new trials set.
          // --
          // Skip the first round, then on each following round,
          // place a relevant pause screen before actual trials starts.
          if (i > 0 && j === 0) {
            var k = toggleOrderFlag ? 1 : 2;
            toggleOrderFlag = !toggleOrderFlag;
            preparedTrials.push({
              message: pauseScreens.message[k],
              cta: pauseScreens.cta[lang]
            });
          }

          // Push an element in the set.
          // This is basically the bulk of our user's run,
          // containing all trials data that she will go through.
          preparedTrials.push({
            id: id,

            // Set of French data for data recovery and reconciliation purposes.
            // That way, we always receive French text to analyze IAT results,
            // no matter what languege we were testing for.
            correctCategory: capitalize(getLocalizedValue(displayed, displayed.correct, 'fr')),
            stimuli: getLocalizedValue(displayed, 'showing', 'fr'),
            left: capitalize(getLocalizedValue(displayed, 'left', 'fr')),
            right: capitalize(getLocalizedValue(displayed, 'right', 'fr')),
            correctPosition: displayed.correct,

            // Set of localized data to display to user.
            _stimuli: getLocalizedValue(displayed, 'showing', lang),
            _left: capitalize(getLocalizedValue(displayed, 'left', lang)),
            _right: capitalize(getLocalizedValue(displayed, 'right', lang))
          });

          id++;
        });
      });

      return preparedTrials;
    }

    /**
     * Apply configuration from data passed in.
     *
     * @param {Array}  dataStore
     */
    function setConfiguration(dataStore) {
      keyCodeLeft = dataStore.config.keycodes.left;
      keyCodeRight = dataStore.config.keycodes.right;
      answerTimeLimit = dataStore.config.answer_time_limit;
      pauseScreens = dataStore.pauses;
      leftAndRightKeys[keyCodeLeft] = 'left';
      leftAndRightKeys[keyCodeRight] = 'right';
      participant = dataStore.participant;
    }

    /**
     * State whether the trial is actually a pause screen.
     *
     * @param  {Object}  trial The trial object to test.
     * @return {Boolean} True if it is a pause screen.
     */
    function isPauseScreen(trial) {
      return trial.hasOwnProperty('message');
    }

    /**
     * Load up and start the queue of trials, one after the next,
     * then return the results as a promise.
     *
     * @param  {Array}  dataStore
     * @param  {string} order        The order of passage, such as "A B C D"...
     * @param  {string} lang         Language code to base sets on.
     * @param  {string} timeStarted  A UTC date string informing when the test was started.
     * @return {Object} A promise resolving with the results payload.
     */
    function loadBlocks(dataStore, order, lang, timeStarted, toCSV) {
      setConfiguration(dataStore);

      var deferred = $.Deferred();

      startBlocks(prepareTrials(dataStore, order, lang), toCSV)
        .then(function (results) {
          var errorPercentage = (results.failures.length / results.successes.length) * 100;
          var platform = mightBeUsingTablet ? 'tablet' : 'desktop';

          // Player ID in group, Code, Label, Time started, Trials order, Error Percentage, Platform'
          var meta = results.meta.slice(0).split();
          meta.push(
            dataStore.participant.id + "," + dataStore.participant.code + "," + dataStore.participant.label + "," +
            timeStarted + "," + order + "," +  errorPercentage + "," + platform + '\n'
          )

          results.meta = meta.join('\\n');

          return deferred.resolve(results);
        });

      return deferred.promise();
    }

    /**
     * Save the correct or wrong input from user, with timing for each round.
     *
     * @param  {String} type   'successes' or 'failures', according to the keys in `answerStore`.
     * @param  {Object} trial  The current trial object.
     * @param  {String} timing The elapsed time for this answer, as taken by the Timer instance.
     * @return {void}
     */
    function save(type, trial, timing, timedOut) {
      answerStore[type].push(
        Object.assign(
          {},
          {
            id: trial.id,
            left: trial.left,
            right: trial.right,
            correctCategory: trial.correctCategory,
            correctPosition: trial.correctPosition,
            stimuli: trial.stimuli
          },
          {timing: timing, timedOut: timedOut ? true : false}
        )
      );
    }

    /**
     * Promise encapsulating all the process of waiting for the user's answer.
     * When it does resolve, it means the current trial is finished,
     * and we have saved successes (and optional failures).
     *
     * @param  {Object} trial The current trial.
     * @return {Object} Promise, resolved when trial is done.
     */
    function waitForAnswer(trial) {
      // console.log('Trial --- ' trial);
      var deferred = $.Deferred();
      var timer = Timer;
      var keyPressed = null;
      var timeLimitForAnswer = null;

      /**
       * Make everything ready to display the trial for a round.
       *
       * @return {void}
       */
      function reset() {
        displayWrongAnswerFeedback(false);
        dispose();

        if (!isPauseScreen(trial)) {
          timeLimitForAnswer = setTimeout(timeLimitHandler, answerTimeLimit * 1000);
          $window.on('keyup', keyUpHandler);
          $('.btn-left').on('click touchstart', leftBtnHandler);
          $('.btn-right').on('click touchstart', rightBtnHandler);
          timer.start();
        } else {
          setWaitingPauseScreen()
        }
      }

      /**
       * Pass the currently displaying pause screen.
       *
       * @return {Object|void}  Resolve promise.
       */
      function setWaitingPauseScreen() {
        dispose();
        setTimeout(function () {
          function next(e) {
            $window.off('keyup', next);
            $window.off('click touchstart', next);
            return deferred.resolve();
          }
          $window.on('keyup', next);
          $window.on('click touchstart', next);
        }, PAUSE_SCREEN_DELAY);
      }

      /**
       * Kill resources used by this round, and reset
       * the trial so that we are ready to pass it again.
       *
       * @return {void}
       */
      function dispose() {
        timer.stop();
        keyPressed = null;

        clearTimeout(timeLimitForAnswer);
        $window.off('keyup', keyUpHandler);
        $('.btn-left').off('click touchstart', leftBtnHandler);
        $('.btn-right').off('click touchstart', rightBtnHandler);
      }

      /**
       * Handler for user input on keyboard.
       *
       * @param  {Object} e jQuery.Event passed to handler.
       * @return {void}
       */
      function keyUpHandler(e) {
        if (!keyPressed) {
          keyPressed = leftAndRightKeys[e.keyCode];
          return checkUserInputValidity(keyPressed);
        }
      }

      /**
       * Check answer validity and resolve promise if valid.
       * Otherwise, reset trial.
       *
       * @param  {string} leftOrRight 'left' or 'right' depending on user's input.
       * @return {Object|void}  Resolve promise if correct.
       */
      function checkUserInputValidity(leftOrRight) {
        if (answerIsOk(leftOrRight)) {
          dispose();
          save('successes', trial, timer.getElapsed())
          return deferred.resolve();
        }

        displayWrongAnswerFeedback(true);
        setError(trial, timer.getElapsed());
      }

      function leftBtnHandler(e) {
        if (!mightBeUsingTablet) {
          mightBeUsingTablet = true;
        }
        e.stopPropagation();
        e.preventDefault();
        return checkUserInputValidity('left');
      }

      function rightBtnHandler(e) {
        if (!mightBeUsingTablet) {
          mightBeUsingTablet = true;
        }
        e.stopPropagation();
        e.preventDefault();
        return checkUserInputValidity('right');
      }

      /**
       * Save a time out or input error for this trial, then reset.
       *
       * @param {Object}  trial    The current trial.
       * @param {String}  timing   The elapsed time for this answer, as taken by the Timer instance.
       * @param {Boolean} timedOut Set true to specify the error is a time out.
       * @return {void}
       */
      function setError(trial, timing, timedOut) {
        save('failures', trial, timing, timedOut);
        reset();
      }

      /**
       * Boolean telling if answer is valid or not.
       *
       * @param  {String} keyPressed 'left' or 'right'.
       * @return {Boolean}
       */
      function answerIsOk(keyPressed) {
        if (keyPressed && trial.correctPosition === keyPressed) {
          return true;
        }
        return false;
      }

      /**
       * Triggered on time out... store time out as an error,
       * and reset the trial silently (don't display red X).
       *
       * @return {void}
       */
      function timeLimitHandler() {
        setError(trial, timer.getElapsed(), true);
      }

      // Start process.
      reset();

      return deferred.promise();
    }

    /**
     * Compute stored JSON data and transform it into accumulative
     * arrays of CSV-formatted successes/failures during the user's run.
     *
     * @param  {Object} store        An instance of answerStore holding JSON values.
     * @param  {Object} participant  Holds global data on the player used in resulting table.
     * @return {Object} A object with two arrays (successes/failures) cumulating CSV-formatted data.
     */
    function computeResults(store, participant, toCSV) {
      toCSV.successes = toCSV.successes.concat(
        answerStore.successes.map(function (a) {
          // Trial ID, MTurk ID, Code, Label, left category, Right category
          // Stimuli word, Correct position, Correct category, Time taken
          return a.id + ',' + participant.id + ',' + participant.code + ',' +
                 participant.label + ',' + a.left + ',' + a.right + ',' + a.stimuli + ',' +
                 a.correctPosition + ',' + a.correctCategory + ',' + a.timing;
        })
      );

      toCSV.failures = toCSV.failures.concat(
        answerStore.failures.map(function (a) {
          // Trial ID, MTurk ID, Code, Label, left category,
          // Right category, Stimuli word, Correct position, Correct category,
          // Failed by time out, Time taken
          return a.id + ',' + participant.id + ',' + participant.code + ',' +
                 participant.label + ',' + a.left + ',' + a.right + ',' + a.stimuli + ',' +
                 a.correctPosition + ',' + a.correctCategory + ',' +
                 a.timedOut + ',' + a.timing
        })
      );

      return toCSV;
    }

    /**
     * Clean input from remnants of HTML tags.
     *
     * @param  {string} input  The string to clean up.
     * @return {string} The resulting, clean output.
     */
    function cleanHTML(input) {
      return input.split(/<[^>]*>/g).join(' ').trim();
    }

    /**
     * Reduve the given toCSV set of data, from object containing successes/failures
     * arrays of CSV-formatted rows, to an object containing the same fields
     * holding CSV-formatted string, with new line separator between rows.
     *
     * @param  {Object}   toCSV          Input data.
     * @param  {Function} htmlCleanerFn  Function for removing HTML remnants.
     * @return {Object}   The final object with CSV-formatted string properties.
     */
    function finalizeCSV(toCSV, htmlCleanerFn) {  // => {successes: string[], failures: string[], meta: string[]}
      return Object.keys(toCSV)                   // => ['successes', 'failures', 'meta']
                   .map(function (k) {
                     var o = {};
                     o[k] = htmlCleanerFn(toCSV[k].join('\\n'));
                     return o;
                   })                            // => [{'successes': string}, {'failures': string}, {'meta': string}]
                   .reduce(function (a, b) {
                     return Object.assign({}, a, b)
                   }, {});                       // => {successes: string, failures: string, meta: string}
    }

    /**
     * Start the queue of blocks of trials.
     * Built as a promise resolving the answers/failures payload
     * once the entire suite of blocks is completed.
     *
     * @param  {Array} queue Queue of trials objects.
     * @return {Object} Promise.
     */
    function startBlocks(queue, toCSV) {
      var deferred = $.Deferred();
      var currentTrialIndex = 0;
      var totalNumOfTrials = queue.length;

      /**
       * Show the specified trial by updating the UI to display its attribute
       * and returning the promise encapsulating the process of running it.
       *
       * @param  {Object} trial        The trial to display.
       * @param  {int}    trialIndex   Index of currently shown trial/screen.
       * @param  {Object} participant  Holds global data on the player used in resulting table.
       * @return {Object} Promise.
       */
      var showTrial = function (trial, trialIndex, participant, toCSV) {
        if (trialIndex > 0 && isPauseScreen(trial)) {
          toCSV = Object.assign({}, toCSV, computeResults(answerStore, participant, toCSV));
        }

        updateUIText(trial, queue, trialIndex);
        return waitForAnswer(trial);
      };

      /**
       * Pass and show next trial. Do it recursively as long as
       * you have trials to display. When queue of trials is empty,
       * resolve promise with all the results.
       *
       * @param  {int}      trialIndex     Index of currently shown trial/screen.
       * @param  {Object}   participant    Holds global data on the player used in resulting table.
       * @param  {Function} htmlCleanerFn  Function for removing HTML remnants.
       */
      var loadTrial = function (trialIndex, participant, htmlCleanerFn) {
        if (trialIndex < totalNumOfTrials) {
          currentTrialIndex++;

          return showTrial(queue[trialIndex], trialIndex, participant, toCSV)
            .then(function () {
              return loadTrial(currentTrialIndex, participant, htmlCleanerFn);
            });
        } else {
          deferred.resolve(finalizeCSV(toCSV, htmlCleanerFn));
        }
      };

      // Start first trial.
      loadTrial(0, participant, cleanHTML, toCSV);

      return deferred.promise();
    }

    /**
     * Public API.
     */
    return {
      begin: function (data, order, lang) {
        console.log('IAT Starting — current locale is "' + lang + '"');
        return loadBlocks(data, order, lang, new Date().toUTCString(), toCSV);
      }
    }
  })(window, undefined);

}(window, undefined));
