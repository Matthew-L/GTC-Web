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
            var curr = this.id
            $("#string_row"+curr.substr(curr.length - 1)).toggle();
//            alert("#string_row"+curr.substr(curr.length - 1))
//            counter -= 1;
//            $("#string_row"+id_num).toggle("slide")
        })
    });


