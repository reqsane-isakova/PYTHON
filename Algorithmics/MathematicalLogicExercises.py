#a, b, və c tam ədədləri verilir. Bu ədədlərdən ən azı biri müsbət və ən azı biri mənfidirsə çıxışa YES, əks halda NO verin.
a = int(input('A ededini daxil edin: '))
b = int(input('B ededini daxil edin: '))
c = int(input('C ededini daxil edin: '))
if a > 0:
  if b < 0 or c < 0:
      print('YES')
    else:
        print('NO')
elif b > 0:
    if a < 0 or c < 0:
        print('YES')
    else:
        print('NO')
elif c > 0:
    if a < 0 or b < 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

#Proqram üçrəqəmli N ədədi daxil edir. N ədədinin bütün rəqəmləri fərqlidirsə çıxışa YES, əks halda NO verin.
N = input("Ucreqemli ededi daxil edin: ")
if len(set(N)) == 3:
    print("YES")
else:
    print("NO")

#İki tam ədəd a və b arasında yerləşən tam ədədlərin sayını tapıb çıxarın.
a = int(input("Birinci ededi daxil edin: "))
b = int(input("İkinci ededi daxil edin: "))
if a > b:
    count = a - b - 1
    if count < 0:
        count = 0
elif b > a:
    count = b - a - 1
    if count < 0:
        count = 0
else:
    count = 0
print(count)

#Dörd ədəd verilir. Onların arasında ən böyüyünü tapın.
a = int(input("Birinci ededi daxil edin: "))
b = int(input("İkinci ededi daxil edin: "))
c = int(input("Üçüncü ededi daxil edin: "))
d = int(input("Dördüncü ededi daxil edin: "))
print(max(a, b, c, d))

#"Hello, Python!" ismarıcını çap edin.
print("Hello World!")

#Verilmiş ölçülərinə görə düzbucaqlı paralelepipedin səthinin sahəsini və həcmini hesablayın.
a = int(input("a-nin uzunluğunu daxil edin: "))
b = int(input("b-nin uzunluğunu daxil edin: "))
c = int(input("c-nin uzunluğunu daxil edin: "))
Hecm = a * b * c
Seth = 2 * (a*b + a*c + b*c)
print("Səth sahəsi:", Seth)
print("Həcmi:", Hecm)

#0dan 100e, qeder butun ededlerin cemi, rekursiya
#0-dan 100e qeder cut ededlerincemi
#0dan 100e qeder tek ededlerincemi
def butun(n):
    if n == 0:
        return 0
    else:
        return n + butun(n-1)
def cut(n):
    if n <= 0:
        return 0
    if n % 2 != 0:
        return cut(n-1)
    else:
        return n + cut(n-2)
def tek(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return tek(n-1)
    else:
        return n + tek(n-2)
n = 100
print("0-dan 100-e qeder butun ededlerin cemi:", butun(n))
print("0-dan 100-e qeder cut ededlerin cemi:", cut(n))
print("0-dan 100-e qeder tek ededlerin cemi:", tek(n-1))


