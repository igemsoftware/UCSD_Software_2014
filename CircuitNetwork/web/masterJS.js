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
       window.location.href="sampleHome.html"; 
    });
     $("#wiki").click(function(){
       window.location.href="Tester_Wiki.html"; 
    });
     $("#app").click(function(){
       window.location.href="AppPage.html"; 
    });
     $("#contact").click(function(){
       window.location.href="contactPage.html"; 
    });
    $("#signMe").click(function(){
       window.location.href="registrationPage.html"; 
    });
     $("#registerMe").click(function(){
       window.location.href="registrationPage.html"; 
    });
     
    
    //server functions
     $("#registration").click(function(){
                    alert("you are getting registered");
                    var userName= $("#userName").val();
                    var userPassword = $("#userPassword").val();
                    alert("userName:" + userName + "userPassword: " + userPassword);
                    var data= { user:userID, userName:userName, userPassword: userPassword, command:"registration"};
                    $.get("AuthenticationServlet", data, function(done){
                        $('#sayHello').text(done);
                        alert(done);
                    });
                    
                });
});