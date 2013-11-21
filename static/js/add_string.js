/**
 * Created by Micah on 11/19/13.
 */

    $(document).ready(function() {
        $("#string_row0").nextAll().hide();
        var counter = 1;
        $(".addstring_btn").click(function() {
            $("#string_row"+counter).slideToggle("slow")
            counter += 1;
        })
    });

