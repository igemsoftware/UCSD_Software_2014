
$(document).ready(function() {

    $('#ping').click(function() {
        var commandString = $('#command').val();
        var data = {command: commandString};
        $.get("AuthenticationServlet", data, function(data) {
            $('#output').text(data);
        });
    });


    $('#login').click(function(e) {
        var user = $('#user').val();
        var password = $('#password').val();
        alert("you are logged in");
        var data = {user: "some user", password: "password"};
        $.post("Demo_Site_Login.html", data, function(data) {
            //alert(data);
            alert("whats up");
        });
        //e.preventDefault();
    });

    $('#LogOut').click(function() {
        var LogOut = $('#LogOut').val();
        alert("about to log out");
        var data = {user: "", password: ""};
        $.post("AuthenticationServlet", data, function(data) {
            alert(data);
            alert("back");
        });
    });
});