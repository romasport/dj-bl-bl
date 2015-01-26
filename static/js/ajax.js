function perl_plus(id){
    $.ajax({
        url: "/perl/plus/",
        type: "POST",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        dataType: "html",
        success: function(msg){
            $('#count-plus-'+id).text(parseInt($('#count-plus-'+id).text())+1);
        },
        error: function(msg){
            $('#mmes').html(
                '<div class="message error" style="display:block">'+
                '<div class="mmes-close" onclick="closemmes()">×</div>'+
                '<div class="mmes-test">'+
                    msg.responseText+
                '</div>'+
                '</div>'
            );
            setTimeout('closemmes()', 1000);
        }
    })
}

function perl_minus(id){
    $.ajax({
        url: "/perl/plus/",
        type: "POST",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        dataType: "html",
        success: function(msg){
            $('#count-minus-'+id).text(parseInt($('#count-minus-'+id).text())+1);
        },
        error: function(msg){
            $('#mmes').html(
                '<div class="message error" style="display:block">'+
                '<div class="mmes-close" onclick="closemmes()">×</div>'+
                '<div class="mmes-test">'+
                    msg.responseText+
                '</div>'+
                '</div>'
            );
            setTimeout('closemmes()', 1000);
        }
    })
}

function comment_minus(id){
    $.ajax({
        url: "/perl/comment_minus/",
        type: "POST",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        dataType: "html",
        success: function(msg){
            $('#comments_reyting-'+id).text(parseInt($('#comments_reyting-'+id).text())-1);
        },
        error: function(msg){
            $('#mmes').html(
                '<div class="message error" style="display:block">'+
                '<div class="mmes-close" onclick="closemmes()">×</div>'+
                '<div class="mmes-test">'+
                    msg.responseText+
                '</div>'+
                '</div>'
            );
            setTimeout('closemmes()', 1000);
        }
    })
}

function comment_plus(id){
    $.ajax({
        url: "/perl/comment_plus/",
        type: "POST",
        data: {
            'id': id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        dataType: "html",
        success: function(msg){
            $('#comments_reyting-'+id).text(parseInt($('#comments_reyting-'+id).text())+1);
        },
        error: function(msg){
            $('#mmes').html(
                '<div class="message error" style="display:block">'+
                '<div class="mmes-close" onclick="closemmes()">×</div>'+
                '<div class="mmes-test">'+
                    msg.responseText+
                '</div>'+
                '</div>'
            );
            setTimeout('closemmes()', 1000);
        }
    })
}