def decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0

    for i in range(len(n)):
        decimal = int(n[i]) * 2 ** i
    return decimal

print(decimal("10110"))

def binario(n):
    binario= []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    return ''.join(binario)

print(binario(18))