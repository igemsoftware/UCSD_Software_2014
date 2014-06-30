$(function(){ // on dom ready

$('#cy').cytoscape({
  style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'content': 'data(name)',
        'text-valign': 'center',
        'color': 'white',
        'text-outline-width': 2,
        //'text-outline-color': '#888',
        'width': 'mapData(weight, 30, 80, 20, 50)',
        'height': 'mapData(height, 0, 200, 10, 45)',
        'border-color': '#fff',
        //'text-outline-color': 'data(faveColor)',
        'background-color': 'data(faveColor)'
      })
    .selector('edge')
      .css({
        'target-arrow-shape': 'triangle'
      })
    .selector(':selected')
      .css({
        'background-color': 'black',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black'
      })
    .selector('.faded')
      .css({
        'opacity': 0.25,
        'text-opacity': 0
      }),
     
    
  elements: {
    nodes: [
      { data: { id: 'home', name: 'Home', weight: 90, height: 180, faveColor: '#6FB1FC' }},
      { data: { id: 'about', name: 'About', weight: 70, height: 150, faveColor: '#F5A45D' } },
      { data: { id: 'notebook', name: 'Notebook', weight: 70, height: 150, faveColor: '#F5A45D' } },
      { data: { id: 'project', name: 'Project', weight: 70, height: 150, faveColor: '#F5A45D' } },
      { data: { id: 'safety', name: 'Safety', weight: 70, height: 150, faveColor: '#F5A45D' } },
      { data: { id: 'about1', name: 'The Team', weight: 48, height: 160 } },
      { data: { id: 'about2', name: 'Team Profile', weight: 48, height: 160 } },
      { data: { id: 'about3', name: 'iGEM', weight: 48, height: 160 } },
      { data: { id: 'about4', name: 'Sponsors', weight: 48, height: 160 } },
      { data: { id: 'about5', name: 'Attributions', weight: 48, height: 160 } },
      { data: { id: 'project1', name: 'Network', weight: 48, height: 160 } },
      { data: { id: 'project2', name: 'Overview', weight: 48, height: 160 } },
      { data: { id: 'project3', name: 'Achievements', weight: 48, height: 160 } },
      { data: { id: 'project4', name: 'Collaboration', weight: 48, height: 160 } },
      { data: { id: 'project5', name: 'Experiments', weight: 48, height: 160 } },
      { data: { id: 'notebook1', name: 'Methods', weight: 48, height: 160 } },
      { data: { id: 'notebook2', name: 'Notes', weight: 48, height: 160 } },
      { data: { id: 'safety1', name: 'Ethics', weight: 48, height: 160 } },
      { data: { id: 'safety2', name: 'Human Practices', weight: 48, height: 160 } }
    ],
    edges: [
      { data: { source: 'home', target: 'about' } },
      { data: { source: 'home', target: 'project' } },
      { data: { source: 'home', target: 'notebook' } },
      { data: { source: 'home', target: 'safety' } },
      { data: { source: 'about', target: 'home' } },
      { data: { source: 'about', target: 'about1' } },
      { data: { source: 'about', target: 'about2' } },
      { data: { source: 'about', target: 'about3' } },
      { data: { source: 'about', target: 'about4' } },
      { data: { source: 'about', target: 'about5' } },
      { data: { source: 'project', target: 'home' } },
      { data: { source: 'project', target: 'project1' } },
      { data: { source: 'project', target: 'project2' } },
      { data: { source: 'project', target: 'project3' } },
      { data: { source: 'project', target: 'project4' } },
      { data: { source: 'project', target: 'project5' } },
      { data: { source: 'notebook', target: 'home' } },
      { data: { source: 'notebook', target: 'notebook1' } },
      { data: { source: 'notebook', target: 'notebook2' } },
      { data: { source: 'safety', target: 'home' } },
      { data: { source: 'safety', target: 'safety1' } },
      { data: { source: 'safety', target: 'safety2' } },
    ]
  },
  
  layout: {
    name: 'grid',
    padding: 10
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
    
    cy.on('tap', 'node', function(e){
      var node = e.cyTarget; 
      var neighborhood = node.neighborhood().add(node);
      
      cy.elements().addClass('faded');
      neighborhood.removeClass('faded');
    });
    
    cy.on('tap', function(e){
      if( e.cyTarget === cy ){
        cy.elements().removeClass('faded');
      }
    });
  }
});

}); // on dom ready