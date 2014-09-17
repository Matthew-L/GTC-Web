$(document).ready(function () {
  'use strict';

  var ajaxDelete = function(user, setName) {
    $.ajax({
      type: 'POST',
      url: '/delete-set/',
      data: {
        user: user,
        setName: setName
      },
      dataType: 'json',
      success: function (response) {

      },
      error: function (response, error) {
        alert('ERROR!');
      }
    });
  };

  $('.delete-set-btn').click(function () {
    if (confirm('Are you sure you want delete this entire set?')) {
      var user = $(this).data('user');
      var setName = $(this).data('set');
      var rowNumber = $(this).data('row');
      ajaxDelete(user, setName);
      $('#row-' + rowNumber).slideUp();
    }
  });

});
