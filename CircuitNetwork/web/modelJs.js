/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*Guide:
 * -Declaring global variables
 * -Angular App
 * -Functions for Data collection and graph points
 * -Graph functions
 * -Line editing functions
 */

//***Global variables***
var circuitData = {};

var k = [1,1];
var OpticalDensity;
var Input1;
var Input2;
var Input3;

/**
 * @type type variable
 * List of dictionairies of modeling equations
 */
//To change an input's name, equation.value[index].name("newName").
//To change an input's value, equation.value[index].value(newNumber).
var eqnDef = {
    values: [
        {"name": "m", "value": k[0]},
        {"name": "b", "value": k[1]}
    ], 
    equation: function(i){
                return eqnDef.values[0].value*i + eqnDef.values[1].value;
    },
    eqnText: "y = mx + b"
};

var eqnOD = {
    inputs: ["Optical Density","Input 1"],
    values: [
        {"name": "Optical Density", "value" :OpticalDensity},
        {"name": "Input 1", "value": Input1}
    ],
    equation: function (OD, k1, i){
        OpticalDensity = OD;
        Input1 = k1;

        return OD + 0.1*OpticalDensity*(1-k1*OpticalDensity)*0.1;
    },
    eqnText: "(dOD/dt) = 0.1*OpticalDensity*(1-k1*OpticalDensity)"
};

/**
 * 
 * @type {{name: string}} eqnDict - Dictionary of all stored equations.
 */
//Dictionary of equation dictionaries for easy reference by JSON string.
var eqnDict = {
    "eqnDef":eqnDef, 
    "eqnOD":eqnOD
};

//preparing the Angular Application
var graphApp = angular.module('graphApp',[]);

//counting variables
var graphCount = 0;
var lineCount = 0;

//defining the size of the graph.
var m = [80,80,80,80]; //margins top,left,bottom,left
var h = 500 - m[0] - m [2]; //height
var w = 500 - m[1] - m[3]; //width

//Graphed line variables
var equation = eqnDict.eqnDef; //holds the current equation being used

var time = 100; //sample domain needs to be bound to data from Ryan's modeling
var timestep = 1; //sample timestep for iteration through time.
var domain = [];//An array of the desired domain.
var range = []; //range computed from domain.
var points =[]; //the points used by d3.js
var rangeMax; //maximum range

//SVG container.
var plot;

/**
 * Angular Controller that manages user input of equation variables
 * to dynamically rerender graph.
 * 
 * @param {string} 'KCtrl' - Name of the controller.
 * @param {variable} $scope - angular.js's scope object.
 */
graphApp.controller('KCtrl',function($scope){
    
    $scope.constants = equation.values;
    
    $scope.collectData = function (){
        console.log($scope.constants);
    };    
}); //end of KCtrl.

//determing the scale of the axes lines.
var xScale = d3.scale.linear().domain([0,time]).range([0,w]);
var yScale = d3.scale.linear().domain([0,100]).range([h,0]);

//d3.js reference for creating path objects.
var line = d3.svg.line()
    .x(function(d) { 
        //console.log("plotting x-value:" + d[0]);
        return xScale(d[0]); 
    })
    .y(function(d){
        //console.log("plotting x-value:" + d[1])
       return yScale(d[1]);
    });

//Orients lines to be drawn horizontally.
function make_x_axis() {        
    return d3.svg.axis()
        .scale(xScale)
         .orient("bottom")
         .ticks(10);
};

//Orients lines to be drawn horizontally.
function make_y_axis() {        
    return d3.svg.axis()
        .scale(yScale)
        .orient("left")
        .ticks(10);
};

//Changes plot varaiable's selector to the current graph being drawn.
function setPlot(newGraph){
    var graphNumber = newGraph;
    plot = d3.select("#graph" + String(graphNumber)).append("svg:svg")
        .attr("height", h + m[0] +m[2])
        .attr("width", w + m[1] + m[3])
    .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");
};

//Draws the grid and axis of a graph.
var drawGraph = function(){
    //adding x-grid
    plot.append("g")         
        .attr("class", "grid")
        .attr("transform", "translate(0," + h + ")")
        .call(make_x_axis()
            .tickSize(-h, 0, 0)
            .tickFormat("")
        );

    //adding y-grid
    plot.append("g")         
        .attr("class", "grid")
        .call(make_y_axis()
            .tickSize(-w, 0, 0)
            .tickFormat("")
        );

    // Add the main y-axis
    plot.append("svg:g")
            .attr("class", "main axis")
            //.attr("transform", "translate(0," + h + ")")
            .call(make_y_axis());

    // Add the main x-axis
    plot.append("svg:g")
            .attr("class", "main axis")
            .attr("transform", "translate(0," + h + ")")
            .call(make_x_axis());

    //Adding X-axis label
    plot.append("text")
        .attr("class", "label")
        .attr("x", w/2)
        .attr("y", h + 50 )
        .style("text-anchor", "middle")
        .text("Time");

    //Adding Y-axis label
    plot.append("text")
        .attr("class", "label")
        .attr("x", -(w/2))
        .attr("y", -50)
        .attr("dy", ".1em")
        .attr("transform", "rotate(-90)")
        .style("text-anchor", "middle")
        .text("Concentration");

    console.log("Empty graph drawn...");
}; //end of drawGraph.

function graphDivAppend(graphNumber) {
    var divString = '<div class="graph" id="graph' + String(graphNumber) + '"></div>';
    $("#graphContainter").append(divString);

    console.log("New graph div appended...");
};

function domainSet(time,step) {
    for(atime = 0; atime < time + step; atime+= step){
    domain.push(atime);
    };
};

var rangeSet = function(time) {
for (i = 0; i <= d3.max(time); i++){
    var y = equation.equation(i);
    range.push(y);
    };
};

var pointsSet = function(input,output){
    for (i = 0; i <= d3.max(input); i++){
        //Setting up entry into the points array.
        var point = [];
        //Assigning x-value of point "i"
        point.push(input[i]);
        //Assigning y-value of point "i"
        point.push(output[i]);
        //Adding point to array of points.
        points.push(point);
    };
};

var removeLine = function(){
    var currentGraph = graphCount;
    var currentLine = lineCount;
    var removeBttn = '<button id="bttn' + String(currentLine) + '">X</button>';
    $("#legend").append('<p id="line_legend' + String(currentLine)+ '">Line ' + String(currentLine) + '</p>');
    $("#legend").append(removeBttn);
    $("#bttn" + String(currentLine)).on("click", function(){        
        d3.selectAll(".line" + String(currentLine)).remove();
        d3.select("#line_legend" + String(currentLine)).remove();
        d3.select("#bttn" + String(currentLine)).remove();
    });
};

var newLine = function(currentEqn,time,step){
    //clearing the arrays of old data.
    equation = currentEqn;
    domain = [];
    range = [];
    points = [];

    //Calling functions to reset arrays to new data.
    domainSet(time,step);
    rangeSet(domain);
    rangeMax = d3.max(range);
    pointsSet(domain,range);
    lineCount += 1;
    plot.append("svg:path").attr("class","line" + String(lineCount)).attr("d", line(points));
};

//***WIP function for constructing graph and plotting data.
function eqnGraph(graphNumber,currentEqn,time,step) {
    console.log("Starting equation graphing...");

    //Draws current eqn's graph and creates containing div.
    //Appends Div to container for new graph.
    graphDivAppend(graphNumber);
    //Sets plot variable to point towards new graph
    setPlot(graphNumber);
    //Draws empty graph in new div.
    drawGraph();

    //Calculates points and graphs line.
    newLine(currentEqn,time,step);

    graphCount += 1;
    console.log("Equation and graph render complete.");
}; //end of eqnGraph.

function eqnDataGET() {
    console.log("*****");
    console.log("Beginning circuit graph...");
    console.log("*****");
    console.log("");
    //Receives order of circuit JSON from GET request.
    //Temp setting of hard-coded data.
    var data = '{ "data": [ { "equation":"eqnDef", "values": [1,0], "domain": [100,1] }, { "equation":"eqnDef", "values": [-1,100], "domain": [100,1] } ] }';
    
    circuitData = JSON.parse(data).data; 
//    [
//        {
//            "equation":"eqnDef",
//            "values": [1,0],
//            "domain": [100,1]
//        },
//        {
//            "equation":"eqnDef",
//            "values": [-1,100],
//            "domain": [100,1]
//        }
//    ];
    
    for (var counter = 0; counter <= circuitData.length - 1; counter ++) {
        console.log("*****");
        console.log("Graphing equation #" + String(counter) + " of circutit.");
        console.log("---");
        
        graphCount = counter;
        equation = eqnDict[circuitData[counter].equation];
        for (var index = 0; index <= equation.values.length - 1; index += 1) {
            equation.values[index].value = circuitData[counter].values[index];
        };
        time = circuitData[counter].domain[0];
        timestep = circuitData[counter].domain[1];

        //Resets lineCount for new graph.
        lineCount = 0;
        eqnGraph(graphCount,equation,time,timestep);
        
        console.log("Graph#" + String(graphCount - 1) + " drawn.");
        console.log("*****");
        console.log("");
    };
    //Adds button to remove all lines of a circuit's current iteration.
    removeLine();
    console.log("*****");
    console.log("Circuit graph complete.");
    console.log("*****");
    
};

eqnDataGET();