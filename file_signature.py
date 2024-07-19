import magic

def identify_file_signature(file_path):
    # Create a magic object
    magic_obj = magic.Magic()

    # Get the file type based on its signature
    file_type = magic_obj.from_file(file_path)

    return file_type

if __name__ == "__main__":
    # path to the file you want to identify
    file_path = 'sop.txt'

    # Identify and print the file signature
    file_signature = identify_file_signature(file_path)
    print(f"The file signature for '{file_path}' is: {file_signature}")
