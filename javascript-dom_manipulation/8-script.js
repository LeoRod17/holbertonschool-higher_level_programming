StarWars()
async function StarWars()
{
const hell = await (await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")).json();
    document.querySelector("#hello").innerHTML = hell["hello"];
}
