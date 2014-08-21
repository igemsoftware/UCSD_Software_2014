
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

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


