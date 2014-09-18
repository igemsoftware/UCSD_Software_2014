
'use strict';

angular.module('cyViewerApp')
    .controller('TopCtrl', function($scope, $rootScope, $http, $location) {

        $scope.advancedMenu = {show: false};

        $scope.visualize = function(networkUrl, styleUrl) {
            console.log('NET ================= ' + networkUrl);
            $rootScope.networkUrl = networkUrl;
            var encodedNetworkUrl = encodeURIComponent(networkUrl);

            // Validation


            if(!styleUrl) {
                console.log('STYLE UNDEF ================= ' + styleUrl);
            } else {
                $rootScope.encodedStyle = encodeURIComponent(styleUrl);
            }
            $location.path('/' + encodedNetworkUrl);
        };

        $scope.visualizeGist = function (gistId) {
            console.log('GIST NET2 ================= ' + gistId);
            $rootScope.gistId = gistId;
            $location.path('/gists/' + gistId);
        };

        $scope.toggleAdvancedMenu = function() {
            $scope.advancedMenu.show = !$scope.advancedMenu.show;
        };

    });

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



