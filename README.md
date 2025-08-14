### Hexlet tests and linter status:
[![Actions Status](https://github.com/jcastiblancoc/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/jcastiblancoc/python-project-174/actions)


[![Code Coverage](https://qlty.sh/gh/jcastiblancoc/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/jcastiblancoc/projects/python-project-174)

# Calculadora de Diferencias (gendiff)

[![asciicast](https://asciinema.org/a/30107266-8473-4cd3-a558-f0cac6e61533.svg)](https://asciinema.org/connect/30107266-8473-4cd3-a558-f0cac6e61533)

Herramienta en línea de comandos y librería de Python para comparar archivos JSON y mostrar sus diferencias de forma clara y ordenada.

## Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/jcastiblancoc/python-project-174.git
cd python-project-174


Instala las dependencias usando Poetry:

poetry install

Compara dos archivos JSON con el comando:

poetry run gendiff file1.json file2.json


Ejemplo:

file1.json

{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}


file2.json

{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}


Salida esperada:

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}


