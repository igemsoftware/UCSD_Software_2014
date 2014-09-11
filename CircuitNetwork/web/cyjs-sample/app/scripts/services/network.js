
/**
 * Created by kono on 2014/01/24.
 */

'use strict';

/**
 * Services that persists and retrieves TODOs from localStorage
 */
angular.module('cyViewerApp')
    .factory('Network', ['$resource', function ($resource) {
        return $resource('/view/:networkUrl');
    }]
);

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
