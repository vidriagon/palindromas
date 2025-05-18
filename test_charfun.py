# Se importa librería unittest y la función esPalindromo
import unittest
from charfun import esPalindromo

# Se crea una clase TestCharfun que hereda de unittest.TestCase
class TestCharfun(unittest.TestCase):
    # Se define un método test_esPalindromo con varios casos de prueba
    def test_esPalindromo(self):
        self.assertTrue(esPalindromo("Anita lava la tina"))

    def test_palindromo_simple(self):
        """Verifica un caso simple de palíndromo."""
        self.assertTrue(esPalindromo("radar"))

    def test_no_palindromo(self):
        """Verifica que una cadena que no es palíndromo retorne False."""
        self.assertFalse(esPalindromo("Puesta en producción"))

    def test_cadena_vacia(self):
        """Verifica que una cadena vacía sea considerada palíndromo."""
        self.assertTrue(esPalindromo(""))

    def test_no_alfanumericos(self):
        """Verifica que solo considere caracteres alfanuméricos."""
        self.assertTrue(esPalindromo(".-.?¿¡!¡¿?-."))

    def test_solo_numeros(self):
        """Verifica que una cadena compuesta por números pueda ser palíndromo."""
        self.assertTrue(esPalindromo("12345654321"))

if __name__ == "__main__":
    unittest.main()
