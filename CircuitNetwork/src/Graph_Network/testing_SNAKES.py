import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "nets")
from nets import *

def factory (cons, prod, init=[1, 2, 3]) :
    n = PetriNet("N")
    n.add_place(Place("src", init))
    n.add_place(Place("tgt", []))
    t = Transition("t")
    n.add_transition(t)
    n.add_input("src", "t", cons)
    n.add_output("tgt", "t", prod)
    return n, t, t.modes()
    
net, trans, modes = factory(Value(1), Value(0))
net.draw("value-0.png")
print modes
trans.fire(modes[0])
net.draw("value-1.png")