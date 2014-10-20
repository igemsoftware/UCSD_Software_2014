
angular.module('cyViewerApp')

    .controller('MainCtrl', function($scope, $http, $location, $routeParams,
            $window, Network, VisualStyles, Gist) {

        'use strict';
        //these files are the temporary network
        var NETWORK_FILE = '../../whole_network.json';
        var visualStyleFile = 'data/sbiderStyle.json';
        var DEFAULT_VISUAL_STYLE_NAME = 'default';//'Solid';
        var PRESET_STYLE_FILE = encodeURIComponent('data/sbiderStyle.json');
        var tempJSON = '{"data" : { "selected" : true,"_Annotations": [] ,"shared_name" : "Test.sif","SUID" : 52,"name":"Test.sif"},"elements":{"nodes":[{"data":{"id":"spe_13","name":"ahl","type":"None","sbml":"species_sbml_13_.txt"},"position":{"x":1647.08594482,"y":8598.94923601},"classes":"species","selected":false},{"data":{"id":"spe_38","name":"lara","type":"None","sbml":"species_sbml_38_.txt"},"position":{"x":7512.31542492,"y":677.903112321},"classes":"species","selected":false},{"data":{"id":"spe_9","name":"luxr","type":"None","sbml":"species_sbml_9_.txt"},"position":{"x":2687.68400151,"y":9096.77965734},"classes":"species","selected":false},{"data":{"id":"spe_2","name":"arac","type":"None","sbml":"species_sbml_2_.txt"},"position":{"x":6818.09580237,"y":1245.48879966},"classes":"species","selected":false},{"data":{"id":"spe_11","name":"gfp","type":"None","sbml":"species_sbml_11_.txt"},"position":{"x":4564.40456877,"y":6235.4913226},"classes":"species","selected":false},{"data":{"id":"it_80","logic":"AND","sbml":"it_sbml_80_.txt"},"position":{"x":9376.95360885,"y":2583.09845369},"classes":"input transition","selected":false},{"data":{"id":"it_86","logic":"AND","sbml":"it_sbml_86_.txt"},"position":{"x":4844.7976263,"y":0.0},"classes":"input transition","selected":false},{"data":{"id":"it_97","logic":"AND","sbml":"it_sbml_97_.txt"},"position":{"x":8894.89274833,"y":1836.73106933},"classes":"input transition","selected":false},{"data":{"id":"it_107","logic":"AND","sbml":"it_sbml_107_.txt"},"position":{"x":6926.40093122,"y":4214.7270139},"classes":"input transition","selected":false},{"data":{"id":"it_81","logic":"AND","sbml":"it_sbml_81_.txt"},"position":{"x":685.36275705,"y":7220.26621579},"classes":"input transition","selected":false},{"data":{"id":"ope_24-2","sbml":"operon_sbml_24-2_.txt","sbol":"operon_sbol_24-2_.png","name":"pBAD--->gfp"},"position":{"x":10000.0,"y":4579.1685352},"classes":"operon","selected":false},{"data":{"id":"ope_57-1","sbml":"operon_sbml_57-1_.txt","sbol":"operon_sbol_57-1_.png","name":"pLac_pBAD--->LuxR_luxI"},"position":{"x":6472.40787568,"y":8940.22250002},"classes":"operon","selected":false},{"data":{"id":"ope_50-1","sbml":"operon_sbml_50-1_.txt","sbol":"operon_sbol_50-1_.png","name":"pLac_pBAD--->gfp"},"position":{"x":9898.14814649,"y":5838.44100614},"classes":"operon","selected":false},{"data":{"id":"ope_25-2","sbml":"operon_sbml_25-2_.txt","sbol":"operon_sbol_25-2_.png","name":"pLux--->gfp"},"position":{"x":0.0,"y":4412.71735088},"classes":"operon","selected":false},{"data":{"id":"ope_35-1","sbml":"operon_sbml_3These arrays can be accessed from the directly from the first initial json object. Each array contains 5-1_.txt","sbol":"operon_sbol_35-1_.png","name":"pBAD--->gfp"},"position":{"x":2501.34325291,"y":743.386070972},"classes":"operon","selected":false},{"data":{"id":"ot_98","sbml":"ot_sbml_ot_98_.txt"},"position":{"x":4167.61142875,"y":9776.8845485},"classes":"output transition","selected":false},{"data":{"id":"ot_90","sbml":"ot_sbml_ot_90_.txt"},"position":{"x":8287.83384551,"y":8618.90819216},"classes":"output transition","selected":false},{"data":{"id":"ot_73","sbml":"ot_sbml_ot_73_.txt"},"position":{"x":8777.32982673,"y":7156.15959443},"classes":"output transition","selected":false},{"data":{"id":"ot_74","sbml":"ot_sbml_ot_74_.txt"},"position":{"x":180.847242818,"y":5817.35785317},"classes":"output transition","selected":false},{"data":{"id":"ot_79","sbml":"ot_sbml_ot_79_.txt"},"position":{"x":1786.32933156,"y":2794.81164864},"classes":"output transition","selected":false}],"edges":[{"data":{"id":"50","source":"spe_38","target":"it_97"},"selected":false},{"data":{"id":"51","source":"spe_38","target":"it_107"},"selected":false},{"data":{"id":"52","source":"it_81","target":"ope_25-2"},"selected":false},{"data":{"id":"53","source":"spe_2","target":"it_107"},"selected":false},{"data":{"id":"54","source":"ot_98","target":"spe_13"},"selected":false},{"data":{"id":"55","source":"it_107","target":"ope_57-1"},"selected":false},{"data":{"id":"56","source":"spe_13","target":"it_81"},"selected":false},{"data":{"id":"57","source":"it_97","target":"ope_These arrays can be accessed from the directly from the first initial json object. Each array contains 50-1"},"selected":false},{"data":{"id":"58","source":"spe_38","target":"it_86"},"selected":false},{"data":{"id":"59","source":"ope_50-1","target":"ot_90"},"selected":false},{"data":{"id":"60","source":"ot_90","target":"spe_11"},"selected":false},{"data":{"id":"61","source":"ot_73","target":"spe_11"},"selected":false},{"data":{"id":"62","source":"ot_74","target":"spe_11"},"selected":false},{"data":{"id":"63","source":"spe_2","target":"it_80"},"selected":false},{"data":{"id":"64","source":"spe_38","target":"it_80"},"selected":false},{"data":{"id":"65","source":"ope_24-2","target":"ot_73"},"selected":false},{"data":{"id":"66","source":"ope_25-2","target":"ot_74"},"selected":false},{"data":{"id":"67","source":"it_80","target":"ope_24-2"},"selected":false},{"data":{"id":"68","source":"it_86","target":"ope_These arrays can be accessed from the directly from the first initial json object. Each array contains 35-1"},"selected":false},{"data":{"id":"69","source":"spe_2","target":"it_86"},"selected":false},{"data":{"id":"70","source":"ot_98","target":"spe_9"},"selected":false},{"data":{"id":"71","source":"spe_2","target":"it_97"},"selected":false},{"data":{"id":"72","source":"ope_57-1","target":"ot_98"},"selected":false},{"data":{"id":"73","source":"ope_35-1","target":"ot_79"},"selected":false},{"data":{"id":"74","source":"spe_9","target":"it_81"},"selected":false},{"data":{"id":"75","source":"ot_79","target":"spe_11"},"selected":false}]},"speciesId": [["spe_2", "spe_38", "spe_11"], ["spe_2", "spe_38", "spe_11"], ["spe_2", "spe_38", "spe_11"], ["spe_9", "spe_2", "spe_13", "spe_38", "spe_11"]],"inputTransitionsId": [["it_80"], ["it_86"], ["it_97"], ["it_107", "it_81"]],"operonsId": [["ope_24-2"], ["ope_35-1"], ["ope_50-1"], ["ope_57-1", "ope_25-2"]],"outputTransitionsId": [["ot_73"], ["ot_79"], ["ot_90"], ["ot_98", "ot_74"]],"edgesId": [["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1"], ["edge_1", "edge_1", "edge_1", "edge_1", "edge_1"]]}';

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


//            networkData = JSON.parse(tempJSON);
//            console.log(networkData);
//            angular.element('.loading').hide();
//            $scope.cynet.load(networkData.elements);
//            $scope.circuitCtrl();

            searchGet();
        };



        //refreshes the inputs and the page 
        $scope.reloadPage = function() {
            reset();
            $scope.cynet.$('*').unselect();
            $scope.resultIndex = [];
            angular.element('.loading').show();
            $scope.cynet.load(networkDefault.elements);
            $scope.currentCad = "no_image.png";
            $scope.currentCadName = "No image selected";
            angular.element('.loading').hide();
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

        //empty arrays for use in the update form.
        $scope.plasmids=[];
        $scope.operons=[];
        $scope.inputTransitions=[];
        $scope.inputSpecies=[];
        $scope.outputSpecies=[];

        $scope.updateString;

        //Do not use this function. The database form cannot handle this much info yet!
        //This is for future additions and versions.
        //adds a plasmid to the update form fields.
        $scope.addPlasmid = function(){
            $scope.plasmids.push({
                "data":{
                    "name": {"label":"Name", "placeholder":"Name","value":""},
                    "pubMedId": {"label":"PubMed ID", "placeholder":"PMID","value":""}
                },
                "plasNum":$scope.plasmids.length
            });
        };
        //adds an operon to the update fields.
        $scope.addOperon = function(plasNum){
            $scope.operons.push({
                "data":{
                    "name": {"label":"Name", "placeholder":"Name","value":""},
                    "direction":{"label":"Direction", "placeholder":"Left(L) or Right(R)","value":""}
                },
                "opeNum":$scope.operons.length,
                "plasNum":plasNum
            });

            $scope.inputTransitions.push([]);
            $scope.inputSpecies.push([]);
            $scope.outputSpecies.push([]);

            $scope.addInTran($scope.operons.length - 1);
        };

        $scope.addInTran = function(opeNum){
            $scope.inputTransitions[opeNum].push({
                "data":{
                    "promoter": {"label":"Promoter", "placeholder":"Name","value":""},
                    "logic": {"label":"Logic", "placeholder":"Logic Type of Input Species","value":""}
                },
                "inTranNum":$scope.inputTransitions[opeNum].length,
                "opeNum":opeNum
            });

            $scope.inputSpecies[opeNum].push([]);
            $scope.outputSpecies[opeNum].push([]);

            var inTranCount = $scope.inputTransitions[opeNum].length - 1;
            $scope.addInSpec(opeNum, inTranCount);
            $scope.addOutSpec(opeNum, inTranCount);                
        };

        $scope.addInSpec = function(opeNum,inTranNum){
            $scope.inputSpecies[opeNum][inTranNum].push({
                "data":{
                    "name": {"label":"Name", "placeholder":"Name","value":""},
                    "type": {"label":"Type", "placeholder":"Type","value":""},
                    "repression": {"label":"Repression", "placeholder":"TRUE or FALSE","value":""}
                },
                "inTranNum":inTranNum
            });
        };

        $scope.addOutSpec = function(opeNum,inTranNum){
            $scope.outputSpecies[opeNum][inTranNum].push({
                "data":{
                    "name": {"label":"Name", "placeholder":"Name","value":""},
                    "type": {"label":"Type", "placeholder":"Type","value":""}
                },
                "opeNum":opeNum
            });
        };

        $scope.removeOperon = function(){
            if($scope.operons.length > 1){
                var spliced = $scope.operons.length;
                $scope.operons.splice(spliced - 1,1);
                $scope.inputTransitions.splice(spliced - 1,1);
                $scope.inputSpecies.splice(spliced - 1,1);
                $scope.outputSpecies.splice(spliced - 1,1);
            }
            else{
                $scope.errorMessage = "A Plasmids require at least one operon.";
                $("#errorModal").modal("show");
            };
        };

        //Requires an argument to specify which operon's transitions are affected.
        $scope.removeInTran = function(opeNum){
            if($scope.inputTransitions[opeNum].length > 1){
                var spliced = $scope.operons.length;
                $scope.inputTransitions[opeNum].splice(spliced - 1,1);
                $scope.inputSpecies[opeNum].splice(spliced - 1,1);
                $scope.outputSpecies[opeNum].splice(spliced -1,1);
            }
            else{
                $scope.errorMessage = "An Operon require at least one Input Transition.";
                $("#errorModal").modal("show");
            };
        };

        //Also require an argument due to $scope.inputSpecies's nested structure.
        $scope.removeInSpec = function(opeNum, inTranNum){
            if($scope.inputSpecies[opeNum][inTranNum].length > 1){
                var spliced = $scope.operons.length;
                $scope.inputSpecies[opeNum][inTranNum].splice(spliced - 1,1);
            }
            else{
                $scope.errorMessage = "An Input Transition require at least one Input Species.";
                $("#errorModal").modal("show");
            };
        };

        $scope.removeOutSpec = function(opeNum, inTranNum){
            if($scope.outputSpecies[opeNum][inTranNum].length > 1){
                var spliced = $scope.operons.length;
                $scope.outputSpecies[opeNum][inTranNum].splice(spliced - 1,1);
            }
            else{
                $scope.errorMessage = "An Input Transition require at least one Output Species.";
                $("#errorModal").modal("show");
            };
        };

        function initUpdate(){
            $scope.addPlasmid();
            $scope.addOperon($scope.plasmids.length - 1);
            $scope.addOperon($scope.plasmids.length - 1);
        };
        initUpdate();

        $scope.resetUpdate = function(){
            //resetting form arrays
            $scope.plasmids=[];
            $scope.operons=[];
            $scope.inputTransitions=[];
            $scope.inputSpecies=[];
            $scope.outputSpecies=[];
            //restarting forms
            initUpdate();
        };

        $scope.parseUpdatePlasmid = function(){
            for(var plasCount = 0; plasCount < $scope.plasmids.length; plasCount ++){
                //adding plasmid information.
                var plas = $scope.plasmids[plasCount].data;
                $scope.updateString = "Plasmid:" + plas.name.value + "," + plas.pubMedId.value + "\t";

                for(var opeCount = 0; opeCount < $scope.operons.length; opeCount ++){
                    //adding operon information.
                    var ope = $scope.operons[opeCount].data;
                    $scope.updateString += "Operon:" + ope.name.value + "," + ope.direction.value + "\t";

                    for(var inTranCount = 0; inTranCount < $scope.inputTransitions[opeCount].length; inTranCount ++){
                        //adding input transition information.
                        var inTran = $scope.inputTransitions[opeCount][inTranCount].data;
                        $scope.updateString += "InputTransition:" + inTran.logic.value + "\tPromoter:" + inTran.promoter.value + "\t";

                        for(var inSpecCount = 0; inSpecCount < $scope.inputSpecies[opeCount][inTranCount].length; inSpecCount++){
                            //adding input species data.
                            var inSpec = $scope.inputSpecies[opeCount][inTranCount][inSpecCount].data;
                            $scope.updateString += "InputSpecies:" + inSpec.name.value + "," + inSpec.type.value + "," + inSpec.repression.value + "\t";
                        };

                        for(var outSpecCount = 0; outSpecCount < $scope.outputSpecies[opeCount][inTranCount].length; outSpecCount++){
                            //adding output species data.
                            var outSpec = $scope.outputSpecies[opeCount][inTranCount][outSpecCount].data;
                            $scope.updateString += "OutputSpecies:" +outSpec.name.value + "," + outSpec.type.value + "\t";
                        };
                    };
                };
            };
            console.log($scope.updateString);
        };

        $scope.updateDatabase = function(){
            $scope.parseUpdatePlasmid();
            //GET function not fully finished yet.
//                updateGET();
        };

        $scope.redirect = function(){
            window.top.location = "../../contactPage.html";
        };

        //Sets name for the autcomplete.
        $scope.autoNames = ["and","not","or"];
        function autoComSet(){
            for (var nodeNum = 0; nodeNum < networkDefault.elements.nodes.length; nodeNum ++){
                var node = networkDefault.elements.nodes[nodeNum];
                if(node.classes === "species"){
                    $scope.autoNames.push(node.data.name);
                };
            };
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
                                autoComSet();
                                console.log($scope.autoNames);
                                console.log($scope.autoNames.length);
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
            alert("Submitting Command: "+commandString);
            if (commandString === "undefined = undefined undefined" || $scope.searchInput === undefined || $scope.searchInput === "" || $scope.searchOutput === undefined || $scope.searchOutput === "") {
                $scope.errorMessage ="Please enter a valid query. Check you inputs and output species, and make sure each species and logic is separated by a single space.";
                $("#errorModal").modal("show");
                angular.element('.loading').hide();
            }

            else {

                var data = {user: userID, command: 'query', data: commandString}; //package the input into a json file for submission to the server
                $.get("../../AuthenticationServlet", data, function(data) { //parameters are: servlet url, data, callback function
                    data = JSON.stringify(data).replace(/\\n/g, '', "").replace(/\\/g, '', "");
                    data = data.substr(1, data.length - 2);
                    alert(data);
                    networkData = JSON.parse(data);
                    angular.element('.loading').hide();

                    if (typeof networkData.error === "string") {
                        $scope.errorMessage = networkData.error;
                        $("#errorModal").modal("show");
                    }
                    else if (networkData.operonsId.length === 0 && $scope.BooleanTrue === undefined) {
                        $scope.errorMessage ='No circuits found. Please try searching for an Indirect Path (check the box marked "Indirect Path").';
                        $("#errorModal").modal("show");
                    }
                    else if (networkData.operonsId.length === 0 && $scope.BooleanTrue === "true") {
                        $scope.errorMessage = 'No circuits found in current database. Results may change as the SBiDer web grows.';
                        $("#errorModal").modal("show");
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
        };

        //The http GET request to the servlet that adds the user's entry to the SBiDer database.
        function updateGET() {
            //Sending the database entrie string as data.
            var commandString = $scope.updateString;

            //The update command needs to be written and inserted here.
            var data = {user: userID, command: 'uploadNew', data: commandString}; //package the input into a json file for submission to the server
            $.get("../../AuthenticationServlet", data, function(data) {
                //Using the error Modal to give an success alert.
                $scope.errorMessage = "Upload successful! Thank you for adding to the SBiDer web!";
                $("#errorModal").modal("show");

                //resetting the update form and string
                resetUpdate();
                $scope.updateString;
            });
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

        //example function for the user
        $scope.exampleSet = function(){
           $scope.searchInput = "lara and arac";
           $scope.searchOutput = "gfp";
           $('#myModal').modal('hide');
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
