
function validateScaleLength(scale_length) {

  var is_mscale = $("#mscale_checkbox").is(':checked');
  var is_valid = false;

  if (is_mscale) {
    var arr;
    arr = scale_length.split("-", 2)
    if (scale_length == arr[0] + "-" + arr[1]) {
      if (isFloat(arr[0]) && isFloat(arr[1])) {
        if (scale_length.length <= 30)
          is_valid = true;
      }
    }
  } else {
    if (isFloat(scale_length)) {
      if (scale_length.length <= 30)
        is_valid = true;
    }
  }
  return is_valid;
}

function validateGauge(gauge) {

  var is_valid = false;
  if (isFloat(gauge)) {
    if (0 < gauge && gauge < 1) {
      if (gauge.length <= 6)
        is_valid = true;
    }
  }
  return is_valid;
}

function validateStringNumber(string_number) {
  var is_valid = false;
  if (isInt(string_number)) {
    if (string_number > 0) {

      var is_mscale = $("#mscale_checkbox").is(':checked');
      if (is_mscale) {
        var number_of_strings = $("#number_of_strings").val();
        if (isInt(number_of_strings)) {
          if (parseInt(number_of_strings) >= parseInt(string_number)) {
            if (string_number.length <= 2)
              is_valid = true;
          }
        }
      }
      else {
        if (string_number.length <= 2)
          is_valid = true;
      }

    }
  }

  return is_valid
}

function validateNumberOfStrings(number_of_strings) {
  if (isInt(number_of_strings))
    if (number_of_strings.length <= 2)
      return true;
  return false;
}


//function validateDropdown(dropdown_value) {
//  if (dropdown_value != '-')
//    return true;
//  return false;
//}


//function colorValid(id, is_valid) {
//  if (is_valid) {
//    $(id).css("background-color", "#5cb85c");
//  } else {
//    $(id).css("background-color", "#d2322d");
//  }
//}

function isInt(input) {
  var int_regex = /^\d+$/;
  if (int_regex.test(input))
    return true;
  else
    return false;
}

function isFloat(input) {
  var float_regex = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
  if (float_regex.test(input))
    return true;
  else
    return false;
}

function setColorValidation(element, valid){
  if(valid){
    $(element).css("border-bottom", "solid 1px #5cb85c");
  }else {
    $(element).css("border-bottom", "solid 1px #d2322d");
  }
}

function validateNote(note){
  return note
}