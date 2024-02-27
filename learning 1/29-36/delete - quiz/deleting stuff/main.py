import os, shutil
path = 'test1.txt'
# deleting stuff


# deleting a file
try:
    os.remove(path)
    print("File deleted.")
except FileNotFoundError:
    print("File not found. One has been created.")
    open("test1.txt", "x")
except PermissionError:
    print("You do not have permission to delete that.")

# deleting a folder
path_folder = "empty_folder"

try:
    os.rmdir(path_folder)
    print("Folder deleted.")

except FileNotFoundError:
    print("Folder not found. one has been created for this.")
    os.mkdir(path_folder)
except PermissionError:
    print("You do not have permission to delete that.")
except OSError:
    print("You cannot delete that using this function. Shutil is needed.")

else:
    print(path_folder + " has been deleted.")

    # shutil.rmtree(path)  # removes a folder and all the files in it. Somewhat dangerous.