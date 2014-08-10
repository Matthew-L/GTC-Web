/*exported loadStringSet*/
/*jshint camelcase: false */


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
  $('#strings-table tr:last > td > .string-number').text(index);
  return(row);
}

function loadRow(guitarString) {
  'use strict';
  var index = guitarString.string_number;
  if (index !== 1) {
    addRow(index);
  } else {
    $('#scale-length a').text(guitarString.scale_length);
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
