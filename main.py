from app.manager import Manager

def main():
    file_path= input("Enter path to file: ")
    manager = Manager(file_path)
    manager.print_file_data()
    
if __name__ == "__main__":
    main()