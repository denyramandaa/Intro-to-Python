# ag2 = 10

# while ag2 != 0:
#     age = input('Masukan umur anda: ')
#     age = int(age)
    
#     if age < 12:
#         print('child prize')
#     elif age >= 12 and age <50:
#         print('adult prize')
#     else:
#         print('senior prize')
        
#     ag2-=1
    
# def add(a,b):
#     return a+b
    
# c = add(1,2)

# print(c)

# def intersection(word_1, word_2):
#     inter_char = []
#     for char_1 in word_1:
#         if char_1 in word_2:
#             inter_char.append(char_1)
#     return inter_char
    
# hasil_1 = intersection('makan','mandi')
# hasil_2 = intersection('dkasdkasl','sdjshdakl')

# print(hasil_1)
# print(hasil_2)

#build in function
# a = abs(-1) #menjadikan bilangan ke positif
# print(a)

# numbers = [1,2,3,4,5,6]
# print(isinstance(numbers, dict)) #pengecekan data type

# #build in methods yang blabla.append()
# print(numbers.index(4))

def findMax(input_list):
    maxim = 0
    for i in input_list:
        if(i > maxim):
            maxim = i
    return maxim
    
my_list = [1,10,9,100,21, 150]

max_value = findMax(my_list)

print(max_value)