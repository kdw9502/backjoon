n = int(input())
fibo = dict()
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1

var = 1000000007
def get_fibo(i):
    if i in fibo:
        return fibo[i]
    if i & 1 == 1:
        a = i // 2 + 1
        b = a -1
        fibo_a = get_fibo(a)
        fibo_b = get_fibo(b)
        result =  (fibo_a * fibo_a + fibo_b * fibo_b)  % var
        fibo[i] = result
        return result
    else:
        a = i // 2
        fibo_n = get_fibo(a)
        fibo_n_1 = get_fibo(a -1)
        add = (2*fibo_n_1 + fibo_n) % var
        result = add * fibo_n %var
        fibo[i] = result
        return result

print(get_fibo(n))
