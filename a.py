#Here it is clean and ready to copy:

# Open original file and read lines
with open('ABJH23.txt', 'r') as infile:
    lines = infile.readlines()

    # Prepare output lines with new header
    output_lines = []
    output_lines.append("RSID,CHROMOSOME,POSITION,RESULT\n")

    # Process remaining lines
    for line in lines:
        # Skip comment lines
            if line.startswith('#'):
                    continue

                        # Split by tab
                            parts = line.strip().split()

                                # Ensure the line has enough columns
                                    if len(parts) >= 4:
                                            output_lines.append(f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}\n")

                                            # Write to CSV file
                                            with open('original_file.csv', 'w') as outfile:
                                                outfile.writelines(output_lines)

                                                print("Conversion complete. Saved as 'original_file.csv'.")