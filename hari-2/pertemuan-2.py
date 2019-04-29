#ada open-> w untuk write, r untuk read
my_file = open('./file.txt','w') #write untuk txt
a,b,c = 1,2,3
info = {
    'name':'deny',
    'age': '22',
    'email':'deny@kompas.com'
}
to_do = ['wake','eat', 'code', 'repeat']

#my_file.write(a) #error karena ga bisa nulis int langsung. CUMA BISA STRING

#write untuk nulis ke dalam file
my_file.write("Hello world\n")
my_file.write('%s, %s, %s'%(a,b,c) + '\n' + info['name'] + '\n') #%s mirip di C
my_file.write(str(info)) #di str kan karena cuma bisa nulis string

#PENTING!!!
my_file.close() #USAHAKAN selalu ada ini setelah write, standar untuk write FILE

#dibawah ini untuk membaca file
read_file = open('./file.txt')
# file_content = read_file.read() #baca semua baris
# print(file_content)

#print(list(enumerate(read_file))[2]) #spesifik baris yang ingin ditampilkan

file_baris_1 = read_file.readline() #baca sebaris, baris berikutnya panggil fungsi yang sama = readline()
file_baris_2 = read_file.readline()
print(file_baris_1)
print(file_baris_2)

#masuk materi JSON
import json

json_data={
    'name': {
        'first':'Deny',
        'last':'Ramanda',
    },
    'job':['front end developer', 'web designer', '3D Modeling']
}

# my_json_string = json.dumps(json_data)
json.dump(json_data, open('./me.json','w')) #write json file
about_me = json.load(open('./me.json')) #ini untuk load json

print(about_me['name']['last'])