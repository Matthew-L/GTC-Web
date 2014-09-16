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
      console.log(response)
      var tension = response.tension;
      if (tension < 0) {
        tension = 0;
      }
      console.log(tension);
      $('#string-row-' + index + ' > td > .tension').text(tension);
    },
    error: function (response, error) {
      var json = JSON.parse(response.responseText);
      console.log(json.error);
      $('#calculate-error-alert').removeClass('hidden');
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
      console.log(response);
      alert(response.successMessage);

    },
    error: function (response, error) {
      var json = JSON.parse(response.responseText);
      console.log(json.errors);
      $('#save-error-alert').removeClass('hidden').text(json.errors);
    }
  });
}