/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function(){
  $("#morePics").click(function(){
   $(".jumbotron").hide("slow", function(){
   $("#indvPics").load("Tester_Profiles.html");
   });
  });
  
  $("#backBtn").click(function(){
     $("#hello").remove();
    $(".jumbotron").show("slow", function(){
         
     });
  });
});

  



