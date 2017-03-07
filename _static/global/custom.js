// Circumvent bug in IE10 and above where range inputs DO have the "oninput" event,
// but DO NOT actually trigger it (false positive!)
// @see https://connect.microsoft.com/IE/feedback/details/856998/input-type-range-oninput-missing-onchange-wrong
function getInputEventName() {
  if (navigator.userAgent.match(/MSIE 10/i) || navigator.userAgent.match(/Trident\/7\./)) {
    return 'change';
  }
  return 'input'
}

function buildRedirectionLink(redirectionUrl, participantLabel) {
  var vars = participantLabel.split('|').filter(function (f) {
    if (f.indexOf('ac') > -1 || f.indexOf('sn') > -1) {
      return f;
    }
  }).join('&');

  return redirectionUrl + '&' + vars;
}
