import os
import sys
import shutil

def replace_bytes_in_file(file_path, old_bytes, new_bytes):
    # Convert byte sequences from hex strings to byte arrays
    old_bytes = bytes.fromhex(old_bytes)
    new_bytes = bytes.fromhex(new_bytes)

    # Read the file into memory
    with open(file_path, 'rb') as file:
        data = file.read()

    # Failsafe in case we can't find the bytes
    if old_bytes not in data:
        print("Cannot find bytes to patch, are you sure it isn't already applied?")
        return False

    # Find and replace the old byte sequence with the new one
    data = data.replace(old_bytes, new_bytes)

    # Write the modified data back to the file
    with open(file_path, 'wb') as file:
        file.write(data)

    return True

def is_path_valid(file_path):
        temp_path = file_path

        if not temp_path:
            print("You must enter a path!")
            return False

        if not os.path.exists(temp_path):
            print(f"The path \"{temp_path}\" does not exsist")
            return False
        else:
            if not os.path.exists(f"{temp_path}/Vampire/dlls/vampire.dll"):
                print("Could not find 'vampire.dll' in \"{temp_path}/Vampire/dlls/\", please check your path again.")
                return False

        return True

def get_path_from_user():
    path_verified = False

    while not path_verified:
        file_path = input("Please enter the full path to the game directory: ")

        path_verified = is_path_valid(file_path)

        if not path_verified:
            continue

        # if no errors, then path is valid
        break

    return file_path

def patch_bloodstrike_remove_stationary_requirement(file_path):
    old_bytes = '56 8B F1 8A 0D 24 9A 73 10 B0 01 84 C8 75 2C 0A C8 57 88 0D 24 9A 73 10'
    new_bytes = '56 8B F1 8A 0D 24 9A 73 10 B0 01 84 C8 5E C2 04 00 90 90 90 90 9A 73 10'

    # backup 'vampire.dll' just in case something goes wrong.
    if not os.path.exists(f"{file_path}.bak"):
        shutil.copy2(file_path, f"{file_path}.bak")
        print(f"Created backup of 'vampire.dll' at location \"{file_path}.bak\"")

    is_patch_success = replace_bytes_in_file(file_path, old_bytes, new_bytes)
    
    if not is_patch_success:
        print("Patch failed, nothing changed!")
        return False
    
    print("Sucessfully patched game!")
    return True

if __name__ == "__main__":

    # get path to game dir
    if len(sys.argv) == 2:
        path_verified = is_path_valid(sys.argv[1])

        if not path_verified:
            exit(f"The path \"{sys.argv[1]}\" isn't valid.")

        file_path = sys.argv[1]
    else:
        file_path = get_path_from_user()

    # remove "/" at end of line, if needed.
    if file_path[-1] == "/":
       file_path = file_path[:-1]

    # point path to 'vampire.dll'
    file_path = f"{file_path}/Vampire/dlls/vampire.dll"

    # do the patch
    is_patch_success = patch_bloodstrike_remove_stationary_requirement(file_path)

    if not is_patch_success:
        exit("An error occured while attempting to patch 'vampire.dll'. Please ensure you have the basic Unofficial Patch, and haven't already applied the patch.")

