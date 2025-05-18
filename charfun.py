# Función: esPalindromo
# Autor: Rafael Ruiz González
def esPalindromo(stringCheck):
    stringClean = ''.join(c for c in stringCheck if c.isalnum()).lower()
    return stringClean == stringClean[::-1]

if __name__ == "__main__":
    # Entrada del usuario y ejecución
    stringUser = input("Introduce una frase: ")
    if esPalindromo(stringUser):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")
