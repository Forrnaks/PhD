# Read the contents of the text file into a list
with open("residue_interactions.txt", "r") as file:
    rows = file.readlines()

# Sort the rows based on the values in the last column
sorted_rows = sorted(rows, key=lambda row: float(row.split(":")[-1]))

# Write the sorted rows back to the text file
with open("residue_interactions_sorted.txt", "w") as file:
    file.writelines(sorted_rows)
