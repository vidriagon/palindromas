# Proyecto: Verificador de Palíndromos en Python

## Descripción

Este proyecto implementa una función en Python para verificar si una cadena de texto es un palíndromo. Además, se incluyen pruebas automáticas utilizando la librería `unittest` para validar diferentes casos de uso.

---

## Estructura del Proyecto

```
tarea_python/
├── charfun.py          # Script principal con la función esPalindromo
├── test_charfun.py     # Pruebas unitarias usando unittest
└── README.md           # Documentación del proyecto
```

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework de pruebas:** `unittest` (incluido en la librería estándar de Python)

---

## Instrucciones de Uso

### Ejecutar el script principal:

```bash
python3 charfun.py
```

_Sigue las instrucciones en pantalla para introducir una frase y verificar si es un palíndromo._

### Ejecutar las pruebas unitarias:

```bash
python3 test_charfun.py
```

---

## Casos de Prueba Incluidos

- Palíndromos con espacios y mayúsculas:  
  `"Anita lava la tina"`
- Palíndromo simple:  
  `"radar"`
- No palíndromo:  
  `"Puesta en producción"`
- Cadena vacía:  
  `""` (se considera palíndromo)
- Caracteres no alfanuméricos:  
  `".-.?¿¡!¡¿?-."`
- Números como palíndromos:  
  `"12345654321"`

---

## Autor

- **Nombre:** Rafael Ruiz González  
- **Correo:** vidriagon.dev@gmail.com
