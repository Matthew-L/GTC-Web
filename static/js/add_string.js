/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {
        addChangeEvent();
        validateAll();
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

    $(".dropdown_input").on("change", validateAll);
    $(".user_input").keyup(validateAll);
    $("#mscale_checkbox").click(validateAll);

    last_row = $('#strings-tbl tr:last');
    last_row.css('display', 'none');
    last_row.insertAfter('#strings-tbl tr:last');
    last_row.fadeIn('slow');
}

function validateAll(){
    var is_valid;
    var id = "#scale_length";
    var val = $(id).val();
    is_valid = validateScaleLength(val);
    colorValid(id, is_valid);

    id = "#number_of_strings";
    val = $(id).val();
    is_valid = validateNumberOfStrings(val);
    colorValid(id, is_valid);

    for (var i = 0; i <= countValidRows(); ++i) {
        if ($("#string_number_GTC_" + i).length) {//check if it exists
            id = "#string_number_GTC_"+i;
            val = $(id).val();
            is_valid = validateStringNumber(val);
            colorValid(id, is_valid);

            id = "#note_GTC_"+i;
            val = $(id).val();
            is_valid = validateDropdown(val);
            colorValid(id, is_valid);

            id = "#octave_GTC_"+i;
            val = $(id).val();
            is_valid = validateDropdown(val);
            colorValid(id, is_valid);

            id = "#gauge_GTC_"+i;
            val = $(id).val();
            is_valid = validateGauge(val);
            colorValid(id, is_valid);

            id = "#string_type_GTC_"+i;
            val = $(id).val();
            is_valid = validateDropdown(val);
            colorValid(id, is_valid);

        }
    }
    calculateAllRows()
}

function calculateAllRows() {

        for (var i = 0; i <= countValidRows(); ++i) {
            if ($("#string_number_GTC_" + i).length) {//check if it exists
                if(validateRow(i)){
                    var is_mscale = $("#mscale_checkbox").is(':checked');
                    var scale_length = $("#scale_length").val();
                    var number_of_strings = $("#number_of_strings").val();
                    var string_number = $("#string_number_GTC_" + i).val();
                    var note = $("#note_GTC_" + i).val();
                    var octave = $("#octave_GTC_" + i).val();
                    var gauge = $("#gauge_GTC_" + i).val();
                    var string_type = $("#string_type_GTC_" + i).val();
                    ajaxCalculate(is_mscale, scale_length, string_number, note, octave, gauge, string_type, number_of_strings, i);
                }

            }
        }

}

function countValidRows() {
    var lastid = $('#strings-tbl tr:last-child').find("div").attr('id')
    var curr = lastid.substr(lastid.length - 1);
    return curr;
}

function ajaxCalculate(is_mscale, scale_length, string_number, note, octave, gauge, string_type, number_of_strings, curr) {
    $.ajax({
        type: "POST",
        url: "/ajax/",
        data: {
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
            var tension = response.tension;
            if(tension < 0){
                tension = 0;
            }

            $('#tension_GTC_' + curr).text(tension);
        },
        error: function (response, error) {
            alert("ERROR!");
        }
    })
}

function validateRow(curr){

    var is_mscale = $("#mscale_checkbox").is(':checked');
    var scale_length = $("#scale_length").val();
    var number_of_strings = $("#number_of_strings").val();
    var string_number = $("#string_number_GTC_" + curr).val();
    var note = $("#note_GTC_" + curr).val();
    var octave = $("#octave_GTC_" + curr).val();
    var gauge = $("#gauge_GTC_" + curr).val();
    var string_type = $("#string_type_GTC_" + curr).val();

    if(is_mscale){
        if(validateScaleLength(scale_length) && validateStringNumber(string_number)
        && validateDropdown(note) && validateDropdown(octave) &&
            validateGauge(gauge) && validateDropdown(string_type) && validateNumberOfStrings(number_of_strings)
            )
        {
            return true;
        }
    }
    else{
        if(validateScaleLength(scale_length) && validateStringNumber(string_number)
        && validateDropdown(note) && validateDropdown(octave) &&
            validateGauge(gauge) && validateDropdown(string_type)
            )
        {
            return true;
        }

    }

    return false;
}

function validateScaleLength( scale_length){

    var is_mscale = $("#mscale_checkbox").is(':checked');
    var is_valid = false;

    if (is_mscale) {
        var arr;
        arr = scale_length.split("-", 2)
        if(scale_length == arr[0]+"-"+arr[1]){
            if( isFloat(arr[0]) && isFloat(arr[1]) ){
                is_valid = true;
            }
        }
    }else {
        if(isFloat(scale_length)){
            is_valid = true;
        }
    }
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
                    if(parseInt(number_of_strings) >= parseInt(string_number)){
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