doc = document.querySelector("#toggle_header");
function tochange(){
    doc2 = document.querySelector("header");
    if (doc2.classList == "red")
    {
        doc2.classList = "green";
    }
    else
    {
        doc2.classList = "red";
    }

}

doc.addEventListener("click", tochange);