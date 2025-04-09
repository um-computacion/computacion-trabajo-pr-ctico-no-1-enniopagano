def decimal_to_roman(numero):
    valores = [(1000, "M"), (900,  "CM"), (500,  "D"), (400,  "CD"), (100,  "C"), (90,   "XC"), (50,   "L"),
        (40,   "XL"), (10,   "X"), (9,    "IX"), (5,    "V"), (4,    "IV"), (1,    "I")
    ]

    resultado = ""
    for valor, romano in valores:
        while numero >= valor:
            resultado = resultado + romano
            numero = numero - valor
    return resultado

def main():
    decimal_humano = int(input('Ingrese un numero entre 1 y 3999: '))
    if not (1 <= decimal_humano <= 3999):
        print("El número debe estar entre 1 y 3999")
    else:
        romano = decimal_to_roman(decimal_humano)

        print(str(decimal_humano) + ' -> ' + str(romano))


if __name__ == '__main__':
    main()