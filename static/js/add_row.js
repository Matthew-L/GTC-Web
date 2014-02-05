    function resetBackgroundColor(){
        var currentRow = numberOfRows - 1
//            $('#string_number_GTC_' + currentRow).css("background-color", "White");
//            $('#note_GTC_' + currentRow).css("background-color", "White");
//            $('#scale_length_GTC_' + currentRow).css("background-color", "White");
//            $('#gauge_GTC_' + currentRow).css("background-color", "White");
//            $('#octave_GTC_' + currentRow).css("background-color", "White");
//            $('#string_set_GTC_' + currentRow).css("background-color", "White");
//            $('#string_type_GTC_' + currentRow).css("background-color", "White");
    }



    /**
     * Deletes a row when the correct column is clicked on
     * Checks if the row is the last one, if so another is inserted before so that
     * the table is never empty
     * @param row:
     */
    function delete_user(row) {
        if (confirm('Are you sure you want delete this entire string?')) {

        var rowCount = $('table#strings-tbl tr:last').index() + 1;
//            console.log("Row Count:" + rowCount)
        if (rowCount == 2) {
            newRow()

        }

        $(row).closest('tr')
                .children('td')
                .animate({ padding: 0 })
                .wrapInner('<div />')
                .children()
                .slideUp(function () {
                    row.closest('tr').remove();
                });
              // Save it!
        } else {
            // Do nothing!
        }
    }
function newRow(){
        $("#strings-tbl").each(function () {
            var tds = '<tr>';
            jQuery.each($('tr:last td', this), function () {
                tds += '<td>' + returnValidRow($(this).html(), numberOfRows) + '</td>';
            });

            tds += '</tr>';
            if ($('tbody', this).length > 0) {
                $('tbody', this).append(tds);
            } else {
                $(this).append(tds);
            }
            numberOfRows += 1;
        });
    }

    function returnValidRow(currentRow, rowNumber){
        if(currentRow == '<a class="delete btn btn-danger" onclick="delete_user($(this))"><span class="glyphicon glyphicon-trash"></span></a>')
            return currentRow
        var id_tag = "_GTC_";
        if(currentRow.indexOf(id_tag) !== -1){
            var tagIndex = currentRow.indexOf(id_tag);

            var frontSubstring = currentRow.substr(0,tagIndex);

            var quoteIndex = currentRow.indexOf('"');
            var idSubstring = currentRow.substr(0, quoteIndex + 1);
            var idNameIndex = frontSubstring.indexOf(idSubstring);
            var idName = frontSubstring.replace(idSubstring, "")
            var idName = idName + id_tag + rowNumber;
            var htmlNameTag = 'name="' + idName + '"';
            var backSubstring = currentRow.substr(tagIndex);

            while(backSubstring.charAt(0) != "\""){
                backSubstring = currentRow.substr(tagIndex);
                tagIndex += 1
            }

            var tension = '<div id="tension'

            if(frontSubstring === tension){
                return '<div id="tension_GTC_'+rowNumber+'"' + htmlNameTag + '> - </div>'

                return '<div id="tension_GTC_'+rowNumber+'"' + htmlNameTag + '>tension goes here</div>'
            }

            backSubstring = currentRow.substr(tagIndex );
            var validRow = frontSubstring + id_tag + rowNumber + "\"" +  htmlNameTag + backSubstring
            return validRow
        }
    }



