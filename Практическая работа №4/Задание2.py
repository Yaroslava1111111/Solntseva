
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as c:
        reader = csv.DictReader(c, delimiter=",", quotechar="\n")
        row = list(reader)
    with open(OUTPUT_FILENAME, "w") as f:
        result = json.dump(row, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
