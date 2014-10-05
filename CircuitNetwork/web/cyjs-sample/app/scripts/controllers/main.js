
angular.module('cyViewerApp')
	
    .controller('MainCtrl', function ($scope, $http, $location, $routeParams, 
$window, Network, VisualStyles, Gist) {		

        'use strict';     
        //these files are the temporary network
	var NETWORK_FILE = 'data/sbider_whole_network.json'; 
        var visualStyleFile = 'data/sbiderStyle.json'; 
        var DEFAULT_VISUAL_STYLE_NAME = 'default';//'Solid';
        var PRESET_STYLE_FILE = encodeURIComponent('data/sbiderStyle.json');
        
        //temp user declaration
        //generates a random string of 20 characters
        var userID = "carlo";

        //these empty dictionaries are updated by the server for use by the cytoscape.js object.
        var networkData = {};
        var networkDefault = {};
	var vs = {};
        //global reference for cytoscape.js
        $scope.cynet;
        //Global variables for storing algorithm results
        //currently hard coded from dummy data
        var speciesId = [["spe_11"],["ope_2-1","ope_46-1","ope_47-1","ope_57-1","spe_13","spe_2","spe_33","spe_9"],["ope_1-1","spe_20","spe_21"],["spe_39"]];
        var transitionId = [["ot_1","ot_2"],["it_2","it_3","it_72","it_75","it_98","ot_98"],["it_1","ot_72","ot_75"],["ot_3","ot_5"]];
        var edgeId = [["54","69"],["55","56","57","58","65","66","67","68","71","72","73","76","77","78","80","81","82","83","85"],["50","51","52","53","74","79"],["59","64"]];
       
        $scope.networks = {};
        $scope.visualStyles = {};
        $scope.styleNames = [];
        $scope.networkNames = [];
        $scope.currentVS = DEFAULT_VISUAL_STYLE_NAME;
        //$scope.currentNetworkData = null;
        
        var gistStyle = null;

        // Parse url parameters
        var gistId = $routeParams.id;
        var zoomLevel = $routeParams.zoom;
        var panX = $routeParams.x;
        var panY = $routeParams.y;

        // Application global objects
        $scope.networks = {};
        $scope.visualStyles = {};
        $scope.styleNames = [];
        $scope.networkNames = [];
        $scope.currentVS = DEFAULT_VISUAL_STYLE_NAME;
        $scope.currentNetworkData = null;

        //Toolbar state variables
        $scope.browserState = {
            show: false
        };
        $scope.overlayState = {
            show: true
        };
        $scope.toolbarState = {
            show: true
        };
        $scope.searchState = {
            show: true
        };
        $scope.cadState = {
            show: false
        };
        $scope.modelState = {
            show: false
        };

        $scope.bg = {
            color: '#FAFAFA'
        };

        $scope.columnNames = [];
        $scope.edgeColumnNames = [];
        $scope.networkColumnNames = [];

        var originalLocation = $location.absUrl().split('?')[0];

        console.log('GistID: ' + gistId);
        console.log('Network rendering start...');
        
         /** EVIL CODE: do NOT uncomment. This KILLS the graph. :( Took me 3 hours to get this bug...hmpf**/
	var styleLocation = $scope.encodedStyle;
        if (!styleLocation) {
            visualStyleFile = PRESET_STYLE_FILE;
        } else {
            visualStyleFile = $scope.encodedStyle;
        }
        
        var options = {
            showOverlay: false,
            minZoom: 0.01,
            maxZoom: 200,

            layout: {
                name: 'preset'
            },
	    
	    //style: cytoscape.stylesheet()
	    //Changing shapes of nodes 
	  
		
            ready: function() {
                var cy = this;
                cy.load(networkData.elements);
                $scope.cy = cy;
                setEventListeners();
                $scope.cy.style().fromJson($scope.visualStyles
                [DEFAULT_VISUAL_STYLE_NAME].style).update();
                updateNetworkData(cy);
	        angular.element('.loading').hide();
				//$('#752').addClass('highlighted');
				
				//$scope.#752.addClass('highlighted');
                /*$scope.cy = this;
                $scope.cy.load(networkData.elements);
		/*$scope.cy = cy;
                $scope.cy.style().fromJson($scope.visualStyles[DEFAULT_VISUAL_STYLE_NAME].style).update();
                updateNetworkData(cy);*/
                /*if (!gistStyle) {
                    VisualStyles.query({
                        styleUrl: visualStyleFile
                    }, function(vs) {
                        init(vs);
                        dropSupport();
                        setEventListeners();
                        var newStyle = $routeParams.selectedstyle;
                        if (!newStyle) {
                            newStyle = DEFAULT_VISUAL_STYLE_NAME;
                        }
                        $scope.cy.style().fromJson($scope.visualStyles[newStyle].style).update();
                        $scope.style = newStyle;
                        angular.element('.loading').remove();
                    });
                } else {
                    init(gistStyle);
                    dropSupport();
                    setEventListeners();
                    $scope.cy.style().fromJson($scope.visualStyles[DEFAULT_VISUAL_STYLE_NAME].style).update();
                    $scope.style = DEFAULT_VISUAL_STYLE_NAME;
                    angular.element('.loading').remove();
                }*/
            }
        };



	function updateNetworkData(cy) {
            var dropZone = $('#network');
            dropZone.on('dragenter', function (e) {
                e.stopPropagation();
                e.preventDefault();
            });

            dropZone.on('dragover', function (e) {
                e.stopPropagation();
                e.preventDefault();
            });
            dropZone.on('drop', function (e) {
                e.preventDefault();
                var files = e.originalEvent.dataTransfer.files;
                var networkFile = files[0];
                var reader = new FileReader();
                reader.onload = function (evt) {
                    var network = JSON.parse(evt.target.result);
                    var networkName = network.data.name;
                    console.log("NetworkName = " + networkName);
                    if(networkName === undefined) {
                        networkName = "Unknown";
                    }
                    $scope.$apply(function() {
                        $scope.networks[networkName] = network;
                        $scope.networkNames.push(networkName);
                        $scope.currentNetwork = networkName;
                        console.log($scope.networkNames);
                    });
                    cy.load(network.elements);
                };
                reader.readAsText(networkFile);
            });
        }
        
        //Setting column names
        function setColumnNames() {
            $scope.columnNames = [];
            $scope.edgeColumnNames = [];
            $scope.networkColumnNames = [];

            var oneNode = $scope.nodes[0];
            for (var colName in oneNode.data) {
                $scope.columnNames.push(colName);
            }
            var oneEdge = $scope.edges[0];
            for (var edgeColName in oneEdge.data) {
                $scope.edgeColumnNames.push(edgeColName);
            }
            for (var netColName in networkData.data) {
                $scope.networkColumnNames.push(netColName);
            }
        }

        function reset() {
            $scope.selectedNodes = {};
            $scope.selectedEdges = {};
        }

        /*
         Event listener setup for Cytoscape.js
         */
        function setEventListeners() {
            $scope.selectedNodes = {};
            $scope.selectedEdges = {};

            var updateFlag = false;

            // Node selection
            $scope.cy.on('select', 'node', function(event) {
                var id = event.cyTarget.id();
                $scope.selectedNodes[id] = event.cyTarget;
                $scope.selectedNodes[id].addClass('highlighted');
                updateFlag = true;
            });
            
             // Reset selection
            $scope.cy.on('unselect', 'node', function(event) {
                var id = event.cyTarget.id();
                delete $scope.selectedNodes[id];
                updateFlag = true;
            });

            $scope.cy.on('select', 'edge', function(event) {
                var id = event.cyTarget.id();
                $scope.selectedEdges[id] = event.cyTarget;
                updateFlag = true;
            });

           
            $scope.cy.on('unselect', 'edge', function(event) {
                var id = event.cyTarget.id();
                delete $scope.selectedEdges[id];
                updateFlag = true;
            });

            setInterval(function() {
                if (updateFlag && $scope.browserState.show) {
                    console.log('* update called');
                    //displays node data
                    console.log($scope.nodes[0].data);
                    console.log($scope.edges[0]);
                    setColumnNames();
                    $scope.$apply();
                    updateFlag = false;
                }
            }, 300);

        }

        //Toolbar and overlay controls
        $scope.toggleTableBrowser = function() {
            $scope.browserState.show = !$scope.browserState.show;
        };

        $scope.toggleOverlay = function() {
            $scope.overlayState.show = !$scope.overlayState.show;
        };

        $scope.toggleToolbar = function() {
            $scope.toolbarState.show = !$scope.toolbarState.show;
        };
        
        $scope.toggleSearch = function() {
            $scope.searchState.show = !$scope.searchState.show;
        };
        
        $scope.toggleCAD = function() {
            
            $( ".searchBox" ).append($(".addSlider"));
            $scope.cadState.show = !$scope.cadState.show;
        };
        
        $scope.toggleModel = function() {
            $scope.modelState.show = !$scope.modelState.show;
        };

        $scope.fit = function() {
            $scope.cy.fit();
        };
       
        
       //Variables for CAD selecting
        $scope.currentCad;
        var currentCadId;
        var cadArray = [];
        var currentIndex;
        
        //Table button for controlling "selected" CAD
        function cadSelect() {
            //clearing selected node
            console.log("Clearing selection... ");
            $scope.currentCad = $scope.selectedNodes[currentCadId].data('SBOL');               //assigning new selected CAD
            console.log("New selected Cad is:" + currentCadId);
        };
        
        $scope.cadTable = function(id) {
            currentCadId = id;
            cadSelect();
        };
        
        //Side buttons for selecting CAD
        $scope.cadLeft = function () {
            cadArray = [];
            var cadId;
            //Creating a traversable array of CAD's
            for (var key in $scope.selectedNodes) {
                cadId = ($scope.selectedNodes[key].data('id'));
                cadArray.push(cadId);
            }; 
            
            currentIndex = cadArray.indexOf(String(currentCadId));
            currentCadId = cadArray[currentIndex - 1];
            
            //Preventing further cycling
            if(currentCadId === undefined) {
                currentCadId = cadArray[0];
                cadSelect();
            }
            else{
                cadSelect();
            };      
        };
        
        $scope.cadRight = function () {
            cadArray = [];
            var cadId;
            //Creating a traversable array of CAD's
            for (var key in $scope.selectedNodes) {
                cadId = ($scope.selectedNodes[key].data('id'));
                cadArray.push(cadId);
            };            
            currentIndex = cadArray.indexOf(String(currentCadId));
            currentCadId = cadArray[currentIndex + 1];
            
            //Preventing further cycling
            if(currentCadId === undefined) {
                currentCadId = cadArray[cadArray.length - 1];
                cadSelect();
            }
            else{
                cadSelect();
            };   
        };
         
        //Highlighting and controlling selected paths.

        //Adding result selection to interface, highlighting first result.
        $scope.searchText;
        //Array of all dropdown options for resulting paths.
        $scope.resultIndex = [];
        //Index of selected circuite that is ng-modeled by the dropdown menu in the app.
        $scope.selectedCircuit;

        //
        $scope.searchCtrl = function () {
            //alert($scope.searchText);
            //the input and output of the user 
            $scope.input = String($scope.searchInput);
            $scope.output = String($scope.searchOutput);
            $scope.BooleanTrue = String($scope.checkTrue);
            //combination of input = output 
            $scope.query = ($scope.input + " = " + $scope.output + " " + $scope.BooleanTrue);
            
            //the default is false, when checked its true and direct path is set
            
            console.log($scope.query);
            
            angular.element('.loading').show();
            searchGet();
            
            //$scope.circuitCtrl();
        };
        
        //refreshes the inputs and the page 
         $scope.reloadPage = function()
         {$scope.cynet.load(networkDefault.elements);
         };

        //function for highlighting a path.        
        $scope.selectPath = function(index) {
            reset();
            $scope.cynet.$('*').unselect();
            for (var count = 0; count < speciesId[index].length; count++){
                $scope.cynet.$("#"+String(speciesId[index][count])).select();
            };
            for (var count = 0; count < transitionId[index].length; count++){
                $scope.cynet.$("#"+String(transitionId[index][count])).select();
            };
            for (var count = 0; count < edgeId[index].length; count++){
                $scope.cynet.$("#"+String(edgeId[index][count])).select();
            };
            console.log("New Circuit Selected.");
        };
        $scope.circuitCtrl = function() {
            for (var result = 0; result <speciesId.length; result ++){
                $scope.resultIndex.push({ label: "Path " + String(result + 1), value: result});
            };
        };
        $scope.circuitCtrl();
        
        $scope.encodeUrl = function() {
            var pan = $scope.cy.pan();
            var zoom = $scope.cy.zoom();

            // The following fields should be encoded because it may includes special chars.
            var bgColor = encodeURIComponent($scope.bg.color);
            var encodedStyleName = encodeURIComponent($scope.currentVS);
            console.log(zoom);
            console.log(encodedStyleName);
            console.log(bgColor);
            $scope.encodedUrl = originalLocation + '?selectedstyle=' + encodedStyleName +
                '&x=' + pan.x + '&y=' + pan.y + '&zoom=' + zoom + '&bgcolor=' + bgColor;
        };


        // Encode visualization URL.
        $scope.shortenUrl = function() {
            var request = $http({
                method: 'post',
                url: 'https://www.googleapis.com/urlshortener/v1/url',
                data: {
                    longUrl: $scope.encodedUrl
                }
            });
            // Store the data-dump of the FORM scope.
            request.success(
                function(json) {
                    $scope.encodedUrl = json.id;
                    angular.element('#shareUrl').select();
                }
            );
        };
        
	/////////////New content
	$scope.switchNetwork = function(networkName) {
	     $scope.currentNetwork = networkName;//changed to include currentNetworkData as opposed to only currentNetwork
            //$scope.currentNetwork = networkName;
            var network = $scope.networks[networkName];
            $scope.cy.load(network.elements);
        };

        //
        // Apply Visual Style
        //
        $scope.switchVS = function(vsName) {
            // Apply Visual Style
            $scope.cy.style().fromJson($scope.visualStyles[vsName].style).update();
            // Set current title
            $scope.currentVS = vsName;
        };
	
        
	
	$http({method: 'GET', url: visualStyleFile}).
            success(function(data) {
                
                vs = data;
                $http({method: 'GET', url: NETWORK_FILE}).
                    success(function(data) {
                        networkData = data;
                        networkDefault = data;
                        $('#network').cytoscape(options);
                        $scope.cynet = $('#network').cytoscape('get');
                        init();
                    }).
                    error(function(data, status, headers, config) {
                    });
                //             The Actual GET request.
                /*
                $http({
                    method: 'GET', 
                    url: "/src/java/communication/AuthenticationServlet.java"
                    }).
                    success(function(data) {
                        networkData = JSON.parse(data);
                        networkDefault = JSON.parse(data);
                        $('#network').cytoscape(options);
                        $scope.cynet = $('#network').cytoscape('get');
                        init();
                    }).
                    error(function(data, status, headers, config) {
                        alert(status);
                    });
                */
            }).
            error(function(data, status, headers, config) {
            });
    
            
        function searchGet() {
            
            
            var commandString = $scope.query;
            alert(commandString);
            var data = {user: userID, command: 'query', data: commandString}; //package the input into a json file for submission to the server
                  
                    $.get("../../AuthenticationServlet", data, function(data) { //parameters are: servlet url, data, callback function
                    data = JSON.stringify(data).replace(/\\n/g, '',"").replace(/\\/g, '',"")
                    data = data.substr(1,data.length-2)
                    alert(data)
                    networkData = JSON.parse(data);
                    angular.element('.loading').hide();
                    alert(JSON.stringify(networkData.elements))
                    $scope.cynet.load(networkData.elements);
                    
                    });
                
//            $http({ 
//                method: 'GET', 
//                url: "../../AuthenticationServlet",
//                params: { user: userID, command: "query" , data: $scope.query }
//                }).
////                alert("$http was called with: " + $scope.query);
//                success(function(data) {
//                    alert("shit went through");
//                    alert(data);
//                    networkData = JSON.parse(data);
//                    alert(networkData);
//                    $scope.cynet.load(networkData.elements);
//                }).
//                error(function(data, status, headers, config) {
//                });
        };
        
        
        

	function init() {
            $scope.nodes = networkData.elements.nodes;
            //Added function to retrieve edge information
            $scope.edges = networkData.elements.edges;
            initVisualStyleCombobox();
            // Set network name
            var networkName = networkData.data.name;
            $scope.currentNetwork = networkData.data.name;//changed to include currentNetworkData as opposed to only currentNetwork
            $scope.networks[networkName] = networkData;
            $scope.networkNames.push(networkName);
        }

	function initVisualStyleCombobox() {
            var styleNames = [];
            for (var i = 0; i < vs.length; i++) {
                var visualStyle = vs[i];
                var title = visualStyle.title;
                styleNames[i] = title;
                $scope.visualStyles[title] = visualStyle;
                $scope.styleNames[i] = title;
            }
        }
              
    });


    /*function CarouselDemoCtrl($scope) {
  $scope.myInterval = 5000;
  var slides = $scope.slides = [];
  $scope.addSlide = function() {
    var newWidth = 50 + slides.length;
    slides.push({
      image: 'http://placekitten.com/' + newWidth + '/30',
      text: ['More','Extra','Lots of','Surplus'][slides.length % 4] + ' ' +
        ['Cats', 'Kittys', 'Felines', 'Cutes'][slides.length % 4]
    });
  };
  for (var i=0; i<4; i++) {
    $scope.addSlide();
  }
};*/ 	

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
