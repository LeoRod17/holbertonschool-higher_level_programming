doc = document.querySelector("#red_header");
function tochange(){
    doc.classList.add("red")
}

doc.addEventListener("click", tochange);