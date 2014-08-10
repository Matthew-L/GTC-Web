$(function () {
  'use strict';
  $.fn.editable.defaults.mode = 'inline';
  $.fn.editable.defaults.anim = 'true';
  $.fn.editable.defaults.onblur = 'submit';

//  $.fn.editable.defaults.url = '/post';
  $.fn.editableform.buttons = '';
  $('#string-set-name').editable({
    type: 'text'
  });

  $('#description a').editable({
    type: 'textarea'
  });

  $('#scale-length a').editable({
    type: 'text'
  });


  $('.note a').editable({
    type: 'select',
    source: [
      { text: 'A'},
      { text: 'A#/Bb'},
      { text: 'B'},
      { text: 'C'},
      { text: 'C#/Db'},
      { text: 'D'},
      { text: 'D#/Eb'},
      { text: 'E'},
      { text: 'F'},
      { text: 'F#/Gb'},
      { text: 'G'},
      { text: 'G#/Ab'}
    ]
  });

  $('.octave a').editable({
    type: 'select',
    source: [
      { text: '0'},
      { text: '1'},
      { text: '2'},
      { text: '3'},
      { text: '4'},
      { text: '5'},
      { text: '6'},
      { text: '7'},
      { text: '8'},
      { text: '9'}
    ]
  });

  $('.gauge a').editable({
    type: 'text'
  });

  $('.string-material a').editable({
    type: 'select',
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
});