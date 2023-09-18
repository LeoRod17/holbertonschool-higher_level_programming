window.onload = function () {
    $("#btn_translate").click(function () {
        $.get("https://www.fourtonfish.com/hellosalut/?" + $("#language_code").val(), function (data) {
            $("#hello").text(data)
        })
    })
};