import csv

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = infile.readlines()
        writer = csv.writer(outfile)
        
        # Write the header
        writer.writerow(['Employee Number', 'Decimal Number'])
        
        for line in reader:
            # Strip newline characters and split by comma
            employee_number, decimal_number = line.strip().split(', ')
            # Write the row to the CSV file
            writer.writerow([employee_number, decimal_number])

# Example usage
input_file = 'employee_decimals.txt'  # Path to your input text file
output_file = 'employee_decimals.csv'  # Path to the output CSV file

convert_to_csv(input_file, output_file)
