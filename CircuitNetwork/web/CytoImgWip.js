$(document).ready(function(){

$('#cy').cytoscape({
 style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'height': 80,
        'width': 80,
        'background-fit': 'cover',
        'border-color': '#000',
        'border-width': 3,
        'border-opacity': 0.5}),
 elements:{
   nodes:[
       {data: {id: 'a', name: 'a'} },
       {data: {id: 'b', name: 'b'} }
   ],
   edges:[
       {data: {source: 'a', target: 'b'} }
   ]
 },
  
 layout: {
    name: 'breadthfirst',
    directed: true,
    padding: 10
  },
 ready: function(){
    window.cy = this;
    
    cy.on('tap', 'node', function(){
        //adding div's on click centered at node
        var mouseX = event.pageX;
        var mouseY = event.pageY;
        $('#secret').remove();
        $('body').append(
                '<div id="secret">It\'s a \n\
<a href="https://www.youtube.com/watch?v=c8YNB9zVlHE">secret</a> \n\
to everybody!</div>'
        );
        $('#secret').css({
            'height':'50px', 
            'width':'100px', 
            'position':'relative',
            'top': mouseY - 25,
            'left': mouseX - 50,
            'background-color':'#B2B2CC'
        });
    });
     
 }

});//cytoscape

});//on dom ready