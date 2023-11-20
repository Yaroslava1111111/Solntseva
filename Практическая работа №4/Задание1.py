import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_content = json.load(f)
    sum_ = sum([value["score"] * value["weight"] for value in json_content])
    return round(sum_, 3)
print(task())
