def bilanganPrima(angkaAwal, angkaAkhir):
    prima = []
    for i in range(angkaAwal, angkaAkhir):
        if(i%2 == 1 or i == 2):
            prima.append(i)
            
    return prima
            
print(bilanganPrima(1,10))

print(bilanganPrima(500,600))