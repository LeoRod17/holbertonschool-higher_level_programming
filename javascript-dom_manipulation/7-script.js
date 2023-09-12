StarWars()
async function StarWars()
{
    const names = await (await fetch("https://swapi-api.hbtn.io/api/films/?format=json")).json();
    const sw = names["results"]
    for (i in sw)
    {
        document.querySelector("#list_movies").innerHTML += '<li>' + sw[i]["title"] + '</li>';
    }
}
