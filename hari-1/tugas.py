#NGUMPULIN SEMUA STATEMENT DI PYTHON

import random #dibutuhkan kalau mau pakai fungsi random
import string #kalau random string tanpa ini ga bisa jalan
import copy #untuk mengcopy suatu array

#random int
print("Ini adalah hasil random int: ",random.randint(1, 9))

#random str
print("Ini adalah hasil random str: ",random.choice('abcdefg'))

#random dari array
laugh = ["haha", "wkwk", "555"]
print("Ini adalah hasil random array: ",random.choice(laugh))

#mengcopy array laugh diatas
copy_laugh = copy.copy(laugh)
print("Ini adalah hasil pengcopyan array: ",copy_laugh)

#mengubah int ke str atau sebaliknya
textInt = 29
print(type(textInt))
print(type(str(textInt)))


#penggunaan keyword enter pakai \n
print("Hallo nama saya Deny \nSaya suka main Dota\nHero favorite saya adalah Invoker")

#pemanggilan array dari hinnga sampai
text = "Hallo nama saya Deny"
print(text[3]) #ini berarti array ke-3
print(text[6:9]) #array ke-6 sampai ke-9

#mengubah jadi upper dan lower
print(text.upper())
print(text.lower())

#untuk cek apa kata2 itu upper atau lower
print(text.isupper())
print(text.islower())
#ada juga isalpha, isalnum, isdecimal, istitle

#startswith, endswith. Mengecek apakah kata dimulai dan diakhir kata yang dicari
print(text.startswith('Hallo'))
print(text.endswith('Hallo'))

#join, menggabungkan kata dengan pemisah yang diinginkan
print(', '.join(['Hallo', 'Hai', 'Yoh'])) #menggabungkan dengan ,
print('#'.join(['Hallo', 'Hai', 'Yoh'])) #menggabungkan dengan #

#split, memisahkan kata dengan param yang diingkan
print(text.split()) #memisahkan ketika ketemu space
print(text.split('a')) #memisahkan ketika ketemu a
#bisa juga split \n atau # dll

#rjust, ljust, center.. Semacem text-align di css. right, left, center
print('Welcome'.center(26,'='))
print('Nasi'.ljust(20,'.')+'5.000'.rjust(6,' '))
print('Rendang'.ljust(20,'.')+'12.000'.rjust(6,' '))
print('Gule Kambing'.ljust(20,'.')+'25.000'.rjust(6,' '))

#input kaya scanf di C
print("\nPilih Menu Anda: ")
makanan = input()
print("\nMenu pilihan anda adalah "+makanan)

#if else
print("Apakah anda setuju? Y/N")
keputusan = input()
if keputusan == 'Y':
    print("Anda menyutujui bahwa makanan anda adalah "+makanan+"\n")
elif keputusan == 'N':
    print("Anda tidak setuju bahwa makanan anda adalah "+makanan+"\n")

#looping menggunakan while
spam = 0
while spam < 5:
    print('Mohon tunggu sebentar')
    spam = spam + 1

#break untuk menghentikan looping dalam sebuah kondisi
while True:
    print('\nKetik \'ABC\' untuk lanjut')
    name = input()
    if name == 'ABC':
        break
print('Terima Kasih Brow')

#continue kebalikan dari break
while True:
    print('Username: ')
    name = input()
    if name != 'Kompas':
        continue
    print('Password: ') 
    password = input()
    if password == '1234':
        break
print('Terima kasih sudah login')

#looping menggunakan for
for i in range(5):
    print(i)
for i in range(0, 10, 2): #kalau ini (mulai, berakhir, kelipatan)
    print(i)

#for di dalam dictonary
spam = {'name': 'Deny', 'age': 22}
for i in spam.items(): #items merujuk ke semua isi
    print(i)
for i in spam.values(): #values merujuk ke nilai/value
    print(i)
for i in spam.keys(): #keys merujuk ke variable
    print(i)



