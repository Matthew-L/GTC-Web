function showSuccess(){
  'use strict';
  $('#success-alert').removeClass('hidden');
}

function displayErrors(errors){
  'use strict';
  $('#error-alert').removeClass('hidden');
  $('#error-message > li').remove();
  for(var i = 0; i < errors.length; ++i){
    console.log(errors[i].toString());
    $('#error-message').append('<li>'+errors[i].toString()+'</li>');
  }
}

function hideErrors(){
  'use strict';
  $('#error-alert').addClass('hidden');
}

function calculateString(row) {
  'use strict';
  console.log(row);
  /* jshint camelcase: false */
  var index = row.string_number;
  $.ajax({
    type: 'POST',
    url: '/calculate-tension/',

    data: {
      scale_length: row.scale_length,
      string_number: row.string_number,
      note: row.note,
      octave: row.octave,
      gauge: row.gauge,
      string_type: row.string_type,
      total_strings: getTotalStrings()
    },
    /* jshint camelcase: true*/
    dataType: 'json',
    success: function (response) {
      console.log(response);
      var tension = response.tension;
      if (tension < 0) {
        tension = 0;
      }
      console.log(tension);
      $('#string-row-' + index + ' > td > .tension').text(tension);
      hideErrors();
    },
    error: function (response, error) {
      var json = JSON.parse(response.responseText);
      console.log(json.error);
//      displayErrors(json.errors);
    }
  });
}

function saveStringSet(set){
    'use strict';
  console.log(set);
  /* jshint camelcase: false */

  $.ajax({
    type: 'POST',
    url: '/save-set/',

    data: {
      old_name: getOldName(),
      name: set.name,
      description: set.description,
      scale_length: set.scale_length,
      row: set.rows,
      total_strings: getTotalStrings()
    },
    /* jshint camelcase: true*/
    dataType: 'json',
    success: function (response) {
      showSuccess();
      console.log(response);
      hideErrors();
    },
    error: function (response, error) {
      var json = JSON.parse(response.responseText);
      console.log(json.errors);
      displayErrors(json.errors);

    }
  });
}