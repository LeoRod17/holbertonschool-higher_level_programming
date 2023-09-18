window.onload = function () {
    $("#btn_translate").click(function () {
        $.get("https://hellosalut.stefanbohacek.dev/?lang=" + $("#language_code").val(), function (data) {
            $("#hello").text(data["hello"])
        })
    })
    $("#language_code").keypress(function(a){
        const key = a.which
        if (key === 13){
            $("#btn_translate").click()
        }  
    });
};