function setColorValidation(element, valid) {
  'use strict';
  if (valid) {
    $(element).css('border-bottom', 'solid 1px #5cb85c');
  } else {
    $(element).css('border-bottom', 'solid 1px #d2322d');
  }
}

function isFloat(input) {
  'use strict';
  var floatRegex = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
  return !!floatRegex.test(input);
}

function isValidScaleLength(length) {
  'use strict';
  var lengths = length.split('-', 2);
  if (lengths.length === 2) {
    if (lengths[0] + '-' + lengths[1] !== length) {
      return false;
    }
  }
  for (var i = 0; i < lengths.length; ++i) {
    console.log(lengths[i]);
    if (!isFloat(lengths[i]) && lengths.length <= 30) {
      return false;
    }
  }
  return true;
}

function isValidGauge(gauge) {
  'use strict';
  return !!(isFloat(gauge) && 0 < gauge && gauge < 1 && gauge.length <= 6);
}

