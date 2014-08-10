/*exported loadStringSet*/
/*jshint camelcase: false */

function formatGauge(gauge) {
  'use strict';
  gauge = (parseFloat(gauge).toString()).replace(/^[0]+/gi, '');
  return gauge;
}

function loadRow(guitarString) {
  'use strict';
  addRow();
  $('#scale-length a').text(guitarString.scale_length);
  console.log('test');
//  $('#string-set-name a').text('setValue', '')
}

function addRow() {

}

function iterateGuitarString(string) {
  'use strict';
  var stringDict = {};
  $.each(string, function (key, value) {
    stringDict[key] = value;
    console.log(key + stringDict[key]);
  });
  return stringDict;
}

function loadStringSet(json) {
  'use strict';
  for (var i = 0, len = json.length; i < len; ++i) {
    var guitarString = json[i].fields;
    guitarString = iterateGuitarString(guitarString);
    loadRow(guitarString);
  }
}
