def bilanganPrima(angkaAwal, angkaAkhir):
    prima = []
    for i in range(angkaAwal, angkaAkhir):
        prima.append(i)
        for a in range(2,i):
            if i%a == 0:
                if(i in prima):
                    prima.remove(i)

    return prima
            
print(bilanganPrima(4,20))