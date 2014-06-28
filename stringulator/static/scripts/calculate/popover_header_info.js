/**
 * Created by Micah on 2/20/14.
 */

    $(document).ready(function() {
//        $(".popover_header").hover(function() {
//            var id = $( this ).attr('id');
//            setPopover(id);
//        })

        $("#string_set_name").popover(
            { placement: "bottom", animation:"true",  trigger: "hover",
                title: "The Name of Your String Set",
                content: "A descriptive name that others can search by.\n Must be less than 30 characters."});

        $("#desc").popover({ placement: "bottom", animation:"true",  trigger: "hover",
            title: 'A Description of Your String Set',
            content: "Make notes on your thoughts on the set so others can learn from it. Must be less than 1000 characters. " +
                "This field is optional"});
        $("#mscale").popover({ placement: "bottom", animation:"true",  trigger: "hover",
            title: 'Set Calculator to Multi-Scale Mode',
            content: "By checking this, you must put the total number of strings and a value that is multi-scale for your set in the" +
                " appropriate boxes."});
        $("#number_of_strings_popover").popover({ placement: "bottom", animation:"true",  trigger: "hover",
            title: 'Determines the Width of the Fan',
            content: "This is only needed if you have a multi-scale instrument. Put the total number of strings on your guitar " +
                "Must be less than 100."});
        $("#scale_length_popover").popover({ placement: "bottom", animation:"true",  trigger: "hover",
            title: 'The Length of the Guitar From Neck to Bridge',
            content: "Assumes inches. Must be less than 100. If it is multi-scale it should follow the format '27-28.625'," +
                " where the lower value is first"});
        $("#number").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Strings Number',
            content: "Only affects calculation for multi-scale guitars, but is still required to keep the order of your strings." +
                " 1 is used for your highest string. 6 would be the low E on a standard tuned guitar. Must be less than 100 " +
                "and no more than the total number of strings if multi-scale is set."});
        $("#note").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Musical Note',
            content: "Assumes pitch standard note frequencies. Select from dropdown menu."});
        $("#octave").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Octave of the Note',
            content: "A guitars standard tuned octaves are: (high)e:4, B:3, G:3, D:3, A:2, (low)E:2. Select from dropdown menu."});
        $("#gauge").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Diameter of the String',
            content: "Must be less than 1 and no more than 5 decimal places."});
        $("#string-type").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Material the String Is Constructed From',
            content: "CK means Circle K strings. DA means D'Addario strings. " +
                "Select from dropdown menu."});
        $("#tension").popover({ placement: "top", animation:"true",  trigger: "hover",
            title: 'The Calculated Tension', content: "Experiment with what tension feels right to you. " +
                "Typically, you want all your strings to be as close to the same number as possible."});

    });


//function setPopover(id) {
//    var placement = "bottom";
//    var animation = "true";
//    var trigger = "hover";
//    var title = "title";
//    var content = "content";
//
//    if( id == "string_set_name"){
//
//    }else if(id == "desc" ){
//
//    }else if(id == "mscale" ){
//
//    }else if(id == "number_of_strings_popover" ){
//
//    }else if(id == "scale_length_popover" ){
//
//    }else if(id == "number" ){
//        placement = "top";
//    }else if(id == "note" ){
//        placement = "top";
//    }else if(id == "octave" ){
//        placement = "top";
//    }else if(id == "gauge" ){
//        placement = "top";
//    }else if(id == "string-type" ){
//        placement = "top";
//    }else if(id == "tension" ){
//        placement = "top";
//    }
//
//    $("#"+id).popover(
//                { placement: placement, animation:animation,  trigger: trigger,
//                    title: title,
//                    content: content});
//}
