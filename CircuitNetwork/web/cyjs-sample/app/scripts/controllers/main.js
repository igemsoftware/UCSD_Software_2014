angular.module('cyViewerApp')
	
    .controller('MainCtrl', function ($scope, $http, $location, $routeParams, 
$window, Network, VisualStyles, Gist) {		

        'use strict';
        
        //these files are the temporary network
	var NETWORK_FILE = 'data/gal.cyjs'; 
        var visualStyleFile = 'data/galVS.json'; 
        
        var DEFAULT_VISUAL_STYLE_NAME = 'default';//'Solid';
        var PRESET_STYLE_FILE = encodeURIComponent('data/style.json');
        //these empty arrays are updated by the server for use by the cytoscape.js object.
        var networkData = {};
	var vs = {};
       
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
        $scope.cadState = {
            show: true
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
				angular.element('.loading').remove();
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
                //alert("moooooo");
                $('#book').show();
                //$('#752').addClass('highlighted');
                var id = event.cyTarget.id();
                $scope.selectedNodes[id] = event.cyTarget;
                $scope.selectedNodes[id].addClass('highlighted');
                updateFlag = true;
            });
            
             // Reset selection
            $scope.cy.on('unselect', 'node', function(event) {
		$('#book').hide();
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
        
        $scope.toggleCAD = function() {
            $scope.cadState.show = !$scope.cadState.show;
        };
        $scope.toggleModel = function() {
            $scope.modelState.show = !$scope.modelState.show;
        };

        $scope.fit = function() {
            $scope.cy.fit();
        };
        
        
        //Table button for controlling "selected" CAD
        $scope.cadSelect = function(id) {
            //clearing selected node
            $("img.CAD").each(function(){
                $(this).hide();
            });
            console.log("Clearing selection... ");
            //assigning new selected CAD
            $("#"+ id).show();
            console.log("New selected Cad is:" + id);
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
                        $('#network').cytoscape(options);
                        init();
                    }).
                    error(function(data, status, headers, config) {
                    });
            }).
            error(function(data, status, headers, config) {
            });

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

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

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
