hello = "hello world!"
my_integer = 1
my_float = 1.0

#array variable
my_list = [1,'haha',3,4,5,6,7,8,9,10]

me = "my name is {} and im {} years old {}"

print(hello)
print("type of my_integer", type(my_integer)) #type itu untuk cek type data (int/str/float)
print("type of my_float", type(my_float))
print("my list", my_list)
print("my list ke 8", my_list[9])

print("my string", hello + str(my_list))

print('me', me.format('Deny', 26, 30))

about_me = {
    'name':'Deny',
    'age':21,
    'programming_language': ['python','js','java']
}

about_me_copy = { #untuk testing cmp
    'name':'Deny',
    'age':21,
    'programming_language': ['python','js','java']
}

print(about_me['name'])
print(me.format(about_me['name'], about_me['age'], about_me['programming_language'][0]))

fav_food = ['gado-gado', 'pecel']
fav_food_wife = ['burger', 'pizza']
fav_food.append('pisang goreng') #kaya di js
fav_food.insert(2,'kacang rebus') #append sesuai urutan yang diinginkan (urutan, data)

print(fav_food + fav_food_wife)

print('panjang dari fav_foo: ', len(fav_food)) #kalau di list itung jumlah array, kalau kata itung jumlah huruf

print('check something in list','pizza' in fav_food)

print(about_me)

about_me['status'] = 'married'
print(about_me)

del about_me['name'] #delete
print(about_me)

# NOTE: ga bisa cmp di python 3
print('compaare about_me', cmp(about_me, about_me_copy)) #semacam strcmp di C, untuk bandingan dengan result -1, 0, 1


my_tuple = (1, 'my_name', 3.0) #tipe data tuple tidak bisa diubah kaya mutable di C
print(my_tuple[0], my_tuple[1], my_tuple[2])

my_test = ['z', 'a', '0', '8', '6', 'c']
my_test.sort()
print(my_test)

