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
        $('#app').attr('disabled', 'disabled');
        $('#thumbThree').attr('disabled', 'disabled');
    //}
    
       
   
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
           alert("clicked");
          var name = $("#name").val();
          var email = $("#password").val();
          alert("name: " + name + "email: " + email);
          var data = {name: name, email:email, command:"login"};
          $.get("AuthenticationServlet", data, function(done){
              alert(done);
              var q = done;
              alert("q is " + q);
              //if(q.equals("Welcome")){
                  alert("hello" + q);
                 $('#app').removeAttr('disabled');
                 $('#loginModal').modal('hide');
                 //document.getElementById("#userInfo").value="Welcome!";
                 document.getElementById("log").style.visibility = 'hidden';
                 document.getElementById("logOut").style.visibility = 'visible';
             // }
              alert(done);
         
          });
       });
                
              

});  
