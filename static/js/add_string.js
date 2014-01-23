/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {
        addChangeEvent();
        calculateSet();
    });


function addChangeEvent() {
    //$("#string_row_GTC_0").show();

    $("#mscale_checkbox").click(function () {
        console.log('hi')
//        var curr = this.id.substr(this.id.length - 1)
        $(".hidden_row").slideToggle("slow");
    })

    var counter = 1;
    $(".addstring_btn").click(function () {
        var row = "#string_row" + counter
        $(row).show("slide")
        counter += 1;
    })

    $(".remove_btn").click(function () {
//        console.log('hi')
        var curr = this.id.substr(this.id.length - 1)
        $("#string_row_GTC_" + curr).toggle();
    })

    $(".row_input").on("change", calculate);

    $(".scale_length_input").keyup(validateScaleLength);
    $(".gauge_input").keyup(validateGauge);
    $(".string_number_input").keyup(validateStringNumber);
    $(".dropdown_input").on("change", validateDropdown);
    $(".string_set_name_input").keyup(validateStringSetName);

    last_row = $('#strings-tbl tr:last');
    last_row.css('display', 'none');
    last_row.insertAfter('#strings-tbl tr:last');
    last_row.fadeIn('slow');
}


function countValidRows() {
    var lastid = $('#strings-tbl tr:last-child').find("div").attr('id')
    var curr = lastid.substr(lastid.length - 1);
    return curr;
}

function ajaxCalculate(name, scale_length, string_number, note, octave, gauge, string_type, number_of_strings, curr) {
    $.ajax({
        type: "POST",
        url: "/ajax/",
        data: {
            string_set_name: name,
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
//            console.log(response.tension);

            $('#tension_GTC_' + curr).text(response.tension);
        },
        error: function (response, error) {
            alert("ERROR!");
        }
    })
}

function calculateSet(){
    var number_of_strings = countValidRows();
//    console.log("number_of_strings :" + number_of_strings);
    var curr;
    var name;
    var scale_length;
    var string_number;
    var note;
    var octave;
    var gauge;
    var string_type;

    for(curr = 0; curr < number_of_strings; ++curr){
//        name = $("#string_set_name").val();
//        scale_length = $("#scale_length").val();
//        string_number = $("#string_number_GTC_" + curr).val();
//        note = $("#note_GTC_" + curr).val();
//        octave = $("#octave_GTC_" + curr).val();
//        gauge = $("#gauge_GTC_" + curr).val();
//        string_type = $("#string_type_GTC_" + curr).val()
//
//        console.log("number: "+string_number)
//        console.log("note: "+note)
//        console.log("gauge: "+gauge)
//        console.log("type: "+string_type)
//        console.log("name: "+name)
//        console.log("length: "+scale_length)
//        if(string_number != '' && note != '-'
//            && octave != '-' && gauge != ''
//            && string_type != '-' && name != ''
//            && scale_length != ''){
//            ajaxCalculate(name, scale_length, string_number, note,
//                octave, gauge, string_type, number_of_strings, curr);
//        }
    }
}

function calculate(curr){
//    console.log("in calculate")
    var name = $("#string_set_name").val();
    var scale_length = $("#scale_length").val();

//    console.log("name: "+name)
//    console.log("scale_length: "+scale_length)
    if(name != '' && scale_length != ''){
        var number_of_strings = countValidRows()+1;

        var curr = this.id.substr(this.id.length - 1);
        var string_number = $("#string_number_GTC_"+curr).val();
        var note = $("#note_GTC_"+curr).val();
        var octave = $("#octave_GTC_"+curr).val();
        var gauge = $("#gauge_GTC_"+curr).val();
        var string_type = $("#string_type_GTC_"+curr).val();

//        console.log("number: "+string_number)
//        console.log("note: "+note)
//        console.log("gauge: "+gauge)
//        console.log("type: "+string_type)
//        console.log("name: "+name)
//        console.log("length: "+scale_length)


        if(string_number != '' && note != '-'
            && octave != '-' && gauge != ''
            && string_type != '-' && name != ''
            && scale_length != ''){
              ajaxCalculate(name, scale_length, string_number, note,
                octave, gauge, string_type, number_of_strings, curr);

        }
    }
}

function validateScaleLength(){
    var scale_length = $("#scale_length").val();
//    console.log("Scale Length keyup value: " + scale_length);
    $.ajax({
        type: "POST",
        url: "/is-valid-scale-length/",
        data: {
            scale_length: scale_length
        },
        dataType: "json",
        success: function (response) {
//            console.log(response);
           $("#scale_length").css("background-color", "#5cb85c");
        },
        error: function (response, error) {
            $("#scale_length").css("background-color", "#d2322d");
        }
    })
}

function validateGauge() {
    id = "#" + this.id
    var gauge_value = $(id).val();
//    console.log("Gauge keyup value: " + gauge_value);
    $.ajax({
        type: "POST",
        url: "/is-valid-gauge/",
        data: {
            gauge: gauge_value
        },
        dataType: "json",
        success: function (response) {
//            console.log(response);
            $(id).css("background-color", "#5cb85c");
            calculate();
        },
        error: function (response, error) {
            $(id).css("background-color", "#d2322d");
        }
    })
}

function validateStringNumber() {
    id = "#" + this.id
    var string_number_value = $(id).val();
//    console.log("StringNumber keyup value: " + string_number_value);
    $.ajax({
        type: "POST",
        url: "/is-valid-string-number/",
        data: {
            string_number: string_number_value
        },
        dataType: "json",
        success: function (response) {
//            console.log(response);
            $(id).css("background-color", "#5cb85c");
            calculate()
        },
        error: function (response, error) {
            $(id).css("background-color", "#d2322d");
        }
    })
}


function validateDropdown() {
    value_not_set = "-"
    id = "#" + this.id
    var dropdown_value = $(id).val();
//    console.log("Dropdown onChange: " + dropdown_value);
    if(dropdown_value == value_not_set){
        $(id).css("background-color", "#d2322d");
    }else{
        $(id).css("background-color", "#5cb85c");
        calculate()
    }
}

function validateStringSetName() {
    value_not_set = ""
    id = "#" + this.id
    var string_set_name = $(id).val();
//    console.log("Dropdown onChange: " + string_set_name);
    if (string_set_name == value_not_set) {
        $(id).css("background-color", "#d2322d");
    } else {
        $(id).css("background-color", "#5cb85c");
    }
}


