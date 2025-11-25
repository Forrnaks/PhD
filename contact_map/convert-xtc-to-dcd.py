import MDAnalysis as mda

# Input XTC trajectory file
xtc_file = "psn.xtc"

# Output DCD trajectory file
dcd_file = "psn.dcd"

# Create a Universe object with the XTC trajectory
u = mda.Universe(xtc_file)

# Select all atoms in the system
ag = u.select_atoms('all')

# Create a DCD Writer
with mda.Writer(dcd_file, ag.n_atoms) as dcd_writer:
    # Iterate through the frames in the XTC trajectory and write to DCD
    for ts in u.trajectory:
        dcd_writer.write(ag)

print(f"Conversion complete. DCD trajectory saved to {dcd_file}")

