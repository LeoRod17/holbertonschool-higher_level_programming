doc = document.querySelector("#add_item");
function toadd(){
    document.querySelector(".my_list").innerHTML += "<li>Item</li>";
}
doc.addEventListener("click", toadd);