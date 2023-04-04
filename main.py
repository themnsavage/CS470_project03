from app.data_manager import Data_Manager

def main():
    file_path = 'data/data01.txt'
    json_file_path = 'data/data01.json'
    
    txt_manager = Data_Manager(file_path=file_path)
    json_manager = Data_Manager(json_file_path=json_file_path)
    
    print("txt manager data:")
    txt_manager.print_data()
    print("json manager data:")
    json_manager.print_data()
    
if __name__ == "__main__":
    main()