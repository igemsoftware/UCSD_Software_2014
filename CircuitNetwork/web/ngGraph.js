
//preparing the Angular Application
var graphApp = angular.module('graphApp',[]);
//setting default proportonality constants for Diff EQ's
var k = [1,1];
//User-adjusted proportionality constants.
var newK;
//default svg line in y=mx+b format.
var eqnDefault = function(i){
        return k[0]*i + k[1];
};
var equation = eqnDefault;

//Where we receive the equation
//Temporarily set to y=(m1)x+(b1).
var eqnNew = function(i){
        return newK.k1*i+newK.k2;
    };

//Counter for line ID's
var counter = 0;

//defining the size of the graph.
var m = [80,80,80,80]; //margins top,left,bottom,left
var h = 500 - m[0] - m [2]; //height
var w = 500 - m[1] - m[3]; //width

//Variables for the points
var domain = 100; //sample domain needs to be bound to data from Ryan's modeling
var eqnDomain = [];//An array of the desired domain.
var range = []; //range computed from domain.
var points =[]; //the points used by d3.js
var rangeMax; //maximum range

//Proportionality Constant Angular Controller
graphApp.controller('KCtrl',function($scope){
    $scope.constants = ["k1", "k2"];
    $scope.default = {
        //setting prop. constants to default values
        constants: {
            "k1": k[0],
            "k2": k[1]
        }
    };
    //Button method that updates the "K" values
    $scope.collectData = function (){
        newK = $scope.default.constants;
        console.log(newK);
        //Function that appends an SVG element with the new "K" values.
        //Located on line ~160. Continues to create duplicate lines.
        newLine(domain);
        removeLine();
    };
});

//Creating the d3.js controlled SVG graph.
//creating an array for the listed domain.
var domainSet = function(time){
    for(i = 0; i <= time; i++){
        eqnDomain.push(i);
    };
};
//hard coding a sample domain.
domainSet(domain);

var rangeSet = function(time) {
    for (i = 0; i <= d3.max(time); i++){
        var y = equation(i);
        range.push(y);
    };
};
//Preparing y-component of points
rangeSet(eqnDomain);
rangeMax = d3.max(range);

//Setting eqnDomain and range to points
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
//Setting points.
pointsSet(eqnDomain,range);

//setting up the function for the line.
var line = d3.svg.line()
        .x(function(d) { 
            //console.log("plotting x-value:" + d[0]);
            return xScale(d[0]); 
        })
        .y(function(d){
            //console.log("plotting x-value:" + d[1])
           return yScale(d[1]);
        });

//determing the scale of the axes lines.
var xScale = d3.scale.linear().domain([0,domain]).range([0,w]);
var yScale = d3.scale.linear().domain([0,rangeMax]).range([h,0]);

function make_x_axis() {        
    return d3.svg.axis()
        .scale(xScale)
         .orient("bottom")
         .ticks(10);
}

function make_y_axis() {        
    return d3.svg.axis()
        .scale(yScale)
        .orient("left")
        .ticks(10);
}
//create the SVG containter
var plot = d3.select("#graph").append("svg:svg")
        .attr("height", h + m[0] +m[2])
        .attr("width", w + m[1] + m[3])
    .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

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

    //create left y-axis
    var yAxisMain = d3.svg.axis().scale(yScale).ticks(10).orient("left");
    // Add the main y-axis
    plot.append("svg:g")
            .attr("class", "main axis")
            //.attr("transform", "translate(0," + h + ")")
            .call(yAxisMain);

    //create bottom x-axis
    var xAxisMain = d3.svg.axis().scale(xScale);
    // Add the main x-axis
    plot.append("svg:g")
            .attr("class", "main axis")
            .attr("transform", "translate(0," + h + ")")
            .call(xAxisMain);
    
    //Adding X-axis label
    plot.append("text")
    .attr("class", "label")
    .attr("x", w/2)
    .attr("y", h + 50 )
    .style("text-anchor", "middle")
    .text("Time");
    
    //Adding Y-axis lavel
    plot.append("text")
    .attr("class", "label")
    .attr("x", -(w/2))
    .attr("y", -50)
    .attr("dy", ".1em")
    .attr("transform", "rotate(-90)")
    .style("text-anchor", "middle")
    .text("Concentration");
    
    // Adding the line to the graph.
    plot.append("svg:path").attr("id","counter" + String(counter)).attr("d", line(points));

//Function to add a button to remove lines. 
var removeLine = function(){    
    var currentCount = counter;
    var removeBttn = '<button id="bttn' + String(currentCount) + '">X</button>';
    $("#legend").append('<p id="line' + String(currentCount)+ '">Line ' + String(currentCount) + '</p>');
    $("#legend").append(removeBttn);
    $("#bttn" + String(currentCount)).on("click", function(){        
        d3.select("#counter" + String(currentCount)).remove();
        d3.select("#line" + String(currentCount)).remove();
        d3.select("#bttn" + String(currentCount)).remove();
    });
};
    removeLine();

var newLine = function(newDomain){
    //clearing the arrays of old data.
    equation = eqnNew;
    eqnDomain = [];
    range = [];
    points = [];
    
    //Calling functions to reset arrays to new data.
    domainSet(newDomain);
    rangeSet(eqnDomain);
    rangeMax = d3.max(range);
    pointsSet(eqnDomain,range);
    counter += 1;
    plot.append("svg:path").attr("id","counter" + String(counter)).attr("d", line(points));
};