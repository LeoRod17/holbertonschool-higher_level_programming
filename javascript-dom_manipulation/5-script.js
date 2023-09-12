doc = document.querySelector("#update_header");
function toadd(){
    document.querySelector("header").innerHTML = "New Header!!!";
}
doc.addEventListener("click", toadd);