

$(document).ready(function() {

    $('#ping').click(function() {
        var commandString = $('#command').val()
//        alert('about to execute: '+commandString);
        var data = {user: "some user", password: "password"}
        $.post("AuthenticationServlet", data, function(data) {

            alert(data);
        });
    });
});

