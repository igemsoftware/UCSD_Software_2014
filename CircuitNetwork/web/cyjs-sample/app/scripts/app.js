<<<<<<< HEAD
// Sample project for visualizing JSON files.
//
//   by Keiichiro Ono
//
'use strict';

angular.module('cyViewerApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute',
    'ngAnimate',
    'ui.bootstrap',
    'angular-underscore',
    'colorpicker.module',
    'angularSpinner'
])
    .config(function($routeProvider) {

        // Routing
        $routeProvider
            .when('/', {
                templateUrl: 'views/top.html',
                controller: 'TopCtrl'
            })
            .when('/gists/:id', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .when('/:url', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .otherwise({
                 redirectTo: '/'
            });
    });
=======
/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


>>>>>>> 9b2911c0a8bbd033ec9ba57aa44ae8360458298f
