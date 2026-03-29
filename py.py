#Open original file and read lines
with open('ABJH23.txt', 'r') as infile:
     lines = infile.readlines()
#Prepare output lines
output lines =output_lines.append ("RSID,CHROMOSOME, POSITION, RESULT\n") #Replace header

# Process remaining lines
for line in lines:
if line.startswith('#'):
continue
# Skip original header
parts = line.strip().split('\t')
# Split by tab
if len(parts) >= 4:output_lines.append(f"{parts[0]}, {parts[1]},{parts[2]},{parts[3]}\n")
# Write to CSV file
with open('original_file.csv', 'w') as outfile:
outfile.writelines(output_lines)
print(" Conversion complete. Saved as 'original_file.csv'.")