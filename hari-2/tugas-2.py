import json

my_json = {
    'students': []
}
my_text = open('./tugas-2.csv').read().split('\n')
print(my_text)

field_name = my_text[0].split(',')
del my_text[0]

print(my_text, field_name)
for line in my_text:
    student = {}
    for idx, field in enumerate(line.split(',')):
        student[field_name[idx]] = field
    my_json['students'].append(student)

print(my_json)    
fe = open('./tugas-2-parsed.json', 'w')
json.dump(my_json, fe)