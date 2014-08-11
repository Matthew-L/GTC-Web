/*globals addRow*/
/*jshint latedef: false*/
function setAddRowListener() {
  'use strict';
  $('#insert-more').click(function () {
    var index = parseInt($('#strings-table').find('tr:last').attr('id').split('-')[2]);
    console.log('split' + index);
    addRow(index + 1);
    setRowListeners();
  });
}

function setRowListeners() {
  'use strict';

  setDeleteRowListeners();
  setEditableListeners();
}

function setEditableListeners() {
  'use strict';
  $.fn.editable.defaults.mode = 'inline';
  $.fn.editable.defaults.anim = 'true';
  $.fn.editable.defaults.onblur = 'submit';

  $.fn.editable.defaults.url = '/post';
//  $.fn.editableform.buttons = '';
  $('#string-set-name').find('a').editable({
    type: 'text',
    success: function (response, newValue) {
//      setColorValidation($(this), validateName(newValue));
    },
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });

  $('#description').find('a').editable({
    type: 'textarea',
    success: function (response, newValue) {
//      setColorValidation(note, newValue);
    },
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });

  $('#scale-length').find('a').editable({
    type: 'text',
    success: function (response, newValue) {
//      setColorValidation(note, newValue);
    },
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });


  $('.note a').editable({
    type: 'select',
    showbuttons: false,
    success: function (response, newValue) {
//      setColorValidation($(this), newValue);
    },
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
    ],
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });

  $('.octave a').editable({
    type: 'select',
    showbuttons: false,
    success: function (response, newValue) {
//      setColorValidation(note, newValue);
    },
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
    ],
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });

  $('.gauge a').editable({
    type: 'text',
    success: function (response, newValue) {
//      setColorValidation(note, newValue);
    },
    showbuttons: false,
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });

  $('.string-type a').editable({
    type: 'select',
    showbuttons: false,
    success: function (response, newValue) {
//      setColorValidation(note, newValue);
    },
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
          { value: 'DAZW', text: '85/15 Great American Bronze'}
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
    ],
    validate: function (value) {
      if ($.trim(value) == '') {
        return 'This field is required';
      }
    }
  });
}

function setDeleteRowListeners() {
  'use strict';
  $('.delete').click(function () {
    console.log('here');
    var row = $(this).closest('tr');
    $('#delete-alert').removeClass('hidden');
    $('#confirm-delete').click(function () {
      $('#delete-alert').addClass('hidden');
      row.remove();
    });
    $('#cancel-delete').click(function () {
      $('#delete-alert').addClass('hidden');
    });
  });
}

$(document).ready(function () {
  'use strict';
  setRowListeners();
  setAddRowListener();
});


