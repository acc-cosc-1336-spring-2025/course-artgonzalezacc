#main program
import files

def main():
    file_name = 'philosophers.txt'
    files.write_to_file(file_name)
    files.read_from_file(file_name)

main()