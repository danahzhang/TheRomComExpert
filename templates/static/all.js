//Import and Parse Json File
var urls = random;
var urls = JSON.stringify(urls);
var urls = JSON.parse(urls);

//Generate a Random Integer
function randomInteger(max) {
  min = Math.ceil(0);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max + 1));
}
aNumber = randomInteger(urls.url.length)

//Get a Random Movie Poster
$.getJSON(urls.url[aNumber], function theImage(data) {
  document.getElementById("randomPosterPic").src = data.Poster
  document.getElementById("randomPosterPic").alt = "There is no movie poster for " + data.Title + " but try the Click Me Tab on Top";
});

//Get the Link to its IMB page for the CLICK ME Button 
$.getJSON(urls.url[aNumber], function theClickMeURL(data) {
  var theUrlID = data.imdbID;
  var theUrl = "https://www.imdb.com/title/"+ theUrlID;
  document.getElementById("randomPosterUrl").href = theUrl;
});




