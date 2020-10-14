n = int(input("Digite o valor de n: "))

odd = 1
i = 1

while i <= n:
    if odd % 2 != 0:
        print(odd)
        odd = odd + 1
        i = i + 1
    else:
        odd = odd + 1  
        