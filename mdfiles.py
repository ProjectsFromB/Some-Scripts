import os

# Define the directory containing the .md files
directory_path = "/home/legomyego/CPTS/cheatsheets/"

# Output file where the combined content will be written
output_file = "combined.md"

# List all .md files in the directory
md_files = [file for file in os.listdir(directory_path) if file.endswith(".md")]

# Sort the files by name if needed
md_files.sort()

# Combine the content of .md files
combined_content = ""
for md_file in md_files:
    with open(os.path.join(directory_path, md_file), "r") as file:
        combined_content += file.read() + "\n"

# Write the combined content to the output file
with open(output_file, "w") as output:
    output.write(combined_content)

print(f"Combined {len(md_files)} .md files into {output_file}")

