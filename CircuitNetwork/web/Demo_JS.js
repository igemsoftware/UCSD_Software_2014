
$(document).ready(function() {

    $('#ping').click(function() {
        var commandString = $('#command').val();
        alert('about to execute: '+commandString);
        var data = {user: "some user", password: "password"};
        $.post("AuthenticationServlet", data, function(data) {
            alert(data);
        });
    });
    
   
    $('#login').click(function(e){
      var user = $('#user').val();
      var password =$('#password').val();
      alert("you are logged in");
      var info = { key: "#user", value: "#password"};
      $.post("Demo_Site_Login.html",info, function(info){
          alert("whats up");
      });
      e.preventDefault();
    });
    
    $('#LogOut').click(function(){
       var LogOut =$('#LogOut').val();
       alert("about to log out");
       var done={user: "", password:""};
       $.post("AuthenticationServlet",done, function(done){
          alert(done);
          alert("back");
      });
    });
    
    $('#clickme').click(function(){
        var obtainFile = $('#filed').val();
        alert("file created");
        var information= {key: "hello"};
        $.post("AuthenticationServlet", information, function(information) {
            alert(information);
        });
        
    });
});
