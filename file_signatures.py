import magic

def signatureof_file_identifications(pathof_file):
    
    # First, we will create a magic object
    magic_objects = magic.Magic()

    # this line helps to identifies the  file type on the basis of its file signature
    typeof_file = magic_objects.from_file(pathof_file)

    return typeof_file

if __name__ == "__main__":
     
    # This is the actual path of the file that we really want to identify
    pathof_file = 'sop.txt'

    # This will identifies and print the signature of file (such as ASCII text, PDF)
    signature_offile = signatureof_file_identifications(pathof_file)
    print(f"The signature for the file '{pathof_file}' is: {signature_offile}")