 

$(document).ready(function(){
  
    $('#ping').click(function(){
    alert("about to ping");
    $.get("AuthenticationServlet", {"command":"ping"},function(data){
        alert(data);
    });
});
});

