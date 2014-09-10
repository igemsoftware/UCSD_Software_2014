/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function(){
  $("#morePics").click(function(){
   $(".jumbotron").hide("slow", function(){
   $("#indvPics").load("ProfilesPage.html");
   });
  });
  
  $("#backBtn").click(function(){
     $("#hello").remove();
    $(".jumbotron").show("slow", function(){
         
     });
  });
  
  //log in 
  $("#signIn").click(function(){
      var email = $("#email").val();
      var password = $("#password").val();
      
      var validateMe = {user:email, password:password, command:"logMeIn"};
      alert(validateMe);
      $.get("AuthenticationServlet", validateMe, function(user){
          $("#logIn").remove(); 
          $("#userInfo").text(user);
          $("#password").val("");
      
                        
      });              
  });
  
  
  
});

  