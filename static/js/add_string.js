/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {

        //$("#string_row_GTC_0").show();
        var counter = 1;
        $(".addstring_btn").click(function() {
            var row = "#string_row"+counter
            $(row).show("slide")
            counter += 1;
        })

        $(".remove_btn").click(function() {
            console.log('hi')
            var curr = this.id.substr(this.id.length - 1)
            $("#string_row_GTC_"+curr).toggle();
        })

        $(".row_input").on("change", calculate)

        $(".user_input").keyup(validateScaleLength)

    });


function calculate(){
    console.log("in calculate")
    var name = $("#string_set_name").val();
    var scale_length = $("#scale_length").val();
    var rows = $('tr')

    console.log("name: "+name)
    console.log("scale_length: "+scale_length)
    if(name != '' && scale_length != ''){
        var number_of_strings = 0;
            console.log("Number of rows: " + rows.length);
        for(var i=0; i<rows.length; ++i){
            if($(rows[i]).css("display")=='table-row'){
                number_of_strings++;
            }
        }
        number_of_strings = number_of_strings-1; // offset due to header table row

        var curr = this.id.substr(this.id.length - 1);
        var string_number = $("#string_number_GTC_"+curr).val();
        var note = $("#note_GTC_"+curr).val();
        var octave = $("#octave_GTC_"+curr).val();
        var gauge = $("#gauge_GTC_"+curr).val();
        var string_type = $("#string_type_GTC_"+curr).val();

        console.log("number: "+string_number)
        console.log("note: "+note)
        console.log("gauge: "+gauge)
        console.log("type: "+string_type)
        console.log("name: "+name)
        console.log("length: "+scale_length)


        if(string_number != '' && note != '-'
            && octave != '-' && gauge != ''
            && string_type != '-' && name != ''
            && scale_length != ''){
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
                success: function(response){
                    console.log(response);
                    $('#tension_GTC_'+curr).text(response.tension);
                },
                error: function(response, error){
                    alert("ERROR!");
                   }
            })

        }
    }
}

function validateScaleLength(){
    var scale_length = $("#scale_length").val();
    console.log("Scale Length onChange value: " + scale_length);
    $.ajax({
        type: "POST",
        url: "/is-valid-scale-length/",
        data: {
            scale_length: scale_length
        },
        dataType: "json",
        success: function (response) {
            console.log(response);
            $("#scale_length").css("background-color", "Green");
        },
        error: function (response, error) {
            $("#scale_length").css("background-color", "Red");
        }
    })

}

