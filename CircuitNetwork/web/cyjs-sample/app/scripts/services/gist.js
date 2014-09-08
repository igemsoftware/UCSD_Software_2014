
/**
 *
 * Created by kono on 2014/06/26.
 */

'use strict';

angular.module('cyViewerApp')
    .factory('Gist', ['$resource', function ($resource) {
        return $resource('/gists/:gistId');
    }]
);

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */