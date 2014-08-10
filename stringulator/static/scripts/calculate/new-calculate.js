/*exported loadStringSet*/
/*jshint camelcase: false */
$(document).ready(function () {
  'use strict';

  setListeners();
});

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

function setEditables() {
  'use strict';
  $.fn.editable.defaults.mode = 'inline';
  $.fn.editable.defaults.anim = 'true';
  $.fn.editable.defaults.onblur = 'submit';

  $.fn.editable.defaults.url = '/post';
//  $.fn.editableform.buttons = '';
  $('#string-set-name').editable({
    type: 'text'
  });

  $('#description').find('a').editable({
    type: 'textarea'
  });

  $('#scale-length').find('a').editable({
    type: 'text'
  });


  $('.note a').editable({
    type: 'select',
    showbuttons: false,
//    selector: 'tr',
    source: [
      {value: 'A', text: 'A'},
      {value: 'A#/Bb', text: 'A#/Bb'},
      {value: 'B', text: 'B'},
      {value: 'C', text: 'C'},
      {value: 'C#/Db', text: 'C#/Db'},
      {value: 'D', text: 'D'},
      {value: 'D#/Eb', text: 'D#/Eb'},
      {value: 'E', text: 'E'},
      {value: 'F', text: 'F'},
      {value: 'F#/Gb', text: 'F#/Gb'},
      {value: 'G', text: 'G'},
      {value: 'G#/Ab', text: 'G#/Ab'}
    ]
  });

  $('.octave a').editable({
    type: 'select',
    showbuttons: false,
    source: [
      {value: '0', text: '0'},
      {value: '1', text: '1'},
      {value: '2', text: '2'},
      {value: '3', text: '3'},
      {value: '4', text: '4'},
      {value: '5', text: '5'},
      {value: '6', text: '6'},
      {value: '7', text: '7'},
      {value: '8', text: '8'},
      {value: '9', text: '9'}
    ]
  });

  $('.gauge a').editable({
    type: 'text',
    showbuttons: false
  });

  $('.string-type a').editable({
    type: 'select',
    showbuttons: false,
    source: [
      { text: 'Kalium',
        children: [
          { value: 'CKPLG', text: 'Plain Steel'},
          { value: 'CKWNG', text: 'Nickel/Steel Hybrid'}
        ]
      },
      { text: 'D\'Addario Guitar',
        children: [
          { value: 'DAPL', text: 'Plain Steel'},
          { value: 'DANW', text: 'Nickel Wound'},
          { value: 'DAPB', text: 'Phosphore Bronze Wound'},
          { value: 'DAXS', text: 'Stainless Steel Wound'},
          { value: 'DAHR', text: 'Half-Round Wound'},
          { value: 'DACG', text: 'Chromes - Stainless Flat Wound'},
          { value: 'DAFT', text: 'Flat Tops - Phosphore Bronze'},
          { value: 'DABW', text: '80/20 Brass Round Wound'},
          { value: 'DAZW', text: '85/15 Great American Bronze'},
        ]
      },
      { text: 'D\'Addario Bass',
        children: [
          { value: 'DAXB', text: 'Nickel Wound'},
          { value: 'DAHB', text: 'Pure Nickel Half Round'},
          { value: 'DABC', text: 'Stainless Steel Flat Wound'},
          { value: 'DABS', text: 'ProSteel Round Wound'}
        ]
      }
    ]
  });
}


function setListeners() {
  'use strict';

  $('.delete').click(function () {
    console.log('here');
    $(this).closest('tr').remove();
  });

  $('#insert-more').click(function () {
    'use strict';
    var index = parseInt($('#strings-table').find('tr:last').attr('id').split('-')[2]);
    console.log('split' + index);
    addRow(index + 1);
    setListeners();
  });
  setEditables();
}