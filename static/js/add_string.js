/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {

        $("#string_row0").nextAll().hide();
        var counter = 0;
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
    if(name != '' && scale_length != ''){
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
                console.log("yeay");
        //$.ajax({
        //    type: "POST",
        //    url: "/ajax",
        //    data: {
        //        key: 1,
        //        text: new_text
        //    },
        //    dataType: "json",
        //    success: function(response){
        //        $("#editor").hide()
        //        $("#save").hide();
        //        $("#cancel").hide();
        //
        //        response_text = response.message;
        //        $("#text").text(response_text);
        //        $("#text").show();
        //    },
        //    error: function(response, error){
        //        alert("ERROR!");
        //       }
        //    })
        //}
        }
    }
}
