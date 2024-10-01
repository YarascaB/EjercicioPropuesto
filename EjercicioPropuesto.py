def obtener_numero_natural():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                raise ValueError("El número no es natural. Debe ser un número mayor que cero.")
            return numero
        except ValueError as ve:
            print(f"Error: {ve}. Intente de nuevo.")

def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
