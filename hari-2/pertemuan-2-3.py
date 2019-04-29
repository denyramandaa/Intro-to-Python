#perulangan menggunakan for
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    
my_text = open('./file.txt').read().split('\n')

for line in my_text:
    print(line)