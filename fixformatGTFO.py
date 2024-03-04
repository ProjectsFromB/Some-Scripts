# Define the input and output file paths
input_file = "sampleGTFObins.txt"
output_file = "output_programs.txt"

# Initialize an empty list to store the modified lines
modified_lines = []

# Open the input file for reading
with open(input_file, "r") as f:
    # Read each line from the input file
    for line in f:
        # Split the line into words
        words = line.strip().split()
        
        # Check if there are at least two words on the line
        if len(words) >= 2:
            # Combine the first word with double quotes, add a colon and a space
            program_name = f'"{words[0]}":'
            
            # Combine the rest of the words in double quotes and join them with a space
            rest_of_line = ' '.join(f'"{word}"' for word in words[1:])
            
            # Combine the program name and the rest of the line with a comma
            modified_line = f'{program_name} "{rest_of_line}",'
            
            # Append the modified line to the list
            modified_lines.append(modified_line)

# Open the output file for writing
with open(output_file, "w") as f:
    # Write the modified lines to the output file
    for line in modified_lines:
        f.write(line + '\n')

print(f"Conversion complete. Output written to {output_file}")


