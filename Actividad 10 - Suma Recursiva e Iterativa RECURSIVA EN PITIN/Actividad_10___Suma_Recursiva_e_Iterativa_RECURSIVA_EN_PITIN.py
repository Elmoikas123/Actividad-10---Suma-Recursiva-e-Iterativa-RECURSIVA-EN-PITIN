def sumaRecursiva(n):
    if n <= 9:
        return n
    else:
        return sumaRecursiva(n // 10) + n % 10

def main():
    numero = 12345
    resultado = sumaRecursiva(numero)
    print(f"La suma de los dígitos de {numero} es {resultado}")

if __name__ == "__main__":
    main()
