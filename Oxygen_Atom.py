from Atom import Atom

class Oxygen_Atom(Atom):

    def __init__(self):
        super().__init__(symbol='O', atomic_number= 8 , 
                         atomic_mass= 15.999 , electronegativity_value= 3.5 , 
                         electronic_configuration= '1s2 2s2 2p4')


O = Oxygen_Atom()

print(O)