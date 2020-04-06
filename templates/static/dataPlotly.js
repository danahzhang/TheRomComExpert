//Import the List
var nan = null;
var years = year_list;
var yList = y_list;
var yAll = yall_list;

//Plotly the Number of Movies Chart


var trace = {
    x: years,
    y: yList[0],
    type: "scatter",
    name: "Number of Films"
  };
  
  var data = [trace];
  
  var layout = {
    title: "Number of Films Per Year",
    xaxis: { title: "Year" },
    yaxis: { title: "Number of Films Released"},
    paper_bgcolor: 'rgb(233,233,233)',
    plot_bgcolor: 'rgb(233,233,233)',
    showlegend: true,

  };
  
  var config = {responsive: true}
  
Plotly.newPlot("count", data, layout, config, {scrollZoom: true});



//Creating a Box Office Box Chart
data = []
for( var i = 0; i < years.length;  i++ ){
  var result = {
    y: yAll[0][i],
    type:'box',
    name: (years[i]).toString(),

  };
  data.push(result);
};



var layout = {

  paper_bgcolor: 'rgb(233,233,233)',
  plot_bgcolor: 'rgb(233,233,233)',
  showlegend: true,
  title: "Box Office Per Year",
  xaxis: { title: "Year" },
  yaxis: { title: "Dollars Earned Domestically"}
};
var config = {responsive: true}


Plotly.newPlot('box', data, layout, config ,{scrollZoom: true});



//Create Rating Chart
var trace1 = {
    x: years,
    y: yList[2],
    type: "scatter",
    name: 'Rotten Tomatoes'
  };


var trace2 = {
  x: years,
  y: yList[3],
  type: "scatter",
  name: "imbdRatings"
};


var trace3 = {
    x: years,
    y: yList[4],
    type: "scatter",
    name: "MetaCritic Score"
  };

  var data = [trace1, trace2, trace3];
  
  var layout = {
    title: "Critical Acclaim Per Year",
    xaxis: { title: "Year" },
    yaxis: { title: "Ratings"},
    paper_bgcolor: 'rgb(233,233,233)',
    plot_bgcolor: 'rgb(233,233,233)',
    showlegend: true
  };
  var config = {responsive: true}
  Plotly.newPlot("rating", data, layout, config, {scrollZoom: true});

