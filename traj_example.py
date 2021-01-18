from md_factory import MDFactory
import mdtraj as mdt
import MDAnalysis as mda
import numpy as np
from mdtraj_adapter import MDTrajAdaptor
from mdanalysis_adapter import MDAnalysisAdaptor

"""
#trajectory = mdt.load_pdb('/home/moon/molssi_best_practices/protein.pdb')
#print(f'Center of mass: \n{mdt.compute_center_of_mass(trajectory)}')
#print(f'Radius of gyration:\n {mdt.compute_rg(trajectory)}')

universe = mda.Universe('/home/moon/molssi_best_practices/protein.pdb')

mass_by_frame = np.ndarray(shape=(len(universe.trajectory), 3))
for ts in universe.trajectory:
    mass_by_frame[ts.frame] = universe.atoms.center_of_mass(compound="segments")

print(f'Center of mass: \n{mass_by_frame}')
#print(f'Radius of gyration:\n {mdt.compute_rg(trajectory)}')
"""

md_toolkit = MDTrajAdaptor('/home/moon/molssi_best_practices/protein.pdb')
print(f'Center of mass: \n{md_toolkit.compute_center_of_mass()}')
print(f'Radius of gyration: \n{md_toolkit.compute_radius_of_gyration()}')

md_toolkit2 = MDAnalysisAdaptor('/home/moon/molssi_best_practices/protein.pdb')
print(f'Center of mass: \n{md_toolkit.compute_center_of_mass()}')
print(f'Radius of gyration: \n{md_toolkit.compute_radius_of_gyration()}')

# md_toolkit = MDFactory().md_factory('MDTraj', '/home/moon/molssi_best_practices/protein.pdb')

factory = MDFactory()
