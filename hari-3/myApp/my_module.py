def findMax(input_list):
    maxim = ''
    for i in input_list:
        if(isinstance(maxim, str)):#ini untuk cek str
            maxim = i
        if(i > maxim):#ini untuk cek int
            maxim = i
    return maxim
    
def findMin(input_list):
    minim = 0
    for i in input_list:
        if(i < minim):
            minim = i
    return minim
    
def add(a,b):
    return a+b