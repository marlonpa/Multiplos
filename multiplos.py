# Hallo los multiplos
def Multiplo(num, lim):
    print("multiplos")
    val_min = 0
    for a in range(1, (lim+1)):
        var = (num % a)
        if not var == 0:
            break
        # print(f'CONTEO {a}', flush=True)
        # time.sleep(1)
        if a >= lim:
            if var == 0:
                print(f'El numero positivo mas pequeño'
                      f' que es divisible por todos los numeros'
                      f' del 1 al 20 es: {num}', flush=True)
                val_min = num

    return val_min

# Funcion que calcula los numeros primos
def is_prime(n):
    print("primos")
    if n < 3 or n % 2 == 0:

        return n == 2
    else:
        return not any(n % i == 0 for i in range(3, int(n**0.5 + 2), 2))

# Funcion que factoriza
def prime_factors(n):
    # Saca los que no son primos, factoriza los que no son primos
    # los agrega a una lista, la recorremos, se verifica si hay repetidos en la lista
    # de los primos,se cuenta y lo eleva

    print("Factorizacion")
    i = 2
    factors = []
    while i * i <= n:

        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


lis_fac = []
lis_pri = []
limi = 20
for a in range(1, (limi+1)):
    if is_prime(a):
        lis_pri.append(a)
    else:
        lis_fac.append(prime_factors(a))


dic_val = {}
for primo in lis_pri:
    dic_val.update({primo: 1})
    for factores in lis_fac:
        if set(factores):
            if primo == set(factores).pop():
                new_ind = len(factores)
                old_ind = dic_val.get(primo)
                if new_ind > old_ind:
                    dic_val.update({primo: new_ind})


mul_fin = 1
for k in dic_val:
    mul_fin *= pow(k, dic_val.get(k))

Multiplo(mul_fin, limi)

