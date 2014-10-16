
angular.module('cyViewerApp')

        .controller('MainCtrl', function($scope, $http, $location, $routeParams,
                $window, Network, VisualStyles, Gist) {

            'use strict';
            //these files are the temporary network
            var NETWORK_FILE = 'data/sbider_whole_network.json';
            var visualStyleFile = 'data/sbiderStyle.json';
            var DEFAULT_VISUAL_STYLE_NAME = 'default';//'Solid';
            var PRESET_STYLE_FILE = encodeURIComponent('data/sbiderStyle.json');
            var tempJSON = '{"data" : { "selected" : true,"_Annotations": [] ,"shared_name" : "Test.sif","SUID" : 52,"name":"Test.sif"},"elements":{"nodes":[{"data":{"id":"spe_13","name":"lara","type":"None","sbml":"species_sbml_13.txt"},"position":{"x":81.362787974,"y":54.9882473208},"classes":"species","selected":false},{"data":{"id":"spe_2","name":"arac","type":"None","sbml":"species_sbml_2.txt"},"position":{"x":70.1211838744,"y":88.5038033015},"classes":"species","selected":false},{"data":{"id":"spe_11","name":"gfp","type":"None","sbml":"species_sbml_11.txt"},"position":{"x":286.243038737,"y":177.283279157},"classes":"species","selected":false},{"data":{"id":"spe_9","name":"luxr","type":"None","sbml":"species_sbml_9.txt"},"position":{"x":139.550929534,"y":357.72336417},"classes":"species","selected":false},{"data":{"id":"spe_25","name":"ahl","type":"None","sbml":"species_sbml_25.txt"},"position":{"x":319.453012417,"y":292.938673327},"classes":"species","selected":false},{"data":{"id":"it_61","logic":"AND","sbml":"it_sbml_61.txt"},"position":{"x":182.813011425,"y":39.5662080052},"classes":"input transition","selected":false},{"data":{"id":"it_98","logic":"AND","sbml":"it_sbml_98.txt"},"position":{"x":9.31069590536,"y":187.412397434},"classes":"input transition","selected":false},{"data":{"id":"it_48","logic":"AND","sbml":"it_sbml_48.txt"},"position":{"x":250.05765914,"y":336.95088859},"classes":"input transition","selected":false},{"data":{"id":"it_46","logic":"AND","sbml":"it_sbml_46.txt"},"position":{"x":120.664474846,"y":4.67570828915},"classes":"input transition","selected":false},{"data":{"id":"it_82","logic":"AND","sbml":"it_sbml_82.txt"},"position":{"x":28.042061549,"y":79.00850911},"classes":"input transition","selected":false},{"data":{"id":"ope_35-1","sbml":"operon_sbml_35-1.txt","sbol":"operon_sbol_35-1.png","name":"pBAD--->gfp"},"position":{"x":325.286367567,"y":67.6287284428},"classes":"operon","selected":false},{"data":{"id":"ope_24-2","sbml":"operon_sbml_24-2.txt","sbol":"operon_sbol_24-2.png","name":"pBAD--->gfp"},"position":{"x":216.706250773,"y":0.0},"classes":"operon","selected":false},{"data":{"id":"ope_25-2","sbml":"operon_sbml_25-2.txt","sbol":"operon_sbol_25-2.png","name":"pLux--->gfp"},"position":{"x":222.021232792,"y":360.0},"classes":"operon","selected":false},{"data":{"id":"ope_50-1","sbml":"operon_sbml_50-1.txt","sbol":"operon_sbol_50-1.png","name":"pLac_pBAD--->gfp"},"position":{"x":0.0,"y":144.210925666},"classes":"operon","selected":false},{"data":{"id":"ope_57-1","sbml":"operon_sbml_57-1.txt","sbol":"operon_sbol_57-1.png","name":"pLac_pBAD--->LuxR_luxI"},"position":{"x":48.8387662922,"y":296.87335866},"classes":"operon","selected":false},{"data":{"id":"ot_39","sbml":"ot_sbml_39.txt"},"position":{"x":289.172610514,"y":41.3502115913},"classes":"output transition","selected":false},{"data":{"id":"ot_75","sbml":"ot_sbml_75.txt"},"position":{"x":136.756449626,"y":181.139645625},"classes":"output transition","selected":false},{"data":{"id":"ot_54","sbml":"ot_sbml_54.txt"},"position":{"x":357.816299279,"y":142.515521877},"classes":"output transition","selected":false},{"data":{"id":"ot_41","sbml":"ot_sbml_41.txt"},"position":{"x":300.376264176,"y":314.405974266},"classes":"output transition","selected":false},{"data":{"id":"ot_86","sbml":"ot_sbml_86.txt"},"position":{"x":170.894666776,"y":332.342877406},"classes":"output transition","selected":false}],"edges":[{"data":{"id":"50","source":"ope_50-1","target":"ot_75"},"selected":false},{"data":{"id":"51","source":"spe_2","target":"it_98"},"selected":false},{"data":{"id":"52","source":"it_46","target":"ope_24-2"},"selected":false},{"data":{"id":"53","source":"ope_57-1","target":"ot_86"},"selected":false},{"data":{"id":"54","source":"spe_13","target":"it_61"},"selected":false},{"data":{"id":"55","source":"it_48","target":"ope_25-2"},"selected":false},{"data":{"id":"56","source":"ot_54","target":"spe_11"},"selected":false},{"data":{"id":"57","source":"spe_9","target":"it_48"},"selected":false},{"data":{"id":"58","source":"spe_25","target":"it_48"},"selected":false},{"data":{"id":"59","source":"it_61","target":"ope_35-1"},"selected":false},{"data":{"id":"60","source":"ope_24-2","target":"ot_39"},"selected":false},{"data":{"id":"61","source":"ot_75","target":"spe_11"},"selected":false},{"data":{"id":"62","source":"spe_13","target":"it_98"},"selected":false},{"data":{"id":"63","source":"spe_2","target":"it_46"},"selected":false},{"data":{"id":"64","source":"ope_25-2","target":"ot_41"},"selected":false},{"data":{"id":"65","source":"spe_2","target":"it_82"},"selected":false},{"data":{"id":"66","source":"ot_41","target":"spe_11"},"selected":false},{"data":{"id":"67","source":"ot_86","target":"spe_9"},"selected":false},{"data":{"id":"68","source":"spe_13","target":"it_46"},"selected":false},{"data":{"id":"69","source":"it_98","target":"ope_57-1"},"selected":false},{"data":{"id":"70","source":"ot_86","target":"spe_25"},"selected":false},{"data":{"id":"71","source":"spe_13","target":"it_82"},"selected":false},{"data":{"id":"72","source":"ope_35-1","target":"ot_54"},"selected":false},{"data":{"id":"73","source":"ot_39","target":"spe_11"},"selected":false},{"data":{"id":"74","source":"it_82","target":"ope_50-1"},"selected":false},{"data":{"id":"75","source":"spe_2","target":"it_61"},"selected":false}]},"speciesId": [["spe_2", "spe_11", "spe_13"], ["spe_2", "spe_11", "spe_13"], ["spe_2", "spe_11", "spe_13"], ["spe_25", "spe_2", "spe_11", "spe_13", "spe_9"]],"inputTransitionsId": [["it_46"], ["it_61"], ["it_82"], ["it_98", "it_48"]],"operonsId": [["ope_24-2"], ["ope_35-1"], ["ope_50-1"], ["ope_25-2", "ope_57-1"]],"outputTransitionsId": [["ot_39"], ["ot_54"], ["ot_75"], ["ot_41", "ot_86"]],"edgesId": [["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1", "edge_1", "edge_1"]]}';
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
            var speciesId = [];
            var inputTransitionsId = [];
            var operonsId = [];
            var outputTransitionsId = [];
            var edgesId = [];

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
                dropZone.on('dragenter', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                });

                dropZone.on('dragover', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                });
                dropZone.on('drop', function(e) {
                    e.preventDefault();
                    var files = e.originalEvent.dataTransfer.files;
                    var networkFile = files[0];
                    var reader = new FileReader();
                    reader.onload = function(evt) {
                        var network = JSON.parse(evt.target.result);
                        var networkName = network.data.name;
                        console.log("NetworkName = " + networkName);
                        if (networkName === undefined) {
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

                $(".searchBox").append($(".addSlider"));
                $scope.cadState.show = !$scope.cadState.show;
            };

            $scope.toggleModel = function() {
                $scope.modelState.show = !$scope.modelState.show;
            };

            $scope.fit = function() {
                $scope.cy.fit();
            };

            //Variables for CAD selecting
            $scope.currentCad = "no_image.png";
            $scope.currentCadName = "No image selected";
            var currentCadId;
            var cadArray = [];
            var currentIndex;
            
            //Sets the CAD image slider's caption to the node name if possible.
            function cadNameSet(id){
                if($scope.selectedNodes[id].data('name') === undefined){
                    $scope.currentCadName = "Transition";
                }
                else{
                    $scope.currentCadName = $scope.selectedNodes[id].data('name');
                };                
            };
            
            //Randomizes placeholder images for nodes without SBOL attribute.
            var randomImage;
            function placeholderRandom(){
                var roll = Math.floor((Math.random() * 10) + 1)/2;
//                console.log(roll);
                if(roll <= 1) {
                    randomImage = 1;
                }
                else if(roll > 1 && roll <=2){
                    randomImage = 2;
                }
                else if(roll > 2 && roll <=3){
                    randomImage = 3;
                }
                else if(roll > 3 && roll <=4){
                    randomImage = 4;
                }
                else{
                    randomImage = 5;
                };
            };
            
            //Table button for controlling "selected" CAD
            function cadSelect() {
                //clearing selected node
                console.log("Clearing selection... ");
                if ($scope.selectedNodes === undefined || $scope.selectedNodes[currentCadId].data('sbol') === undefined || $scope.selectedNodes[currentCadId].data('sbol') === "") {             
                    
                    placeholderRandom();
                    
                    if($scope.selectedNodes[currentCadId].hasClass("species") === true) {
                        $scope.currentCad = "holder_species_" + String(randomImage) + ".png";
                    }
                    else if($scope.selectedNodes[currentCadId].hasClass("input") === true) {
                        $scope.currentCad = "holder_input_transition_" + String(randomImage) + ".png";
                    }
                    else if($scope.selectedNodes[currentCadId].hasClass("output") === true) {
                        $scope.currentCad = "holder_output_transition_" + String(randomImage) + ".png";
                    }
                    else{
                        $scope.currentCad = "no_image.png";
                    };
                }
                else {
                    $scope.currentCad = $scope.selectedNodes[currentCadId].data('sbol'); //assigning new selected CAD
                };
                
                cadNameSet(currentCadId);
                console.log("New selected Cad is:" + currentCadId);
            }
            ;

            $scope.cadTable = function(id) {
                currentCadId = id;
                cadSelect();
            };

            //Side buttons for selecting CAD
            $scope.cadLeft = function() {
                cadArray = [];
                var cadId;
                //Creating a traversable array of CAD's
                for (var key in $scope.selectedNodes) {
                    cadId = ($scope.selectedNodes[key].data('id'));
                    cadArray.push(cadId);
                }
                ;

                currentIndex = cadArray.indexOf(String(currentCadId));
                currentCadId = cadArray[currentIndex - 1];

                //Preventing further cycling
                if (currentCadId === undefined) {
                    currentCadId = cadArray[0];
                    cadSelect();
                }
                else {
                    cadSelect();
                }
                ;
            };

            $scope.cadRight = function() {
                cadArray = [];
                var cadId;
                //Creating a traversable array of CAD's
                for (var key in $scope.selectedNodes) {
                    cadId = ($scope.selectedNodes[key].data('id'));
                    cadArray.push(cadId);
                }
                ;
                currentIndex = cadArray.indexOf(String(currentCadId));
                currentCadId = cadArray[currentIndex + 1];

                //Preventing further cycling
                if (currentCadId === undefined) {
                    currentCadId = cadArray[cadArray.length - 1];
                    cadSelect();
                }
                else {
                    cadSelect();
                }
                ;
            };

            //Highlighting and controlling selected paths.

            //Adding result selection to interface, highlighting first result.
            $scope.searchText;
            //Array of all dropdown options for resulting paths.
            $scope.resultIndex = [];
            //Index of selected circuit that is ng-modeled by the dropdown menu in the app.
            $scope.selectedCircuit;

            //
            $scope.searchCtrl = function() {
                //alert($scope.searchText);
                //the input and output of the user 
                $scope.input = String($scope.searchInput);
                $scope.output = String($scope.searchOutput);
                $scope.BooleanTrue = String($scope.checkTrue);
                //Catching error in BooleanTrue that occurs when multiple 
                //searches are run without page reload.
                if($scope.BooleanTrue === "false"){
                    $scope.BooleanTrue = "undefined";
                };
                //combination of input = output 
                $scope.query = ($scope.input + " = " + $scope.output + " " + $scope.BooleanTrue);

                //the default is false, when checked its true and direct path is set

                console.log($scope.query);

                angular.element('.loading').show();

                //Clearing selected elements and paths.
                reset();
                $scope.cynet.$('*').unselect();
                //Clearing path results.
                $scope.resultIndex = [];
                //Clearing selected image.
                $scope.currentCad = "no_image.png";
                $scope.currentCadName = "No image selected";

                networkData = JSON.parse(tempJSON);
                console.log(networkData);
                angular.element('.loading').hide();
                $scope.cynet.load(networkData.elements);
                $scope.circuitCtrl();
              
//                searchGet();
            };

            //refreshes the inputs and the page 
            $scope.reloadPage = function() {
                reset();
                $scope.cynet.$('*').unselect();
                $scope.resultIndex = [];
                $scope.cynet.load(networkDefault.elements);
                $scope.currentCad = "no_image.png";
                $scope.currentCadName = "No image selected";
            };

            //function for highlighting a path.        
            $scope.selectPath = function(index) {
                reset();
                $scope.cynet.$('*').unselect();
                for (var count = 0; count < operonsId[index].length; count++) {
                    $scope.cynet.$("#" + String(operonsId[index][count])).select();
                }
                ;
                for (var count = 0; count < speciesId[index].length; count++) {
                    $scope.cynet.$("#" + String(speciesId[index][count])).select();
                }
                ;
                for (var count = 0; count < inputTransitionsId[index].length; count++) {
                    $scope.cynet.$("#" + String(inputTransitionsId[index][count])).select();
                }
                ;
                for (var count = 0; count < outputTransitionsId[index].length; count++) {
                    $scope.cynet.$("#" + String(inputTransitionsId[index][count])).select();
                }
                ;
                for (var count = 0; count < edgesId[index].length; count++) {
                    $scope.cynet.$("#" + String(edgesId[index][count])).select();
                }
                ;
                console.log("New Circuit Selected.");
            };
            $scope.circuitCtrl = function() {
                speciesId = networkData.speciesId;
                inputTransitionsId = networkData.inputTransitionsId;
                operonsId = networkData.operonsId;
                outputTransitionsId = networkData.outputTransitionsId;
                edgesId = networkData.edgesId;

                for (var result = 0; result < speciesId.length; result++) {
                    $scope.resultIndex.push({"label": "Path " + String(result + 1), "value": result});
                }
                ;
                $scope.selectedCircuit = $scope.resultIndex[0];
                $scope.selectPath($scope.selectedCircuit.value);
            };
            
            $scope.plasmidUpdate = {
                "name" : "Name",
                "pubMedId" : "PubMed Id: PMC#",
                "operons": [                    
                    {"operon":{
                        "name": "Name",
                        "direction": "Left or Right",
                        "inputTransitions":[
                            {"inputTransition":{
                                    "promoter":"Name",
                                    "logic": "Boolean Logic Type",
                                    "inputSpecies":[
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }},
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }}
                                    ]
                            }},
                            {"inputTransition":{
                                    "promoter":"Name",
                                    "logic": "Boolean Logic Type",
                                    "inputSpecies":[
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }},
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }}
                                    ]
                            }}
                        ],
                        "outputSpecies":[
                            {"outputSpecies":{
                                "name": "Name",
                                "type": "Type"
                            }},
                            {"outputSpecies":{
                                "name": "Name",
                                "type": "Type"
                            }}
                        ]
                    }},
                    {"operon":{
                        "name": "Name",
                        "direction": "Left or Right",
                        "inputTransitions":[
                            {"inputTransition":{
                                    "promoter":"Name",
                                    "logic": "Boolean Logic Type",
                                    "inputSpecies":[
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }},
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }}
                                    ]
                            }},
                            {"inputTransition":{
                                    "promoter":"Name",
                                    "logic": "Boolean Logic Type",
                                    "inputSpecies":[
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }},
                                        {"inputSpecies":{
                                            "name": "Name",
                                            "type": "Type",
                                            "repression": "Repressor? True or False"
                                        }}
                                    ]
                            }}
                        ],
                        "outputSpecies":[
                            {"outputSpecies":{
                                "name": "Name",
                                "type": "Type"
                            }},
                            {"outputSpecies":{
                                "name": "Name",
                                "type": "Type"
                            }}
                        ]
                    }} 
                ]                
            };
            $scope.updateString;

            $scope.plasmidStringParser = function(){
                var plas = $scope.plasmidUpdate;
                $scope.updateString = "plasmid:" + plas.name + "," + String(plas.pubMedId) + "\t";
                
                for (var opeNum = 0; opeNum < plas.operons.length; opeNum ++){
                    var ope = plas.operons[opeNum].operon;
                    $scope.updateString += "operon:" + ope.name + "," + ope.direction + "\t";
                    
                    for(var itNum = 0; itNum < ope.inputTransitions.length; itNum++){
                        var it = ope.inputTransitions[itNum].inputTransition;
                        $scope.updateString += "inputTransition:" + it.promoter + "," + it.logic + "\t";
                        for(var inSpecNum = 0; inSpecNum < it.inputSpecies.length; inSpecNum ++){
                            var inSpec = it.inputSpecies[inSpecNum].inputSpecies;
                            $scope.updateString += "inputSpecies:" + inSpec.name + "," +inSpec.type + "," +inSpec.repression + "\t";
                        };
                    };
                    
                    for (var outSpecNum = 0; outSpecNum < ope.outputSpecies.length; outSpecNum ++){
                        var outSpec = ope.outputSpecies[outSpecNum].outputSpecies;
                        $scope.updateString += "outputSpecies:" + outSpec.name + "," + outSpec.type + "\t";
                    };
                };
                console.log($scope.updateString);
            };

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
                                    $scope.toggleCAD();
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
                if (commandString === "undefined = undefined undefined" || $scope.searchInput === undefined || $scope.searchInput === "" || $scope.searchOutput === undefined || $scope.searchOutput === "") {
                    alert("Please enter a valid query.");
                    angular.element('.loading').hide();
                }

                else {

                    var data = {user: userID, command: 'query', data: commandString}; //package the input into a json file for submission to the server
                    $.get("../../AuthenticationServlet", data, function(data) { //parameters are: servlet url, data, callback function
                        data = JSON.stringify(data).replace(/\\n/g, '', "").replace(/\\/g, '', "");
                        data = data.substr(1, data.length - 2);
//                        alert(data);
                        networkData = JSON.parse(data);
                        angular.element('.loading').hide();

                        if (typeof networkData.error === "string") {
                            alert(networkData.error);
                        }
                        else if (networkData.operonsId[0] === null && $scope.BooleanTrue === undefined) {
                            alert('No circuits found. Please try searching for an Indirect Path (check the box marked "Indirect Path").');
                        }
                        else if (networkData.operonsId[0] === null && $scope.BooleanTrue === "true") {
                            alert('No circuits found in current database. Results may change as the SBiDer web grows.');
                        }
                        else {
                            $scope.cynet.load(networkData.elements);
                            console.log(networkData);
                            $scope.circuitCtrl();
                        };

                    });
                };

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

            }
            ;




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
