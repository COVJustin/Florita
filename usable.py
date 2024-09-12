import re

def extract_sixth_decimal(file_path, output_file):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    decimal_numbers = []
    
    # Regular expression to match decimal numbers
    decimal_pattern = re.compile(r'\d*\.\d+')
    
    for line in lines:
        # Find all decimal numbers in the line
        decimals = decimal_pattern.findall(line)
        
        # Check if there are at least 6 decimal numbers
        if len(decimals) >= 6:
            # Append the 6th decimal number (index 5) to the list
            decimal_numbers.append(decimals[5])
    
    # Write the results to the output file
    with open(output_file, 'w') as out_file:
        for number in decimal_numbers:
            out_file.write(f'{number}\n')

# Example usage
extract_sixth_decimal('Accrual Register.txt', 'sixth_decimals.txt')






