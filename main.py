from app.data_manager import Data_Manager

def main():
    file_path= input("Enter path to file: ")
    manager = Data_Manager(file_path)
    manager.print_file_data()
    
if __name__ == "__main__":
    main()