#perulangan menggunakan while
# limit = 10
# i = 0
# while (limit > i):
#     print('ke ' + str(i))
#     i+=1
    
# my_name = 'Deny Ramanda'
# while my_name !='':
#     print(my_name)
#     my_name = my_name[1:]
    
# while True:
#     name = input('Masukan nama anda: ')
#     if name == 'stop':
#         break
#     age = input('Masukan umur anda: ')
#     print('Nama ada adalah %s dan anda berumur %s tahun.' %(name, age))



#LATIHAN
#bikin input data student terdiri dari nama, umur, hoby
#akan berhenti saat nama input stop
import json
my_data = {
    'students': []
}

while True:
    student = {}
    nama = input('Masukan nama: ')
    if nama == 'stop':
        break
    umur = input('Masukan umur: ')
    hoby = input('Masukan hobby: ')
    student['nama'] = nama
    student['umur'] = umur
    student['hobby'] = hoby
    my_data['students'].append(student)
    
fe = open('.\students.json', 'w')
json.dump(my_data, fe)
fe.close()