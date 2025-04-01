def modify_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()  

        modified_content = []
        for index, line in enumerate(content, start=1): 
            modified_line = f"{index}: {line.strip()} \n" 
            modified_content.append(modified_line)

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)  

        print(f"Successfully modified and wrote to {output_filename}")

    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied for {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = input("Enter the input filename: ")
output_file = "modified_" + input_file

modify_and_write_file(input_file, output_file)