
# ===================
# フィボナッチ数列
# ===================

def fibo(n): # nは数列の長さ

    f = []

    f0 = 1
    f.append(f0)
    f1 = 1
    f.append(f1)

    for i in range(n - 2):
        f2 = f0 + f1
        f.append(f2)

        f0 = f1
        f1 = f2
        
    return f


# ===================
# 平方数
# ===================

def squared(n): # nは数列の長さ

    sq = []

    for i in range(n):
        j = i + 1
        s = j ** 2

        sq.append(s)

    return sq

# ===================
# 立方数
# ===================

def cubed(n): # nは数列の長さ

    cu = []

    for i in range(n):
        j = i + 1
        s = j ** 3

        cu.append(s)

    return cu        


# ===================
# Prime Numbers
# (wiht methnod of diffinition)
# ===================

def primeNum(n): # nは数列の長さ

    primeNum = []
    num = 2

    while True:
        for i in range(2, num + 1):
            remainder = num % i
            if remainder == 0 and i < num:             
                break
            elif remainder == 0 and i == num:
                primeNum.append(num) 

        if len(primeNum) >= n:
            break
        
        num = num + 1

    return primeNum


# ===================
# Main
# ===================

n = 25

print()

print('【Squared Number】')
print(squared(n))
print()

print('【Cubed Number】')
print(cubed(n))
print()

print('【Prime Numbers】')
print(primeNum(n))
print()

print('【Fibonacci number】')
print(fibo(n))
print()




