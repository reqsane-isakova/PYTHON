#1-dən 10-a qədər olan ədədlərin kvadratlarını çap edən proqram
i = 1
while i <= 10:
    kvadrat = i ** 2
    print(i,"^ 2 =",kvadrat)
    i += 1

#1-dən n-yə qədər olan cüt ədədləri çap et. n konsoldan daxil edilir.
n= int(input("Ededi daxil edin:"))
i =1;
while i<=n:
    if i%2==0:
     print( i)
    i+=1

#Mənfi ədəd daxil edilənə qədər ədədləri toplayan proqram yaz.
cem =0
while True:
    n=int(input("Ededi daxil edin:"))
    if n<0:
        break
    cem += n
print("Ededlerin cemi:", cem)

#1-dən 10-a qədər ədədləri yaz, amma 4 və 7-ni keç.
for i in range (1, 11):
   if  i!=4 and i!=7:
    print(i)

#İki ədədin cəmini, fərqini, hasilini, bölünməsini tapan funksiya yaz.
a=int(input("1-ci ededi daxil edin:"))
b=int(input("2-ci ededi daxil edin:"))
cem=a+b
ferq=a-b
hasil=a*b
if b!=0:
    nisbet=a/b
else:
    nisbet=("Nisbeti sifira bolmek olmaz!")
print("Cemi:", cem)
print("Ferqi", ferq)
print("Hasili:", hasil)
print("Nisbeti:", nisbet)

#Verilən ədədin cüt olub-olmadığını yoxlayan funksiya yaz.
n = int(input("Ededi daxil edin:"))
if n%2==0:
  print("Eded cemdir")
else:
  print("Eded tekdir")
