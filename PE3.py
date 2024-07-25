num=int(input("num"))

def prime_factors(num):
    factors=[]
    factor=2
    while num>2:
        if num%factor==0:
            factors.append(factor)
            num=num/factor
        else:
            factor = factor+1 
    return factors

a=prime_factors(num)
print(max(a))
