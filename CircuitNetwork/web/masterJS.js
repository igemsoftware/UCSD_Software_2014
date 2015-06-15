/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/*@author valeriy
 * This is a master javascript for the website
 */

$(document).ready(function(){
    //window.onload = function() {
   // $('#appearModal').modal('show');
    
 
//};

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
    
     $("#tut").click(function(){
       window.location.href="Tutorial.html"; 
    });
    
    $("#thumbOne").click(function(){
       window.location.href="TutorialPage.html"; 
    });
     $("#wiki").click(function(){
       window.open("http://2014.igem.org/Team:UCSD_Software", '_blank'); 
    });
     $("#launch").click(function(){
       window.open("AppPage.html", '_blank'); 
    });
    
    $("#contact").click(function(){
       window.location.href="AppPage.html"; 
    });
     $("#signMe").click(function(){
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
    
     $("#wikiDocumentation").click(function(){
           window.open("http://2014.igem.org/Team:UCSD_Software/Documentation", '_blank'); 
    });
    
     $("#doc").click(function(){
           window.open("http://2014.igem.org/Team:UCSD_Software/Documentation", '_blank'); 
    });
      
       $("#githubLink ").click(function(){
           window.open("https://github.com/igemsoftware/UCSD-iGEM_2014", '_blank'); 
    });
      
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
     
      $('#sendMessage').click(function(){
       var name = $("#name").val();
       var subject = $("#subject").val();
       var email = $('#email').val();
       var message = $('#message').val();
       //alert("Name: " + name + "subject: " + subject +  "email: " + email + "msg: " + message);
       var data = {name:name, email:email, subject:subject,message: message, command:"contactUs"}; 
       $.get("AuthenticationServlet", data, function(done){
           var print = document.getElementById("outPut");
           alert("hello");
           $('#outPut').text(done);
           print.innerHTML = done; 
       });
         
     });  
     
   
     
     
});  
