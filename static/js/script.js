$(document).ready(function() {

    //активный пункт меню
    var link = window.location.pathname;
    $('#menu li a[href="'+link+'"]').parent().addClass('active');

    $("#close").click(function(){
        $(".modul").css('display','none')
    });

});

function modvhod() {
    $("#vhod").css('display','block');
}

function modreg() {
    $("#registr").css('display','block');
}

function closemmes() {
    $(".mmes .message").fadeOut(400);
}
