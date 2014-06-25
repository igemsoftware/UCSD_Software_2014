/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function() {
                $('#driver').click(function(event){
          $.post("AuthenticationServlet",{key: "someINFO"}, function( data ) {
                    alert(data);
                });       
    });
            });

$(document).ready(function () {
    //once we click the add button we see the variable inputted into the input 
    //will be added to the bottom of the list 
    
counter=0;
    $("#add").click(function (input) {
        var toAdd = $('input[name=variable]').val();
        $('.list').append('<ul class="item" id="'+counter+'"><li>' + toAdd + '</li></ul>');

       counter = counter +1;
        });

  
     $(document).on('click', '#subtractElement', function(){
       confirm("you will be removing the items");
      
      $(".item").remove();
      
     
 
        });
  
});