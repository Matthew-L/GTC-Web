/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {

        $("#string_row0").show();
        var counter = 1;
        $(".addstring_btn").click(function() {
            var row = "#string_row"+counter
            $(row).show("slide")
//            alert($(row).load( "../templates/includes/forms.html" ));
            counter += 1;
        })

        $(".remove_btn").click(function() {
            console.log('hi')
            var curr = this.id.substr(this.id.length - 1)
            $("#string_row"+curr).toggle();
//            alert("#string_row"+curr.substr(curr.length - 1))
//            counter -= 1;
//            $("#string_row"+id_num).toggle("slide")
        })

        $(".row_input").on("change", calculate)
    });


function calculate(){
    var name = $("#string_set_name").val();
    var scale_length = $("#scale_length").val();
    var rows = $('tr')
//    alert("here")
    if(name != '' && scale_length != ''){
        var number_of_strings = 0;
            console.log(rows.length);
        for(var i=0; i<rows.length; ++i){
            if($(rows[i]).css("display")=='table-row'){
                number_of_strings++;
            }
        }
        number_of_strings = number_of_strings-1; // offset due to header table row

        var curr = this.id.substr(this.id.length - 1);
        var string_number = $("#string_number"+curr).val();
        var note = $("#note"+curr).val();
        var octave = $("#octave"+curr).val();
        var gauge = $("#gauge"+curr).val();
        var string_type = $("#string_type"+curr).val();

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
//                    alert(response.tension)
                    $('#tension'+curr).text(response.tension);
//                    $("#editor").hide()
//                    $("#save").hide();
//                    $("#cancel").hide();
//
//                    response_text = response.message;
//                    $("#text").text(response_text);
//                    $("#text").show();
                },
                error: function(response, error){
                    alert("ERROR!");
                   }
            })

        }
    }
}
