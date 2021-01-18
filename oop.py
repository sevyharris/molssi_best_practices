class Molecule:
    def __init__(self, name, charge, symbols):
            self.name = name
            self.charge = charge
            self.symbols = symbols
            # self._num_atoms = len(symbols)

    def __str__(self):
        return f'name: {self.name}\ncharge: {self.charge}\nsymbol: {self.symbols}'

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = symbols
        self._num_atoms = len(symbols)

    def my_algorithm(self, parameter_list):
        # first stage
        self._first_stage(parameter_list)
        # second stage
        self._second_stage(parameter_list)
        # third stage
        self._third_stage(parameter_list)
        pass

    def _first_stage(self, parameter_list):
        pass

    def _second_stage(self, parameter_list):
        pass

    def _third_stage(self, parameter_list):
        pass


water = Molecule('water', 0.0, ['O', 'H', 'H'])
print(water)
print(water._num_atoms)
water.symbols = ['O', 'O', 'H', 'H']
print(water)
print(water._num_atoms)
