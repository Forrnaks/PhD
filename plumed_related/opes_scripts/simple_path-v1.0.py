# A simple script for getting the ideal snapshots for a path from a given trajectory
# Based on the MC script for the same purpose (by Ladislav Hovan, Federico Comitani)
# By Ladislav Hovan

### Dependencies ###
import mdtraj as md
import numpy as np
import argparse
import sys
import os
### End of Dependencies ###

### Arguments ###
parser = argparse.ArgumentParser(description="Simple Path v1.0",
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=35))
parser.add_argument("filename", help="name of the intial full path (PDB) file", default="morph.pdb", nargs='?')
parser.add_argument("--metric", "-m", help="metric (rmsd/sdrmsd/drmsd/distance/scalar)", type=str, default="rmsd")
parser.add_argument("--sel", "-s", help="atoms selection for the protein (for rmsd, sdrmsd, drmsd)", type=str, 
                    default="(protein and not type H)")
parser.add_argument("--lig", "-lg", help="atoms selection for the ligand (for drmsd and distance)", type=str,
                    default="(not protein and not type H)")
parser.add_argument("--align", "-al", help="atoms selection for alignment (used by rmsd and distance)", 
                    type=str, default="(protein and name CA)")
parser.add_argument("--leng", "-le", help="ouptut path length (+-d_leng, default 2)", type=int, default=20)
parser.add_argument("--d_leng", "-dl", help="output path length tolerance", type=int, default=2)
parser.add_argument("--saveall", "-sa", help="save all the atoms rather than just the important selection", 
                    action='store_true')

args = parser.parse_args()

filename = args.filename
metric = args.metric
selection = args.sel
selection_ligand = args.lig
alignment = args.align
length_target = args.leng
length_tolerance = args.d_leng
### End of Arguments ###

### Functions ###
def load_rmsd_matrix(traj, selection, alignment):
    """Loads a matrix of RMSD values from a given trajectory - native mdtraj implementation"""
    
    top = traj.topology  # Get topology
    traj.superpose(traj, 0, top.select(alignment))  # Superpose to the first frame according to the selection
    matrix = np.empty((traj.n_frames, traj.n_frames))  # Get the RMSD matrix for all the frames
    for i in range(traj.n_frames):
        matrix[i] = md.rmsd(traj, traj, i, top.select(selection))  # Only selected atoms enter into calculation
    
    return matrix

def load_sdrmsd_matrix(traj, selection):
    """Simplified DRMSD implementation, where DRMSD is calculated only on the user's atom selection"""    

    top = traj.topology  # Get topology
    selection_indices = top.select(selection)
    
    pairs_temp = [] 
    # pair selection atoms
    for i in selection_indices:
        for j in selection_indices:
            if j > i:
                pairs_temp.append([i, j])
                
    pairs = np.array(pairs_temp)  # Convert to NumPy array for distance calculations
    
    # Calculate distances between pairs in the first frame
    frame_0_distances = md.compute_distances(traj[0], pairs)
    
    # Implement lower and upper cutoff
    relevant_pairs = np.array([pairs[i] for i in range(0, frame_0_distances[0].size) if 
                               0.8 >= frame_0_distances[0][i] >= 0.4])
    frame_distances = md.compute_distances(traj, relevant_pairs)
    
    # Calculate DRMSD between every pair of frames
    matrix = np.empty((traj.n_frames, traj.n_frames))
    for i in range(0, traj.n_frames):
        for j in range(i, traj.n_frames):
            if i == j:
                matrix[i][j] = 0
            else:
                temp_value = np.sum(np.power(frame_distances[i] - frame_distances[j], 2))
                matrix[i][j] = temp_value
                matrix[j][i] = temp_value
    
    # Normalise by number of pairs
    matrix = np.divide(matrix, len(relevant_pairs))
    
    return matrix

def load_drmsd_matrix(traj, selection_protein, selection_ligand):
    """Loads a matrix of DRMSD values from a given trajectory - not a native mdtraj implementation"""
    
    path_selection=[]
    top = traj.topology  # Get topology
    protein_indices = top.select(selection_protein)
    ligand_indices = top.select(selection_ligand)  # Select heavy atoms of the ligand
    
    # Select protein heavy atoms relatively close to the ligand in the first frame
    close_protein = md.compute_neighbors(traj[0], 0.5, ligand_indices, protein_indices)
    
    # Add all the atoms to path selection
    for i in ligand_indices:
        path_selection.append(i)
    for i in close_protein[0]:
        path_selection.append(i)
    
    # Pair the ligand and protein atoms up
    pairs_temp = [] 
    for i in ligand_indices:
        for j in close_protein[0]:
            pairs_temp.append([i, j])
    
    # Also pair protein atoms
    for i in close_protein[0]:
        for j in close_protein[0]:
            if j > i:
                pairs_temp.append([i, j])
                
    # And also ligand atoms, to comply with DRMSD in Plumed
    for i in ligand_indices:
        for j in ligand_indices:
            if j > i:
                pairs_temp.append([i, j])
                
    pairs = np.array(pairs_temp)  # Convert to NumPy array for distance calculations
    
    # Calculate distances between pairs in the first frame
    frame_0_distances = md.compute_distances(traj[0], pairs)
    
    # Implement lower and upper cutoff
    relevant_pairs = np.array([pairs[i] for i in range(0, frame_0_distances[0].size) if 
                               0.8 >= frame_0_distances[0][i] >= 0.4])
    frame_distances = md.compute_distances(traj, relevant_pairs)
    
    # Calculate DRMSD between every pair of frames
    matrix = np.empty((traj.n_frames, traj.n_frames))
    for i in range(0, traj.n_frames):
        for j in range(i, traj.n_frames):
            if i == j:
                matrix[i][j] = 0
            else:
                temp_value = np.sum(np.power(frame_distances[i] - frame_distances[j], 2))
                matrix[i][j] = temp_value
                matrix[j][i] = temp_value
    
    # Normalise by number of pairs
    matrix = np.divide(matrix, len(relevant_pairs))
    
    return matrix

def load_distance_matrix(traj, selection_ligand, alignment):
    """Loads a matrix of distance values from a given trajectory - not a native mdtraj implementation"""
    
    top = traj.topology  # Get topology
    
    # Superpose the trajectory according to the selection
    traj.superpose(traj, 0, top.select(alignment))
    
    # Select only ligand
    traj_ligand = traj.atom_slice(top.select(selection_ligand))
    
    # Calculate center of mass for ligand in every frame
    coms = md.compute_center_of_mass(traj_ligand)
    
    # Calculate distance between COMs for every pair of frames
    matrix = np.empty((traj_ligand.n_frames, traj_ligand.n_frames))
    for i in range(0, traj_ligand.n_frames):
        for j in range(i, traj_ligand.n_frames):
            if i == j:
                matrix[i][j] = 0
            else:
                temp_value = np.sqrt(np.sum(np.power(coms[i] - coms[j], 2)))
                matrix[i][j] = temp_value
                matrix[j][i] = temp_value
                
    return matrix

def backup_procedure(filename):
    """Backs up a file with a given filename"""
    
    if os.path.isfile(filename):
        # Checks for previous backups
        backup_number = 0
        while os.path.isfile('bck%s_%s' % tuple([backup_number, filename])):
            backup_number += 1
        os.rename(filename, 'bck%s_%s' % tuple([backup_number, filename]))
        
def initialise_list(length_target, traj):
    """Takes the initial trajectory and makes an initial guess from equally spaced snapshots"""
    
    snapshots = []
    snapshots.append(0)
    
    for i in range(1, length_target - 1):
        snapshots.append(i * int(traj.n_frames) // (length_target - 1))
        
    snapshots.append(int(traj.n_frames) - 1)
        
    print ('Initial guess at a path: %s' % snapshots)
    
    return snapshots

def log_e_function(matrix, snapshots, minimal):
    """Natural log of the energy function for MC based on a matrix of metric values"""
    return np.log(e_function(matrix, snapshots, minimal))

def e_function(matrix, snapshots, minimal):
    """Energy function for MC based on a matrix of metric values"""
    
    # First neighbour contributions
    list1 = first_neighbour_contributions(matrix, snapshots)
    
    avg1 = np.average(list1)
    dev1 = np.std(list1)
    
    # Second neighbour contributions
    list2 = []
    for i in range(0, len(snapshots) - 2):
        list2.append(matrix[snapshots[i], snapshots[i+2]])
    
    avg2 = np.average(list2)
    dev2 = np.std(list2)
    
    # Return the function value
    return dev1 + 0.35 * avg1 + 0.1 * avg2 + 0.65 * dev2

def first_neighbour_contributions(matrix, snapshots):
    """Calculates the list of first neighbour contributions in the snapshots list"""
    
    list1 = []
    for i in range(0, len(snapshots) - 1):
        list1.append(matrix[snapshots[i], snapshots[i+1]])
        
    return list1

def add_output_line(file_output, minimal):
    """Adds information about a new best path to the output file"""
    
    file_output.write(' Path: ')
    file_output.write(str(minimal['snapshots']))
    file_output.write(' Energy: ')
    file_output.write(str(minimal['energy']))
    file_output.write(' Lambda: ')
    file_output.write(str(minimal['lambda']))
    file_output.write('\n')
    
def minimise_routine_simple(list_snapshots, matrix, first, last, minimal):
    """Minimises a single snapshot between two fixed ones"""
    
    # Current best energy and subset
    best_energy = log_e_function(matrix, list_snapshots, minimal)
    best_value = list_snapshots[first+1]
    
    # Try the possibilities
    for i in range(list_snapshots[first] + 1, list_snapshots[last] - 1):
        list_snapshots[first+1] = i
        current_energy = log_e_function(matrix, list_snapshots, minimal)
        
        # Update values if better
        if current_energy < best_energy:
            best_energy = current_energy
            best_value = i
        
    # Fill the best value
    list_snapshots[first+1] = best_value
    
def calculate_properties(matrix, snapshots):
    """Calculate all the properties of a single series of snapshots"""
    
    series = {}
    contrib_list = first_neighbour_contributions(matrix, snapshots)
    series['avg'] = np.average(contrib_list)
    series['dev'] = np.std(contrib_list)
    series['snapshots'] = snapshots[:]
    series['energy'] = log_e_function(matrix, snapshots, series)
    series['lambda'] = 2.3 / series['avg']
    
    return series

def select_relevant_atoms(temp_name, output_name, selection, selection_ligand, alignment, metric):
    """Takes a temporary pdb file and outputs the relevant atoms into a new one, includes backup"""
    
    # Back up the output pdb file
    backup_procedure(output_name)
    
    # Open temp file and get all the lines
    file_traj_temp = open(temp_name,'r')
    lines_traj = file_traj_temp.readlines()
    
    # Open output file
    file_traj = open(output_name,'w')
    
    # Concatenate both selections, create complete selection too
    meta_selection = np.concatenate((selection_ligand, selection))
    total_selection = np.concatenate((meta_selection, alignment))
    
    # Add all the required lines
    for i in lines_traj:  
        words_list = i.split()  # Get individual words
        if (words_list[0] != 'REMARK') and (words_list[0] != 'END'):
            if (words_list[0] == 'ATOM' or words_list[0] == 'HETATM'):
                # Need to account for the fact that pdb starts from 1 but array from 0
                # Also TER between protein and ligand will change the offset again
                # Also change all chains to X - single block, maybe not necessary
                if words_list[3] == 'MOL' and ((int(words_list[1]) - 2) in total_selection):
                    atom_id = int(words_list[1]) - 1
                    id_str = str(atom_id)
                    temp1 = i[:(11-len(id_str))]
                    temp2 = i[11:21]
                    temp3 = i[22:56]
                    temp4 = i[66:]
                    designation = '1.00  0.00'
                    if (int(words_list[1]) - 2) not in alignment:
                        designation = '0' + designation[1:]
                    if (int(words_list[1]) - 2) in meta_selection:
                        designation = designation[:6] + '1' + designation[7:]
                    j = temp1 + id_str + temp2 + 'X' + temp3 + designation + temp4
                    file_traj.write(j)
                elif words_list [3] != 'MOL' and ((int(words_list[1]) - 1) in total_selection):
                    temp1 = i[:21]
                    temp2 = i[22:56]
                    temp3 = i[66:]
                    designation = '1.00  0.00'
                    if (int(words_list[1]) - 1) not in alignment:
                        designation = '0' + designation[1:]
                    if (int(words_list[1]) - 1) in meta_selection:
                        designation = designation[:6] + '1' + designation[7:]
                    j = temp1 + 'X' + temp2 + designation + temp3
                    file_traj.write(j)
            elif (words_list[0] == 'TER'):  
                if (words_list[2] == 'MOL'):  # Add the extra lines to make TER consistent, but not strictly needed
                    atom_id = int(words_list[1]) - 1
                    id_str = str(atom_id)
                    temp1 = i[:(11-len(id_str))]
                    temp2 = i[11:21]
                    temp3 = i[22:]
                    j = temp1 + id_str + temp2 + 'X' + temp3
                    file_traj.write(j)
                else:  # Delete the other TER to make it a single block of atoms
                    continue
            elif (words_list[0] == 'MODEL'):
                file_traj.write(i)
                # Extra remarks for cutoffs, loaded by Plumed
                if metric == 'drmsd' or metric == 'sdrmsd' or metric == 'mixed':  # Just in case for mixed
                    file_traj.write('REMARK LOWER_CUTOFF=0.4 UPPER_CUTOFF=0.8\n') 
            else:
                file_traj.write(i)  # Keep everything else, maybe deleting it would be better behaviour

def save_path(traj, minimal, selection, selection_ligand, alignment, metric, make_plumed=False):
    """Saves the relevant selection of the best path into a pdb file, also creates Plumed file for use with PATH"""
    
    print ('Saving the best path into a file')
    
    # Save a temporary pdb trajectory with all atoms
    traj_relevant = traj[minimal['snapshots']]
    traj_relevant.save('final_path_temp.pdb')
    
    # Now make a new file with only relevant atoms
    top = traj.topology
    select_relevant_atoms('final_path_temp.pdb', 'final_path.pdb', top.select(selection), top.select(selection_ligand),
                          top.select(alignment), metric)
    
    if make_plumed:
        if metric == 'rmsd':
            metric = 'OPTIMAL'  # Required by Plumed PATH, it shouldn't break anything
        
        # Open the Plumed file
        plumed_file = open('plumed_path.dat','w')

        # Path definition
        plumed_file.write('p1: PATH TYPE=%s REFERENCE=final_path.pdb LAMBDA=%s\n' % 
                          tuple([metric.upper(),'{0:.1f}'.format(minimal['lambda'])]))

        # Printing in the Plumed file
        plumed_file.write('PRINT ARG=p1.spath,p1.zpath STRIDE=1 FILE=colvar FMT=%8.4f')
        plumed_file.write('\n\nENDPLUMED')
        plumed_file.close()
        
def save_path_simple(traj, minimal):
    """The simplest possible way of saving the path, does nothing else and saves all the atoms"""
    
    print ('Saving the best path into a file')
    
    # Save a pdb trajectory with all atoms
    traj_relevant = traj[minimal['snapshots']]
    backup_procedure('final_path.pdb')
    traj_relevant.save('final_path.pdb')
### End of Functions ###

### Main script ###
# File backup
backup_procedure("best_paths.dat")

# Trajectory loading
traj = md.load(filename)
print('Imported %s frames with %s atoms in %s residues\n' % tuple([traj.n_frames, traj.n_atoms, traj.n_residues]))

# Calculating the length limits
length_min = length_target - length_tolerance
length_max = length_target + length_tolerance

# Checking sensibility of trajectory and limits
if length_max <= 2:
    raise Exception('Can only optimize for path lengths higher than two')
if length_min <= 2:
    print('Adjusting lower limit of path length to three')
    length_min = 3
if traj.n_frames < 3:
    raise Exception('Require at least three frames in the trajectory')
if traj.n_frames <= length_max:
    print('Adjusting upper limit of path length to the number of frames in the trajectory')
    length_max = traj.n_frames

# Matrix loading
if metric == 'rmsd':
    matrix = load_rmsd_matrix(traj, selection, alignment)
elif metric == 'sdrmsd':
    matrix = load_sdrmsd_matrix(traj, selection)
elif metric == 'drmsd':
    matrix = load_drmsd_matrix(traj, selection, selection_ligand)
elif metric == 'distance':
    matrix = load_distance_matrix(traj, alignment)
else:
    raise Exception('The metric %s has not been implemented' % metric)

# Output file for writing best paths after every iteration
file_output = open('best_paths.dat','w')

# The best snapshots across all possible lengths
meta_minimal = {}
meta_minimal['energy'] = np.inf

# Iterate over possible lengths
for curr_length in range(length_min, length_max+1):
    file_output.write('Length: %s\n' % str(curr_length))
    print ('Length: %s' % str(curr_length))
    
    # First guess at the snapshots
    snapshots = initialise_list(curr_length, traj)

    # Properties of current minimal energy snapshots
    minimal = calculate_properties(matrix, snapshots)

    # Log the first guess
    add_output_line(file_output, minimal)

    # Iterate sequential optimisation until convergence
    while (True):
        new_snapshots = snapshots[:]
        
        for i in range(2, len(new_snapshots)-1):
            minimise_routine_simple(new_snapshots, matrix, i-1, i+1, minimal)
            minimal = calculate_properties(matrix, new_snapshots)
            
        add_output_line(file_output, minimal)
        
        if (new_snapshots == snapshots):
            break
        
        snapshots = new_snapshots
    
    print('Optimized path: %s\n' % new_snapshots)
    file_output.write('\n')
            
    if (minimal['energy'] < meta_minimal['energy']):
        meta_minimal = minimal
        
# Print the information on the best path and save it
print('Best path obtained: %s' % meta_minimal['snapshots'])
print('Lambda for the best path: %s' % meta_minimal['lambda'])

if args.saveall:
    save_path_simple(traj, meta_minimal)
else:
    save_path(traj, meta_minimal, selection, selection_ligand, alignment, metric)
### End of Main script ###