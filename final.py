import re

def process_file(input_file, output_file):
    # Define patterns for matching decimal numbers with optional commas and employee numbers
    decimal_pattern = re.compile(r'\d{1,3}(?:,\d{3})*\.\d+')
    employee_number_pattern = re.compile(r'\b\d{6}\b')
    
    # Initialize variables to hold data
    employee_data = {}
    current_employee = None

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Check for employee number
        match = employee_number_pattern.search(line)
        if match:
            # If there's a match, update the current employee number
            current_employee = match.group()
            if current_employee not in employee_data:
                employee_data[current_employee] = []

        # Find all decimal numbers in the line
        decimals = decimal_pattern.findall(line)

        # Only save decimals if an employee number is currently active
        if current_employee:
            employee_data[current_employee].extend(decimals)

    # Write results to output file
    with open(output_file, 'w') as out_file:
        for employee, decimals in employee_data.items():
            for decimal in decimals:
                # Format the decimal number with commas
                formatted_decimal = f"{float(decimal.replace(',', '')):,.2f}"
                out_file.write(f'{employee}, {formatted_decimal}\n')

# Example usage
input_file = 'Accrual Register.txt'  # Path to your input text file
output_file = 'employee_decimals.txt'  # Path to the output file

process_file(input_file, output_file)



