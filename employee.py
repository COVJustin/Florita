import re

# Define the input and output file paths
input_file_path = 'Accrual Register.txt'  # Change this to the path of your input file
output_file_path = 'output.txt'  # Change this to the path of your output file

def extract_fifth_decimal_number(line):
    # Find all decimal numbers in the line
    decimal_numbers = re.findall(r'\d+\.\d+', line)
    # Return the fifth decimal number if it exists, otherwise return an empty string
    return decimal_numbers[4] if len(decimal_numbers) >= 5 else ''

def process_file(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            fifth_decimal = extract_fifth_decimal_number(line)
            if fifth_decimal:
                outfile.write(fifth_decimal + '\n')

# Process the input file and write the output
process_file(input_file_path, output_file_path)

