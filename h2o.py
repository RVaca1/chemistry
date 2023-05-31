from Molecule import Molecule

class H2O(Molecule):

    def __init__(self):
        super().__init__(lone_pairs=4)

    molecular_geometry_types = ['angular']
    

a = H2O()

print(a.lone_pairs)

