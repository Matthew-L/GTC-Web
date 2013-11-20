/**
 * Created by Micah on 11/19/13.
 */

//
$(document).ready(function() {
//    $(".addstring_btn").click(function() {
////          {% csrf_token %} \
////                {% for field in form %} \
////                    <td>{{ field }}</td> \
////                {% endfor %} \
//
////"<tr> \
////            <form method='post' action='.'> \
////                <td> \
////                    <input type='submit' value='Calculate'> \
////                </td> \
//
////                       <td> \
////                    <button type='button' class='addstring_btn'>Add String</button> \
////                </td> \
////            </form> \
////        </tr>"
//
//       $('#strings-tbl tr:last').after("{% for field in form %} <td>{% verbatim %}{{ field }}{% endverbatim %}</td> {% endfor %}");
//    });


function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}
});