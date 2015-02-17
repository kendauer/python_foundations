import os
def rename_files():
    file_list = os.listdir(r"/Users/Ken/Code/python_foundations/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/Users/Ken/Code/python_foundations/prank")
    print("Current Working Directory is "+os.getcwd())
    for file_name in file_list:
        print("Old name - "+file_name)
        os.rename(file_name, file_name.translate(None,"0123456789"))
        print("New name - "+file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    print("Current Working Directory is "+os.getcwd())
    
rename_files()
