/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function(){
    $('#myCarousel').carousel({
    pause: true,
    interval: 6000
  });
  
});

var frameSrc = "/register";

$('#openBtn').click(function(){
    $('#myModal').on('show', function () {

        $('iframe').attr("src",frameSrc);
      
	});
    $('#myModal').modal({show:true})
});