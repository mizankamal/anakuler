#print ("python sangan simple")
#panjang = 10
#lebar = 5
#luas = panjang * lebar
#print (luas)

#bilangan prima
a = int(input("tampilkan nila dari:"))
z = int(input("sampai: "))
n = [ ]

for i in range (a, z):
    p = True
    for j in range (2, i-1):
        if (i%j == 0):
            p = False
        if (p==1):
            n += str(i)
print (n, end = " ")