// Circumvent bug in IE10 and above where range inputs DO have the "oninput" event,
// but DO NOT actually trigger it (false positive!)
// @see https://connect.microsoft.com/IE/feedback/details/856998/input-type-range-oninput-missing-onchange-wrong
function getInputEventName() {
  if (navigator.userAgent.match(/MSIE 10/i) || navigator.userAgent.match(/Trident\/7\./)) {
    return 'change';
  }
  return 'input'
}
