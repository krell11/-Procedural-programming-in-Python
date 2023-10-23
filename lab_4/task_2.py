import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(cvs_file_path) -> None:
    with open(cvs_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    json_data = json.dumps(data, indent=4)
    with open(OUTPUT_FILENAME, 'w') as output_file:
        output_file.write(json_data)



if __name__ == '__main__':
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
