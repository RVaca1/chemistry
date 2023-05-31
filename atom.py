class Atom:


    '''Create Atom'''    

    symbol = ''

    atomic_number = 0

    electron_quantity = 0

    atomic_mass = 0

    electronegativity_value = 0

    electronic_configuration = ''

    def __init__(self, symbol = '', atomic_number = 0, atomic_mass = 0.000, electronegativity_value = 0.0, electronic_configuration = '') -> None:
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.electron_quantity = atomic_number
        self.atomic_mass = atomic_mass
        self.electronegativity_value = electronegativity_value
        self.electronic_configuration = electronic_configuration

    def show_atom_properties(self):
        