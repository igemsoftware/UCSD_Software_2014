$(function(){ // on dom ready

$('#cy').cytoscape({
     layout: {
    name: 'cose',
    directed: true,
    padding: 10
  },
  style: cytoscape.stylesheet()
    
  
    .selector('node')
      .css({
        'content': 'data(name)',
        'shape': 'data(faveShape)',
        'text-valign': 'center',
        'color': 'white',
        'text-outline-width': 2,
        'background-fit': 'contain',
        'background-repeat': 'no-repeat',
        'background-clip': 'node',
        'width': 55,
        'height': 55,
        'border-color': '#fff',
        'background-color': 'data(faveColor)',
        'z-index': '-1'
      })
    .selector('edge')
      .css({
        'target-arrow-shape': 'triangle',
        'source-arrow-shape': 'circle',
        'opacity': 0.666,
        'line-color': 'data(faveColor)',
        'source-arrow-color': 'data(faveColor)',
        'target-arrow-color': 'data(faveColor)',
        'width': 6//'mapData(strength, 70, 100, 2, 6)'
      })
      
      .selector('edge.questionable')
      .css({
        'line-style': 'dotted',
        'target-arrow-shape': 'diamond'
      })
      
    .selector(':selected')
      .css({
        'background-color': 'black',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black'
      })
      .selector('#home')
      .css({
        'background-image': 'igemlogo.png',
        'height': 100,
        'width': 100
      })
      
      .selector('#about3')
      .css({
        'z-index': -1
      })
      
      .selector('#byitself')
      .css({
        'background-image': 'http://www.shouduzp.com/wp-content/uploads/2014/06/belgium_flag_world_cup_2014_wallpaper.jpg',
        'height': 100,
        'width': 100
      })
      
    .selector('.faded')
      .css({
        'opacity': 0.25,
        'text-opacity': 0
      }),
      
     
    
  elements: {
    nodes: [
      { data: { id: 'home', name: '', weight: 90, height: 180, faveColor: '#6FB1FC', faveShape: 'star' }},
      { data: { id: 'about', name: 'About', weight: 70, height: 150, faveColor: '#F5A45D', faveShape: 'octagon' } },
      { data: { id: 'notebook', name: 'Notebook', weight: 70, height: 150, faveColor: '#F5A45D', faveShape: 'octagon' } },
      { data: { id: 'project', name: 'Project', weight: 70, height: 150, faveColor: '#F5A45D', faveShape: 'octagon' } },
      { data: { id: 'safety', name: 'Safety', weight: 70, height: 150, faveColor: '#F5A45D', faveShape: 'octagon' } },
      { data: { id: 'about1', name: 'The Team', weight: 48, height: 160, faveColor: '#86B342' } },
<<<<<<< HEAD
      { data: { id: 'about2', name: 'Team Profile', weight: 48, height: 160, faveColor: '#EDA1ED' } },
      { data: { id: 'about3', name: 'iGEM', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'about4', name: 'Sponsors', weight: 48, height: 160, faveColor: '#EDA1ED' } },
      { data: { id: 'about5', name: 'Attributions', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project1', name: 'Network', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project2', name: 'Overview', weight: 48, height: 160, faveColor: '#EDA1ED' } },
      { data: { id: 'project3', name: 'Achievements', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project4', name: 'Collaboration', weight: 48, height: 160, faveColor: '#EDA1ED' } },
=======
      { data: { id: 'about2', name: 'Team Profile', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'about3', name: 'iGEM', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'about4', name: 'Sponsors', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'about5', name: 'Attributions', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project1', name: 'Network', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project2', name: 'Overview', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project3', name: 'Achievements', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'project4', name: 'Collaboration', weight: 48, height: 160, faveColor: '#86B342' } },
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
      { data: { id: 'project5', name: 'Experiments', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'notebook1', name: 'Methods', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'notebook2', name: 'Notes', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'safety1', name: 'Ethics', weight: 48, height: 160, faveColor: '#86B342' } },
      { data: { id: 'safety2', name: 'Human Practices', weight: 48, height: 160, faveColor: '#86B342' } }
      //{ data: { id: 'byitself', name: '', weight: 48, height: 160 } }
    ],
    edges: [
      { data: { source: 'home', target: 'about', faveColor: 'F5A45D', strength: '90' } },
      { data: { source: 'home', target: 'project' } },
      { data: { source: 'home', target: 'notebook' } },
      { data: { source: 'home', target: 'safety' } },
      { data: { source: 'about', target: 'home' } },
      { data: { source: 'about', target: 'about1' , faveColor: '#EDA1ED'}, classes: 'questionable' },
<<<<<<< HEAD
      { data: { source: 'about', target: 'about2' , faveColor: '#86B342'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about3' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about4' , faveColor: '#86B342'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about5' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'home' } },
      { data: { source: 'project', target: 'project1' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project2' , faveColor: '#86B342'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project3' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project4' , faveColor: '#86B342'}, classes: 'questionable' },
=======
      { data: { source: 'about', target: 'about2' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about3' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about4' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'about', target: 'about5' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'home' } },
      { data: { source: 'project', target: 'project1' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project2' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project3' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'project', target: 'project4' , faveColor: '#EDA1ED'}, classes: 'questionable' },
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
      { data: { source: 'project', target: 'project5' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'notebook', target: 'home' } },
      { data: { source: 'notebook', target: 'notebook1' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'notebook', target: 'notebook2' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'safety', target: 'home' } },
      { data: { source: 'safety', target: 'safety1' , faveColor: '#EDA1ED'}, classes: 'questionable' },
      { data: { source: 'safety', target: 'safety2', faveColor: '#EDA1ED'}, classes: 'questionable' }
      
    ]
  },
  
  ready: function(){
    window.cy = this;
    
    // giddy up...
    cy.$('#home').position({
  x: 680,
  y: 308
}),
 
        cy.$('#about').position({
  x: 530,
  y: 220
}),
        cy.$('#about1').position({
  x: 430,
  y: 120
}),
        cy.$('#about2').position({
  x: 380,
  y: 170
}),
        cy.$('#about3').position({
  x: 330,
  y: 220
}),
        cy.$('#about4').position({
  x: 380,
  y: 270
}),
        cy.$('#about5').position({
  x: 430,
  y: 320
}),
        cy.$('#notebook').position({
  x: 530,
  y: 388
}),
         cy.$('#notebook1').position({
  x: 450,
  y: 488
}),
         cy.$('#notebook2').position({
  x: 610,
  y: 488
}),
        cy.$('#safety').position({
  x: 830,
  y: 388
}),
        cy.$('#safety1').position({
  x: 750,
  y: 488
}),
         cy.$('#safety2').position({
  x: 910,
  y: 488
}),
        cy.$('#project').position({
  x: 830,
  y: 220
}),
        
         cy.$('#project1').position({
  x: 930,
  y: 120
}),
        cy.$('#project2').position({
  x: 980,
  y: 170
}),
        cy.$('#project3').position({
  x: 1030,
  y: 220
}),
        cy.$('#project4').position({
  x: 980,
  y: 270
}),
        cy.$('#project5').position({
  x: 930,
  y: 320
}),
  
    
    cy.elements().unselectify();
    
<<<<<<< HEAD
    cy.on('tap', '#safety', function(e){
=======
    cy.on('mouseover', '#safety', function(e){
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
      //alert("bellooo");
      //$('#cy').hide();
      cy.elements().addClass('faded');
      $('#book').show();
      
<<<<<<< HEAD
      cy.on('tap', function(e){
=======
      cy.on('mouseup', function(e){
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
        $('#book').hide();
      }
    });
    });
    
<<<<<<< HEAD
    /*cy.on('tap', 'node', function(e){
=======
    cy.on('tap', 'node', function(e){
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
      var node = e.cyTarget; 
      var neighborhood = node.neighborhood().add(node);
      
      cy.elements().addClass('faded');
      neighborhood.removeClass('faded');
    });
    
    cy.on('tap', function(e){
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
      }
<<<<<<< HEAD
    });*/
=======
    });
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
  }
});
     $('#n1').click(function(){
           
      var node = cy.$('#about');
      var neighborhood = node.neighborhood().add(node);
      cy.elements().addClass('faded');
      neighborhood.removeClass('faded');
    cy.on('tap', function(e){
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
      }
    });
        
    });
    
    
    $('#n2').click(function(){
           
      var node = cy.$('#project');
      var neighborhood = node.neighborhood().add(node);
      cy.elements().addClass('faded');
      neighborhood.removeClass('faded');
    cy.on('tap', function(e){
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
      }
    });
        
    });
    
    $('#n3').click(function(){
           
      var node = cy.$('#notebook');
      var neighborhood = node.neighborhood().add(node);
      cy.elements().addClass('faded');
      neighborhood.removeClass('faded');
    cy.on('tap', function(e){
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
      }
    });
        
    });
    
   
        $(".header").click(function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
        $header.text(function () {
            //change text based on condition
            return $content.is(":visible") ? "Collapse" : "Expand";
        });
    });

<<<<<<< HEAD
});
    
=======
})
>>>>>>> ca08429aca1bcb3aa0d2a7a25068c30b2f2fa583
}); // on dom ready*/