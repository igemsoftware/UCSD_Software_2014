/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function () {
    //once we click the add button we see the variable inputted into the input 
    //will be added to the buttom of the list 
    $("#button").click(function (input) {
        var toAdd = $('input[name=variable]').val();
        $('.list').append('<div class="item">' + toAdd + '</div>');
        alert("you have added an item");
        });
    
    //subtract the 2n variable from the list
    $('#subtractElement').on('click', '.item', function () {
        var i;
        for(i=0; i<input.length;i++){
            if(i%2===0){
          $(this).remove();
          confirm("The items 2n have been removed");
      }
          else{}
        }
        
    });

    });





