import multiprocessing
def generar_numero(numero):
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero * 2 + 1
def main():
    numeros = list(range(1, 100001))  # Lista de números del 1 al 100000
    with multiprocessing.Pool() as pool:
        resultados = pool.map(generar_numero, numeros)

    print("Serie generada con 100000 posiciones:", resultados)
if __name__ == "__main__":
    main()
