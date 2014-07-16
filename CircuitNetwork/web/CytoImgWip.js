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
        'border-opacity': 0.5})
    .selector('.faded')
      .css({
        'opacity': 0.25,
        'text-opacity': 0
      }),
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
    name: 'cose',
    directed: true,
    padding: 10
  },
 ready: function(){
    window.cy = this;
    //Hides all img divs(secret class) on document load
    //currently hard-coded. This piece needs editing after database is up.
    $('.secret').hide(true);
    //get into position
    cy.$('#a').position({x: 100, y: 50});
    cy.$('#b').position({x: 300,y: 50});
    //hiding/showing div's that belong to a node
     cy.on('tap', 'node', function(){
        //retrieve clicked node's identity
        //this var allows functions to be directed towards clicked node only
        var identity = '#' + this.data('id');
        //Unit Test. Checks that var= node id 
        //alert(identity);
        //retrieve node's position
        var posit = this.position();
        //Unit Test. Checks that node position was grabed. 
        //alert(String(position.x + ", " + position.y));
        //changes the location of the div's node. Doesn't work atm
         $(identity).css({
            'left': posit.x,
            'top': posit.y
        });
        //toggles the html div & img w/ same id as clicked node
        $(identity).toggle();
    });
    //defunct way of getting images by creating divs. Possibly useful later.
    /*cy.on('click', 'node', function(){
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
    });*/
     
 }

});//cytoscape

});//on dom ready