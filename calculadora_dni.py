LETRAS = [
	"T", "R", "W", "A", "G",
    "M", "Y", "F", "P", "D",
    "X", "B", "N", "J", "Z",
    "S", "Q", "V", "H", "L",
    "C", "K", "E"
]

def calculadora_dni(numero_dni):
    return LETRAS[numero_dni % len(LETRAS)]

if __name__ == "__main__":
    numero_dni = 12345678
    print(calculadora_dni(numero_dni))
