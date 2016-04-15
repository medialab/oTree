$(function(window, undefined) {
  /**
   * Timer for measuring user input speed.
   * It's a self-correcting timer to compense for the latency
   * induced by depending upon CPU time (which itself is
   * dependant on its current load).
   *
   * @see http://www.sitepoint.com/creating-accurate-timers-in-javascript/
   */
  var Timer = (function() {
    var startTime = new Date().getTime();
    var time = 0;
    var elapsed = 0;
    var timer = null;

    // Process calculations with auto-correction.
    var instance = function() {
      time += 100;
      elapsed = (time / 100) / 10;
      var diff = (new Date().getTime() - startTime) - time;
      window.setTimeout(instance, (100 - diff));
    }.bind(this);

    // Starts the timer.
    var start = function() {
      if (startTime === null) {
        startTime = new Date().getTime();
      }

      time = 0;
      elapsed = 0;
      timer = window.setTimeout(instance, 100);
    }.bind(this);

    // Stops the timer.
    var stop = function() {
      startTime = null;
      clearTimeout(timer);
    }.bind(this);

    // Return elpased time.
    var getElapsed = function() {
      return elapsed;
    };

    // Public API.
    return {
      start: start,
      stop: stop,
      getElapsed: getElapsed,
    };
  })();

  window.IAT = (function(window, undefined) {
    /**
     * Reference to UI pieces manipulated via jQuery.
     */
    var $uiCategoryLeft = $('.left'),
        $uiCategoryRight = $('.right'),
        $uiStimuli = $('.stimuli'),
        $uiWrongAnswerCross = $('.wrong-answer'),
        $window = $(window),
        mightBeUsingTablet = false;

    var answerStore = {
      results: [],
      errors: [],
    };

    /**
     * Informations to be taken from config.
     */
    var keyCodeLeft = null,
        keyCodeRight = null,
        answerTimeLimit = null,
        leftAndRightKeys = {};

    /**
     * Update text on UI - left and right category, stimuli word.
     * @param  {Object} data Trial data.
     * @return {void}
     */
    function updateUIText(data) {
      $uiCategoryLeft.html(data.left);
      $uiCategoryRight.html(data.right);
      $uiStimuli.html(data.stimuli);
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
          .animate({opacity: 0}, 100, function() {
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
      return str[0].toUpperCase() + str.slice(1);
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
      var resultTrials = [];

      // Arrange the trials based on given order.
      order.split('').forEach(function(character) {
        data.trials[character].displayed.forEach(function(displayed) {
          resultTrials.push({
            correctCategory: capitalize(displayed[displayed.correct]),
            stimuli: displayed.showing[lang],
            left: capitalize(displayed.left),
            right: capitalize(displayed.right),
            correctPosition: displayed.correct,
            blockName: displayed.name
          });
        });
      });

      return resultTrials;
    }

    function setKeyCodesAndTimeLimitFromConfig(dataStore) {
      keyCodeLeft = dataStore.config.keycodes.left;
      keyCodeRight = dataStore.config.keycodes.right;
      answerTimeLimit = dataStore.config.answer_time_limit;
      leftAndRightKeys[keyCodeLeft] = 'left';
      leftAndRightKeys[keyCodeRight] = 'right';
    }

    /**
     * Load up and start the queue of trials, one after the next,
     * then return the results as a promise.
     *
     * @param  {Array}  dataStore
     * @param  {string} order The order of passage, such as "A B C D"...
     * @param  {string} lang  Language code to base sets on.
     * @return {Object} A promise resolving with the results payload.
     */
    function loadBlocks(dataStore, order, lang) {
      setKeyCodesAndTimeLimitFromConfig(dataStore);

      var deferred = $.Deferred();

      startBlocks(prepareTrials(dataStore, order, lang))
        .then(function(results) {
          var errorPercentage = (results.errors.length / results.results.length) * 100;
          results['error_percentage'] = errorPercentage;

          results['order'] = order;

          var platform = mightBeUsingTablet ? 'tablet' : 'desktop';
          results['platform'] = platform;

          return deferred.resolve(results);
        });

      return deferred.promise();
    }

    /**
     * Save the correct or wrong input from user, with timing for each round.
     *
     * @param  {String} type   'results' or 'errors', according to the keys in `answerStore`.
     * @param  {Object} trial  The current trial object.
     * @param  {String} timing The elapsed time for this answer, as taken by the Timer instance.
     * @return {void}
     */
    function save(type, trial, timing, timedOut) {
      answerStore[type].push(
        Object.assign({}, trial, {timing: timing, timedOut: timedOut ? true : false}
      ));
    }

    /**
     * Promise encapsulating all the process of waiting for the user's answer.
     * It does resolve anything, but when it does resolve, it means the current trial is finished,
     * and we have saved results (and optional errors).
     *
     * @param  {Object} trial The current trial.
     * @return {Object} Promise, resolved when trial is done.
     */
    function waitForAnswer(trial) {
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
        // console.log('showing', trial);
        displayWrongAnswerFeedback(false);
        dispose();

        timeLimitForAnswer = setTimeout(timeLimitHandler, answerTimeLimit * 1000);
        $window.on('keyup', keyUpHandler);
        $('.btn-left').on('click', leftBtnHandler);
        $('.btn-right').on('click', rightBtnHandler);
        timer.start();
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
        $('.btn-left').off('click', leftBtnHandler);
        $('.btn-right').off('click', rightBtnHandler);
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
          save('results', trial, timer.getElapsed())
          dispose();
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
        save('errors', trial, timing, timedOut);
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
       * and reset the trial.
       *
       * @return {void}
       */
      function timeLimitHandler() {
        displayWrongAnswerFeedback(true);
        setError(trial, timer.getElapsed(), true);
      }

      // Start process.
      reset();

      return deferred.promise();
    }

    /**
     * Start the queue of blocks of trials.
     * Built as a promise resolving the answers/errors payload
     * once the entire suite of blocks is completed.
     *
     * @param  {Array} queue Queue of trials objects.
     * @return {Object} Promise.
     */
    function startBlocks(queue) {
      var deferred = $.Deferred();
      var currentTrialIndex = 0;
      var totalNumOfTrials = queue.length;

      /**
       * Show the specified trial by updating the UI to display its attribute
       * and returning the promise encapsulating the process of running it.
       *
       * @param  {Object} trial The trial to display.
       * @return {Object} Promise.
       */
      var showTrial = function(trial) {
        updateUIText(trial);
        return waitForAnswer(trial);
      };

      var loadTrial = function(trialIndex) {
        // Pass and show next trial. Do it recursively as long as
        // you have trials to display. When queue of trials is empty,
        // resolve promise with all the results.
        if (trialIndex < totalNumOfTrials) {
          currentTrialIndex++;

          return showTrial(queue[trialIndex])
            .then(function() {
              return loadTrial(currentTrialIndex);
            });
        } else {
          deferred.resolve(answerStore);
        }
      };

      // Start first trial.
      loadTrial(0);

      return deferred.promise();
    }

    /**
     * Public API.
     */
    return {
      begin: function(data, order, lang) {
        return loadBlocks(data, order, lang);
      }
    }
  })(window, undefined);

}(window, undefined));
