import csv
import json


#1
def count_word():
    with open('file.txt','r') as f:
        data = f.read()
        w = data.split()
        return len(w)


print(count_word())
#2

list_of_lists = [["Avi", "Cohen", 7, "Yisrael"], ["Sheri", "Levi", 27, "USA"], ["Salom", "dov", 72, "Anglend"]]

def write_to_file(lists):
    with open('people.csv', 'w', newline='') as people_file:
        writer = csv.writer(people_file)
        writer.writerows(lists)

write_to_file(list_of_lists)

#3
dicts={"name":"Alex","age":3,"city":"Jerusalem"}
def write_to_json_file(dicts):
    with open('people.json', 'w') as people_json_file:
        json.dump(dicts, people_json_file)
        return "people.json"

def read_from_json_file(json_file):
    with open('people.json', 'r') as people_json_file:
        dicts = json.load(people_json_file)
        return dicts

print(read_from_json_file(write_to_json_file))