/**
 * Created by Micah on 1/22/14.
 */
$(document).ready(function() {
    console.log("delete")
    $(".delete-set-btn").click(function () {

        if(confirm('Are you sure you want delete this entire set?')){

            var name = this.id.substring(4)
            var num = $(this).attr("num")
            ajaxDelete(name);
            $("#row-"+num).slideUp();
        }
    });
});

function ajaxDelete(name) {
    $.ajax({
        type: "POST",
        url: "/ajax-delete/",
        data: {
            string_set_name: name
        },
        dataType: "json",
        success: function (response) {

        },
        error: function (response, error) {
            alert("ERROR!");
        }
    })
}
