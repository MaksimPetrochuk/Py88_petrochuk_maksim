import json


def get_bottom_categories(_list):
    for obj in _list:
        try:
            if obj["Child"] is not None:
                get_bottom_categories(obj["Child"])
        except KeyError:
            bottom_categories.append(obj)


with open("categories.json", "r") as file:
    data = file.read()
top_categories = json.loads(data)["Table"]
bottom_categories = []
get_bottom_categories(top_categories)
with open("filtered_categories.json", "w") as file:
    json.dump(bottom_categories, file, indent=" ", ensure_ascii=False)
