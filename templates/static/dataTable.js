//Import and Parse Json File
var urls = random;
var urls = JSON.stringify(urls);
var urls = JSON.parse(urls);

//Create RomCom Movie Info Table
var romcomHead = '<thead><tr><th scope="col">Title</th><th scope="col">Release Date</th><th scope="col">Director</th><th scope="col">Runtime</th><th scope="col">Plot</th></tr></thead>';

////Generate a Random Integer
function randomInteger(max) {
    min = Math.ceil(0);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max + 1));
  }
aNumber = randomInteger(urls.url.length)

var romcomTable = "";
for (var i = aNumber; i < aNumber+100; i++) {

    $.getJSON(urls.url[i], function theTable(data) {
        var movie_data = '';
        movie_data += '<tr class="table-active">';
        movie_data += '<td>'+data.Title+'</td>';
        movie_data += '<td>'+data.Released+'</td>';
        movie_data += '<td>'+data.Director+'</td>';
        movie_data += '<td>'+data.Runtime+'</td>';
        movie_data += '<td>'+data.Plot+'</td>';
        movie_data += '</tr>';
        romcomTable += movie_data;

    });

};

function createTable(){
    document.getElementById('pickData').innerHTML = romcomTable;
    document.getElementById('pickHead').innerHTML = romcomHead;
};

//Create RomCom Project Data Table
var romcomHeadData = '<thead><tr><th scope="col">Title</th><th scope="col">Year</th><th scope="col">imdb ID</th><th scope="col">imdb Score</th><th scope="col">MetaCritic Score</th><th scope="col">Box Office</th></tr></thead>';

var romcomTableData = "";
for (var i = 0; i < (urls.url.length); i++) {

    $.getJSON(urls.url[i], function theTableData(data) {
        var movie_data = '';
        movie_data += '<tr class="table-active">';
        movie_data += '<td>'+data.Title+'</td>';
        movie_data += '<td>'+data.Year+'</td>';
        movie_data += '<td>'+data.imdbID+'</td>';
        movie_data += '<td>'+data.imdbRating+'</td>';
        movie_data += '<td>'+data.Metascore+'</td>';
        movie_data += '<td>'+data.BoxOffice+'</td>';
        movie_data += '</tr>';
        romcomTableData += movie_data;

    });

};
function createDataTable(){
    document.getElementById('pickData').innerHTML = romcomTableData;
    document.getElementById('pickHead').innerHTML = romcomHeadData;
};