class Molecule:

    lone_pairs = 0

    molecular_geometry_types = [ 'linear', 'trigonal', 'tetrahedral', 'trigonal bipyramidal', 'octahedral', 'seesaw', 't-shape', 'angular']

    def __init__(self, lone_pairs):

        self.lone_pairs = lone_pairs



