/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/*@author valeriy
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
    $("#thumbOne").click(function(){
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
    
      $("#thumbTwo").click(function(){
           window.open("http://2014.igem.org/Team:UCSD_Software", '_blank'); 
    });
    $("#ucsd").click(function(){
           window.open("http://www.ucsd.edu", '_blank'); 
    });
       
    //var logged = false;
    //while(logged ===false){
        
    //}
    
       var loggedIn = false;
       if(loggedIn === false){
       $('#app').attr('disabled', 'disabled');
       $('#thumbThree').attr('disabled', 'disabled');
   }
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
          var name = $("#newName").val();
          var email = $("#newPassword").val();
          alert(name + email);
          var data = {name: name, email:email, command:"register"};
          $.get("AuthenticationServlet", data, function(done){
              alert(done);
              
          });
       });
       
       $('#login').click(function(){
          loggedIn=false; 
          var name = $("#name").val();
          var email = $("#password").val();
          
          var data = {name: name, email:email, command:"login"};
          $.get("AuthenticationServlet", data, function(done){
             
              var q = done;
               alert(done);
              if(q === "Welcome"){
                  loggedIn = true;
                  $('#loginModal').modal('hide');
                  loged(loggedIn);
            }
            
          });
          
       });
       
       function loged(loggedIn){
           if(loggedIn === true){
                 
                 $('#app').removeAttr('disabled');
                  document.getElementById("log").style.visibility = 'hidden';
                 document.getElementById("logOut").style.visibility = 'visible';}
          
       }
                
       $("#logOut").click(function(){
          loggedIn =false;
          document.getElementById("log").style.visibility = 'visible';
          document.getElementById("logOut").style.visibility = 'hidden'; 
          $('#app').attr('disabled', 'disabled');
          $('#thumbThree').attr('disabled', 'disabled');
       });       

});  
