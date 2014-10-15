/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/*
 * This is a master javascript for the website
 */

$(document).ready(function(){
    //redirecting to other pages 
    $("#home").click(function(){
       window.location.href="index.html"; 
    });
     $("#about").click(function(){
       window.location.href="AboutPage.html"; 
    });
     $("#documentation").click(function(){
       window.location.href="TutorialPage.html"; 
    });
     $("#wiki").click(function(){
       window.open("http://2014.igem.org/Team:UCSD_Software", '_blank'); 
    });
     $("#app").click(function(){
       window.location.href="AppPage.html"; 
    });
    $("#thumbThree").click(function(){
       window.location.href="AppPage.html"; 
    });
    
     $("#contact").click(function(){
       window.location.href="contactPage.html"; 
    });
    
     
    
    
    
     
     
    //server functions
     
                    
           
      
       //contactUs page
       
       $('#submitContact').click(function(){
       alert("your information is getting sent");
       var name = $("#name").val();
       var email = $('#email').val();
       var affiliation = $('#affiliation').val();
       var message = $('#message').val();
       var data = {name:name, email:email, affiliation:affiliation,message: message, command:"contactUs"}; 
       $.get("AuthenticationServlet", data, function(done){
           alert(done);
       });
         
     });  
     
       $('#register').click(function(){
           alert("clicked");
          var name = $("#newName").val();
          var email = $("#newPassword").val();
          alert(name + email);
          var data = {name: name, email:email, command:"register"};
          $.get("AuthenticationServlet", data, function(done){
              alert(done);
              
          });
       });
       
      
                
              

});  
