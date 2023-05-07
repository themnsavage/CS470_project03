from app.data_generator import Data_Generator
import json


def main():
    generated_data = Data_Generator().generate_multiple_random_data_set(
        data_set_size=1000, max_items=10000, iterate_by=1
    )
    with open("data/generated_data/data.json", "w") as out_file:
        json.dump(generated_data, out_file, indent=4)


if __name__ == "__main__":
    main()
