import argparse

# Function to filter lines and show progress
def filter_lines_and_show_progress(input_filename, output_filename, filter_string):
    total_lines = 0
    with open(input_filename, 'r') as input_file:
        # Get the total number of lines in the input file
        total_lines = sum(1 for line in input_file)
    
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        lines_processed = 0
        for line in input_file:
            # Show progress
            lines_processed += 1
            progress_percentage = (lines_processed / total_lines) * 100
            print(f'Progress: {progress_percentage:.2f}%\r', end='', flush=True)
            
            # Filter lines containing the filter string
            if filter_string in line:
                output_file.write(line)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Filter lines from a file based on a given string.')
parser.add_argument('--input_file', type=str, help='Input file name')
parser.add_argument('--output_file', type=str, help='Output file name')
parser.add_argument('--filter_string', type=str, help='String to filter lines')

args = parser.parse_args()

# Filter lines and show progress
filter_lines_and_show_progress(args.input_file, args.output_file, args.filter_string)

print("\nFiltering completed!")
