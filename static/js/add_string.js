/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {
        addChangeEvent();
    });


function addChangeEvent() {

    $("#mscale_checkbox").click(function () {
        console.log('hi')
        $(".hidden_row").slideToggle("slow");
    })

    var counter = 1;
    $(".addstring_btn").click(function () {
        var row = "#string_row" + counter
        $(row).show("slide")
        counter += 1;
    })

    $(".remove_btn").click(function () {
        var curr = this.id.substr(this.id.length - 1)
        $("#string_row_GTC_" + curr).toggle();
    })

    $(".dropdown_input").on("change", validateInput);
    $(".user_input").keyup(validateInput);


    last_row = $('#strings-tbl tr:last');
    last_row.css('display', 'none');
    last_row.insertAfter('#strings-tbl tr:last');
    last_row.fadeIn('slow');
}

function validateInput(){
    var id = "#" + this.id
    var val = $(id).val()
    var is_valid;

    if( $(id).hasClass("dropdown_input") ){
        is_valid = validateDropdown(val)
    }
    else if($(id).hasClass("string_number_input")){
        is_valid = validateStringNumber(val);
    }
    else if($(id).hasClass("number_of_strings_input")){
        is_valid = validateNumberOfStrings(val);
        return;
    }
    else if($(id).hasClass("gauge_input")){
        is_valid = validateGauge(val);
    }
    else if($(id).hasClass("scale_length_input")){
        is_valid = validateScaleLength(val);
        return;
    }


    colorValid(id, is_valid);
    if(is_valid){

        var curr = id.substr(id.length - 1);
        calculate(curr)
    }

}

function countValidRows() {
    var lastid = $('#strings-tbl tr:last-child').find("div").attr('id')
    var curr = lastid.substr(lastid.length - 1);
    return curr;
}

function ajaxCalculate(name, desc, is_mscale, scale_length, string_number, note, octave, gauge, string_type, number_of_strings, curr) {
    $.ajax({
        type: "POST",
        url: "/ajax/",
        data: {
            string_set_name: name,
            desc: desc,
            is_mscale: is_mscale,
            scale_length: scale_length,
            string_number: string_number,
            note: note,
            octave: octave,
            gauge: gauge,
            string_type: string_type,
            number_of_strings: number_of_strings
        },
        dataType: "json",
        success: function (response) {
            console.log(response.tension);
            $('#tension_GTC_' + curr).text(response.tension);
        },
        error: function (response, error) {
            alert("ERROR!");
        }
    })
}

function check_valid_scale(is_mscale, number_of_strings) {
    var is_valid_scale = false;

    if (is_mscale) {
        var numberRegex = /^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$/; //checks for digit
        if (numberRegex.test(number_of_strings)) {
            if (number_of_strings > 1) {
                is_valid_scale = true;
            }
        }
    } else {
        //must be standard scale and therefore does not need string total
        var scale_length = $("#scale_length").val();
        if(scale_length.match('^[0-9]*\.[0-9]*$')){
//        if( isInt(scale_length) ){
            is_valid_scale = true;
        }
    }
    return is_valid_scale;
}
function calculate(curr){
    var name = $("#string_set_name").val();
    var scale_length = $("#scale_length").val();

    if(name != '' && scale_length != '') {
//        var curr = this.id.substr(this.id.length - 1);

        var is_mscale = $("#mscale_checkbox").is(':checked');
        var number_of_strings = $("#number_of_strings").val();
        var desc = $("#desc").val();
        var string_number = $("#string_number_GTC_" + curr).val();
        var note = $("#note_GTC_" + curr).val();
        var octave = $("#octave_GTC_" + curr).val();
        var gauge = $("#gauge_GTC_" + curr).val();
        var string_type = $("#string_type_GTC_" + curr).val();

        var is_valid_scale =  check_valid_scale(is_mscale, number_of_strings);
        if (string_number != '' && note != '-'
            && octave != '-' && gauge != ''
            && string_type != '-' && name != ''
            && scale_length != '' && is_valid_scale)
        {
            ajaxCalculate(name, desc, is_mscale, scale_length, string_number, note,
                octave, gauge, string_type, number_of_strings, curr);
        }
    }
}

function validateScaleLength( scale_length){

    var is_mscale = $("#mscale_checkbox").is(':checked');
    var number_of_strings = $("#number_of_strings").val();
    var is_valid = true;
//    console.log("Scale Length keyup value: " + scale_length);
//    $.ajax({
//        type: "POST",
//        url: "/is-valid-scale-length/",
//        data: {
//            scale_length: scale_length,
//            is_mscale: is_mscale,
//            number_of_strings: number_of_strings
//        },
//        dataType: "json",
//        success: function (response) {
//           $("#scale_length").css("background-color", "#5cb85c");
//           calculate();
//        },
//        error: function (response, error) {
//            $("#scale_length").css("background-color", "#d2322d");
//        }
//    })
    return is_valid;
}

function validateGauge(gauge) {

    var is_valid = false;
    if( isFloat(gauge) ){
        if( 0 < gauge && gauge < 1){
            is_valid = true;
        }
    }
    return is_valid;
}

function validateStringNumber(string_number) {
    var is_valid = false;
    if(isInt(string_number)){
        if(string_number > 0){

            var is_mscale = $("#mscale_checkbox").is(':checked');
            if( is_mscale){
                var number_of_strings = $("#number_of_strings").val();
                if(isInt(number_of_strings)){
                    if(number_of_strings >= string_number){
                        is_valid = true;
                    }
                }
            }
            else{
                is_valid = true;
            }

        }
    }

    return is_valid
}

function validateNumberOfStrings(number_of_strings) {
    if( isInt(number_of_strings) )
        return true;
    return false;
}


function validateDropdown(dropdown_value) {
    if( dropdown_value != '-')
        return true;
    return false;
}


function colorValid(id, is_valid){
    if(is_valid){
        $(id).css("background-color", "#5cb85c");
    }else{
        $(id).css("background-color", "#d2322d");
    }
}

function isInt(input){
    var int_regex = /^\d+$/;
    if(int_regex.test(input))
        return true;
    else
        return false;
}

function isFloat(input){
    var float_regex = /^\s*(\+|-)?((\d+(\.\d+)?)|(\.\d+))\s*$/;
    if (float_regex.test(input))
        return true;
    else
        return false;
}