/*exported loadStringSet*/
/*jshint camelcase: false */
/*exported getRowInputs*/

function formatGauge(gauge) {
  'use strict';
  gauge = (parseFloat(gauge).toString()).replace(/^[0]+/gi, '');
  return gauge;
}

function addRow(index) {
  'use strict';
  var row = $('#strings-table tr:last');
  var clone = row.clone();
  clone.attr('id', 'string-row-' + index);
  row.after(clone);
  $('#strings-table').find('tr:last > td > .string-number').text(index);
  return(row);
}

function loadRow(guitarString) {
  'use strict';
  var index = guitarString.string_number;
  if (index !== 1) {
    addRow(index);
  } else {
    $('#scale-length').find('a').text(guitarString.scale_length);
  }
  var row = '#string-row-' + index;

  $.each(guitarString, function (key, value) {
    if (key === 'string_type') {
      $(row + '> td > .' + 'string-type > a').attr('data-value', value);
    } else if (key === 'gauge') {
      $(row + '> td > .' + key + '> a').attr('data-value', formatGauge(value));
    }
    else {
      $(row + '> td > .' + key + '> a').attr('data-value', value);
    }
  });
  calculateString(guitarString);
}

function iterateGuitarString(string) {
  'use strict';
  var stringDict = {};
  $.each(string, function (key, value) {
    stringDict[key] = value;
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

function makeRowDict(scale_length, string_number, note, octave, gauge, string_type, total_strings) {
  'use strict';
  return {
    scale_length: scale_length,
    string_number: string_number,
    note: note,
    octave: octave,
    gauge: gauge,
    string_material: string_type,
    total_strings: total_strings
  };
}

function getRowDataValue(row, key) {
  'use strict';
  return $('#' + row + '> td > ' + key + ' > a').attr('data-value');
}

function getRowText(row, key) {
  'use strict';
  return $('#' + row + '> td > ' + key + ' > a').text();
}

function getTotalStrings() {
  return $('#strings-table').find('tr:last > td > .string-number').text();
}

function getRowInputs(row) {
  'use strict';


  return {
    string_number: $('#' + row + '> td > .string-number').text(),
    note: getRowText(row, '.note'),
    octave: getRowText(row, '.octave'),
    gauge: getRowText(row, '.gauge'),
    string_type: getRowDataValue(row, '.string-type')
  };
}


function getScaleLength() {
  'use strict';
  return $('#scale-length').find('> a').text();
}
function calculateSingleString(guitarString) {
  'use strict';
  guitarString.scale_length = getScaleLength();
  calculateString(guitarString);
}

function calculateAllRows(scaleLength) {
  'use strict';
  for (var i = 1; i <= getTotalStrings(); ++i) {
    var guitarString = getRowInputs('string-row-' + i);
    guitarString.scale_length = scaleLength;
    calculateString(guitarString);
  }
}

function updateStringNumber(row, index) {
  'use strict';
  row.id = 'string-row-' + (index + 1);
  $('#' + row.id + ' > td > .string-number').text(index + 1);
}
function updateAllStringNumbers() {
  'use strict';
  var rows = $('.sortable-row');
  for (var i = 0; i < rows.length; ++i) {
    updateStringNumber(rows[i], i);
  }
  calculateAllRows(getScaleLength());
}
