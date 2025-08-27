def karatsuba(x,y):
    
    if x < 10 or y < 10:
        return x*y
    
    m = (max(len(str(x)) , len(str(y))))//2

    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    bd = karatsuba(b , d)
    ab_vezes_cd = karatsuba(a + b , c + d)
    ac = karatsuba(a , c)

#  fórmula: ac * 10^2m     +           (ad+bc)        *  10^m     + bd
    return (ac * 10**(2*m) + ((ab_vezes_cd - ac - bd) * (10**m))) + bd

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

print("Usando Karatsuba(x,y) = " + str(karatsuba(x,y)))
print("Prova usando x * y = " + str(x *y))
