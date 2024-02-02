def read_file(file_name):
    """Reads in a file."""
    with open(file_name, 'r') as file:
        contents = file.read()
    print(contents)
    return contents

def read_file_into_list(file_name):
    """Reads in a file and stores each line as an element in a list, preserving newlines."""
    with open(file_name, 'r') as file:
        lines = file.readlines() 
    return lines

def write_first_line_to_file(file_contents, output_filename):
    """Writes the first line of a string to a file, handling special cases."""
    first_line = file_contents.split('\n', 1)[0] + '\n'
    with open(output_filename, 'w') as file:
        file.write(first_line)

def read_even_numbered_lines(file_name):
    """Reads in the even numbered lines of a file, preserving newlines."""
    with open(file_name, 'r') as file:
        lines = [line for idx, line in enumerate(file, start=1) if idx % 2 == 0]
    return lines

def read_file_in_reverse(file_name):
    """Reads a file and returns a list of the lines in reverse order, preserving newlines."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
    reversed_lines = lines[::-1]
    print(reversed_lines)
    return reversed_lines

def main():
    file_name = "sampletext.txt" 
    file_contents = read_file(file_name)
    print("File contents:", file_contents)
    
    file_lines = read_file_into_list(file_name)
    print("File lines as a list:", file_lines)
    
    output_filename = "first_line.txt"
    write_first_line_to_file(file_contents, output_filename)
    print(f"First line written to {output_filename}")
    
    even_lines = read_even_numbered_lines(file_name)
    print("Even numbered lines:", even_lines)
    
    reversed_lines = read_file_in_reverse(file_name)
    print("File lines in reverse order:", reversed_lines)

if __name__ == "__main__":
    main()

