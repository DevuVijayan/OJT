"""def read_and_print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{file_name}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_name = 'devusallap.docx'
read_and_print_file(file_name)

"""
file_name = 'myfile.txt'

try:
    with open(file_name, 'r') as file:
       
        content = file.read()
   
    print('Content of example.txt:')
    print(content)

except FileNotFoundError:
    print(f'Error: {file_name} does not exist.')

except PermissionError:
    print(f'Error: You do not have permission to read {file_name}.')