import os

file_name = 'devu1.docx'

if os.path.exists(file_name):
   
    os.remove(file_name)
    print(f'{file_name} has been deleted.')
else:
    print(f'{file_name} does not exist.')













# import os
# def delete_file(file_name):
#     try:
#         if os.path.exists(file_name):
#             os.remove(file_name)
#             print(f"Successfully deleted {file_name}")
#         else:
#             print(f"The file {file_name} does not exist")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# file_name = 'abc.docx' 
# delete_file(file_name)
