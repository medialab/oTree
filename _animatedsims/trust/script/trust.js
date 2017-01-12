/**
 * THIS IS THE MAIN SCRIPT FOR THE TRUST GAME SIMULATION,
 * AS FOUND IN THE ADOBE ANIMATOR SOURCE (./trust_simulation/trust_simulation.xfl).
 *
 * THIS FILE EXISTS AND SHOULD BE UPDATED TO ALLOW A QUICK VIEW
 * OF THE CODE BASE WHEN BROWSING THE REPO.
 */

if (!window) {
  throw new Error('window object not found');
}


/**
 * Get or define values.
 * Defaults to 'fr' values.
 * Read FAQ to learn how to set values:
 * TODO: add FAQ URL
 */
var locale = 'fr';
var startAmount = 10;
var multiplier = 3;
var labelA = 'participant A';
var labelB = 'participant B';
var currency = '€';

if (window.document) {
  var canvas = document.getElementsByName('canvas')[0];

  // Override defaults with data-attributes found on host canvas.
  if (canvas) {
    locale = canvas.getAttribute('data-locale') || locale;
    labelA = canvas.getAttribute('data-participants-label-a') || labelA;
    labelB = canvas.getAttribute('data-participants-label-b') || labelB;
    multiplier = canvas.getAttribute('data-multiplier') || multiplier;
    startAmount = canvas.getAttribute('data-start-amount') || startAmount;
    currency = canvas.getAttribute('data-currency') || currency;
  }
}

/**
 * MAIN
 * ----
 */
var players = Players.bind(this)();
var carts = Carts.bind(this)();

window.TRUST = init.bind(this)();

function init() {
  return {
    operate: operate.bind(this)(players, carts),
    reset: reset.bind(this)
  };
}

function reset() {
  this.gotoAndPlay('start');
  players.reset();
  carts.reset();
}

function operate(players, carts) {
  function playerPutsOwnMoney(pIndex, cIndex, color) {
    if (players.decrement(pIndex)) {
      carts.increment(cIndex, color ? color : (pIndex === 0 ? 'green' : 'orange'));
    }
  }

  function playerTakesMoney(pIndex, cIndex, color) {
    if (carts.decrement(cIndex)) {
      players.increment(pIndex, color);
    }
  }

  function moveCart(index) {
    return function () {
      return carts.move(index);
    };
  }

  function moveMoneyFromCartToCart(from, to) {
    return function () {
      if (carts.decrement(from)) {
        return carts.increment(to, 'grey');
      }
    };
  }

  function passInFactory() {
    carts.multiply(0, multiplier);
  }

  function dispatchFinalGains() {
    var giveToPlayer1 = carts.removeAll(1);
    for (var i = 0; i < giveToPlayer1; i++) {
      players.increment(0, 'grey');
    }

    var giveToPlayer2 = carts.removeAll(0);
    for (var j = 0; j < giveToPlayer2; j++) {
      players.increment(1, 'grey', true);
    }
  }

  function getMaxCartMoney(index) {
    return function () {
      return carts.getCarts()[index].money;
    };
  }

  function getMaxPlayerMoney(index) {
    return function () {
      return players.getPlayers()[index].money;
    };
  }

  return {
    playerPutsOwnMoney: playerPutsOwnMoney,
    playerTakesMoney: playerTakesMoney,
    moveCart1: moveCart.call(this, 0),
    moveCart2: moveCart.call(this, 1),
    passInFactory: passInFactory,
    incrementFromCartToCart: moveMoneyFromCartToCart.call(this, 0, 1),
    decrementFromCartToCart: moveMoneyFromCartToCart.call(this, 1, 0),
    dispatchFinalGains: dispatchFinalGains,

    getMaxCart1Money: getMaxCartMoney.call(this, 0),
    getMaxCart2Money: getMaxCartMoney.call(this, 1),
    getMaxPlayer1Money: getMaxPlayerMoney.call(this, 0),
    getMaxPlayer2Money: getMaxPlayerMoney.call(this, 0)
  };
}

/**
 * HELPER FUNCTIONS
 * ----------------
 */
function createBanknote(color) {
  if (!lib) throw new Error('Animate\'s "lib" namespace could not be found');

  var Note = lib['dollar' + color.substring(0, 1).toUpperCase() + color.substring(1).toLowerCase()];
  if (!Note) throw new Error('Could not create banknote based on color ' + color);
  return new Note();
}

function setMoneyText(amount) {
  return currency + amount.toString();
}

function canUpdateBanknotes(amount) {
  return locale !== 'ko' || (locale === 'ko' && amount % 1000 === 0);
}

/**
 * ENTITIES
 * --------
 */
function Carts() {
  // Constants used for placing banknotes.
  var X_OFFSET = 18;
  var Y_OFFSET = 9;
  var Z_OFFSET = 3;

  // Store references to cart-related data in a dedicated array.
  // - money is the amount of money held on the cart
  // - color is a string referencing the color of the relevant UI banknote element
  // - instance references the UI element of one of the 2 carts
  // - stack is an array of references of UI banknote elements displayed on this cart
  var carts = [{
    money: 0,
    color: '',
    instance: this.cart1,
    stack: []
  }, {
    money: 0,
    color: '',
    instance: this.cart2,
    stack: []
  }];

  // Below are references of UI elements in Animate's library.
  // Set default values for starters, and Korean font display.
  this.cart1.bubble.alpha = 0;
  this.cart2.bubble.alpha = 0;

  if (locale === 'ko') {
    this.cart1.bubble.label.font = "18px 'Gotham Medium'";
    this.cart2.bubble.label.font = "18px 'Gotham Medium'";
  }

  function increment(index, color) {
    var banknote = createBanknote(color);
    var cart = carts[index];
    banknote.x = X_OFFSET;
    banknote.y = Y_OFFSET - Z_OFFSET * cart.stack.length;
    addMoney(cart, banknote);
  }

  function decrement(index) {
    return removeMoney(carts[index]);
  }

  function move(index) {
    if (+index === 0) {
      this.gotoAndPlay('first_move');
    } else {
      this.gotoAndPlay('second_move');
      setTimeout(function () {
        this.cart1.bubble.alpha = 0;
        this.cart2.bubble.alpha = 0;
      }.bind(this), 2000);
    }
  }

  function multiply(index) {
    if (!window.TRUST) throw new Error('Could not find namespace TRUST');

    var newAmount = carts[index].money * multiplier;
    window.TRUST.multipliedMoney = newAmount;

    batchRemoveMoney(index);
    batchAddMoney(index, newAmount, 'grey');
  }

  function reset() {
    this.cart1.bubble.alpha = 0;
    this.cart2.bubble.alpha = 0;

    this.cart1.money = 0;
    this.cart2.money = 0;

    this.cart1.stack = [];
    this.cart2.stack = [];
  }

  function getCarts() {
    return carts;
  }

  function addMoney(cart, banknote) {
    // Increment money and update displayed stack of banknotes.
    // Korean should add new banknote once every 1000 won.
    if (canUpdateBanknotes(++cart.money)) {
      cart.stack.push(banknote);
      setTimeout(function () {
        cart.instance.addChild(banknote);
      }, 0);
    }

    // Update text UI accordingly.
    if (cart.instance.bubble.alpha < 1) {
      cart.instance.bubble.alpha = 1;
    }

    cart.instance.bubble.label.text = setMoneyText(cart.money);
  }

  function removeMoney(cart) {
    if (cart.money > 0) {
      if (canUpdateBanknotes(--cart.money)) {
        var removed = cart.stack.pop();
        setTimeout(function () {
          cart.instance.removeChild(removed);
        }, 0);
      }
      cart.instance.bubble.label.text = setMoneyText(cart.money);
      return true;
    }

    return false;
  }

  function batchAddMoney(index, amount, color) {
    for (var i = 0; i < amount; i++) {
      increment(index, color);
    }
  }

  function batchRemoveMoney(index) {
    var cart = carts[index];
    var total = cart.money;
    while (cart.money > 0) {
      decrement(index);
    }
    return total;
  }

  return {
    increment: increment.bind(this),
    decrement: decrement.bind(this),
    multiply: multiply.bind(this),
    removeAll: batchRemoveMoney.bind(this),
    reset: reset.bind(this),
    getCarts: getCarts.bind(this),
    move: move.bind(this)
  };
}

function Players() {
  var X_OFFSET = 0;
  var Y_OFFSET = 22.5;
  var Z_OFFSET = 2.5;

  // Store references to player-related data in a dedicated array.
  // - money is the amount of money the player owns
  // - instance references the UI element representing a stack of banknotes next to her
  // - stack is an array of references of UI banknote elements
  var players = [{
    money: 0,
    instance: this.stack1,
    bubble: this.bubble1,
    stack: []
  }, {
    money: 0,
    instance: this.stack2,
    bubble: this.bubble2,
    stack: []
  }];

  reset();

  function setBubble(index, amount) {
    players[index].bubble.label.text = setMoneyText(amount);
  }

  function addMoney(player, banknote, index) {
    if (canUpdateBanknotes(++player.money)) {
      player.stack.push(banknote);
      setTimeout(function () {
        player.instance.addChild(banknote);
      }, 0);
    }

    setBubble(index, player.money)
  }

  function removeMoney(player, index) {
    if (player.money > 0) {
      setBubble(index, --player.money)

      if (canUpdateBanknotes(player.money)) {
        var removed = player.stack.pop()
        setTimeout(function () {
          player.instance.removeChild(removed);
        }, 0);
      }

      return true;
    }
    return false;
  }

  function increment(index, color, force) {
    var banknote = createBanknote(color);
    var player = players[index];
    banknote.x = X_OFFSET;
    banknote.y = Y_OFFSET - Z_OFFSET * player.stack.length;

    addMoney(player, banknote, index);
  }

  function decrement(index) {
    return removeMoney(players[index], index);
  }

  function reset() {
    players.forEach(function (player, index) {
      while (player.money > 0) {
        decrement(index);
      }

      while (player.money < startAmount) {
        increment(index, ['green', 'orange'][index]);
      }
    });
  }

  function getPlayers() {
    return players;
  }

  return {
    increment: increment.bind(this),
    decrement: decrement.bind(this),
    reset: reset.bind(this),
    getPlayers: getPlayers.bind(this)
  };
}
