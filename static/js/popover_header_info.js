/**
 * Created by Micah on 2/20/14.
 */

    $(document).ready(function() {
        var id = $(".popover_header").attr('id')
        alert(id)
//        setPopover(id)
        $("#string_set_name").popover(
            { placement: "bottom", animation:"true",  trigger: "hover",
                title: 'Twitter Bootstrap Popover',
                content: "It's so simple to create a tooltop for my website!"});
        $("#desc").popover({ placement: "bottom", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#mscale").popover({ placement: "bottom", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#number_of_strings_popover").popover({ placement: "bottom", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#scale_length_popover").popover({ placement: "bottom", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#number").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#note").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#octave").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#gauge").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});
        $("#string-type").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});


        $("#tension").popover({ placement: "top", animation:"true",  trigger: "hover", title: 'Twitter Bootstrap Popover', content: "It's so simple to create a tooltop for my website!"});

    });


function setPopover(id) {
    var placement = "bottom";
    var animation = "true";
    var trigger = "hover";
    var title = "";
    var content = "";

    if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }else if( localeCompare(id, "") == 0 ){

    }

    $(id).popover(
                { placement: placement, animation:animation,  trigger: trigger,
                    title: title,
                    content: content});
}
