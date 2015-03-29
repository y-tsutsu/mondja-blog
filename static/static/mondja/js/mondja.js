$(window).on('load', function () {
    $('.selectpicker').selectpicker({
        size: 4,
        selectedText: 'cat'
    });
});

$(document).ready(function () {
    $('#toggle').click(function () {
        $('button').button('toggle');
    });
    $('#state').click(function () {
        alert($('button').hasClass('active') ? 'on' : 'off');
    });
});
