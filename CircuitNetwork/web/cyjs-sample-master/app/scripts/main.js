    'use strict';

angular.module('cyViewerApp')
    .controller('MainCtrl', function ($scope, $http) {
        
        //these files are are the uploaded Cytoscape object and style
        var NETWORK_FILE = 'data/gal.cyjs';
        var VISUAL_STYLE_FILE = 'data/galVS.json';

        var DEFAULT_VISUAL_STYLE = 'default';

        //these are empty arrays to be updated by 'GET' on line 98
        var networkData = {};
        var vs = {};

        // Application global objects
        $scope.networks = {};
        $scope.visualStyles = {};
        $scope.styleNames = [];
        $scope.networkNames = [];
        $scope.currentVS = DEFAULT_VISUAL_STYLE;

        console.log('Network rendering start...');

        // Basic settings for the Cytoscape window
        //this var "options" is passed into the get callback on line 103
        var options = {

            showOverlay: false,
            minZoom: 0.01,
            maxZoom: 200,

            layout: {
                name: 'preset'
            },

            ready: function () {
                var cy = this;
                //receives networkData from 'GET' on line 98
                cy.load(networkData.elements);
                //includes cytoscapejs as part of angular's scope
                $scope.cy = cy;
                $scope.cy.style().fromJson($scope.visualStyles[DEFAULT_VISUAL_STYLE].style).update();
                updateNetworkData(cy);
            }
        };

        //Allows for jquery upload of files by drag and drop.
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


        $scope.switchNetwork = function(networkName) {
            $scope.currentNetwork = networkName;
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


        $http({method: 'GET', url: VISUAL_STYLE_FILE}).
            success(function(data) {
                vs = data;
                $http({method: 'GET', url: NETWORK_FILE}).
                    success(function(data) {
                        networkData = data;
                        $('#network').cytoscape(options);
                        //init() function starts and formats cytoscape.js
                        init();
                    }).
                    error(function(data, status, headers, config) {
                    });
            }).
            error(function(data, status, headers, config) {
            });

        function init() {
            //Loads $scope.nodes as data loaded from server 
            $scope.nodes = networkData.elements.nodes;
            //Formats cytoscape.js object's style by calling function below
            initVisualStyleCombobox();
            // Set network name
            var networkName = networkData.data.name;
            $scope.currentNetwork = networkData.data.name;
            $scope.networks[networkName] = networkData;
            $scope.networkNames.push(networkName);
        }

        function initVisualStyleCombobox() {
            var styleNames = [];
            //iterates through server data and applies
            for (var i = 0; i < vs.length; i++) {
                var visualStyle = vs[i];
                var title = visualStyle.title;
                styleNames[i] = title;
                $scope.visualStyles[title] = visualStyle;
                $scope.styleNames[i] = title;
            }
        }
    });
