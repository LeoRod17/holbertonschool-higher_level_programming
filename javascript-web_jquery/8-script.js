$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (title) {
    sw = title["results"]
    for (x in sw) {
        $("#list_movies").append(`<li>${sw[x]["title"]}</li>`);
    }
});