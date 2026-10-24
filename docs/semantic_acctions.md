# Acciones Semánticas — PdL-JS

## Auxiliares
lex       := ∅
car       := ∅
num_linea := 1
long_cad  := 0

## Funciones
Leer() : Leer el siguiente carácter
Conc() : Concatenar el carácter actual
Ini() : Inicializar el lexema
Parse_Int(lex) : Modificar el tipo del lexema a número entero
Parse_Real(lex) : Modificar el tipo del lexema a número real
Gen_T(token, atributo) : Generar el token
Error(mensaje, numero_linea, lexema) : Registrar el error en el gestor de errores
NL : Incrementar el número de línea
TPR(lex): Consultar la tabla de palabras reservadas
TS(lex): Buscar o insertar el identificador en la tabla de símbolos y devolver su posición

**0 : 0**

```text
Si car = '\n':
    num_linea := num_linea + 1
Leer()
```

## Números enteros

**0 : 1**

```text
Ini()
Conc()
Leer()
```

**1 : 1**

```text
Conc()
Leer()
```

**1 : 100**

```text
valor := Parse_Int(lex)

Si valor <= 32767:
    Gen_T(integer, valor)
Si no:
    Error("Constante entera fuera de rango máximo (32767)", num_linea, lex)

```

## Números reales

**1 : 2**

```text
Conc()
Leer()
```

**2 : 3**

```text
Conc()
Leer()
```

**3 : 3**

```text
Conc()
Leer()
```

**3 : 101**

```text
valor := Parse_Real(lex)

Si valor <= 117549436.0:
    Gen_T(realnum, valor)
Si no:
    Error("Constante real fuera de rango máximo (117549436.0)", num_linea, lex)

```

## Identificadores y palabras reservadas

**0 : 4**

```text
Ini()
Conc()
Leer()
```

**4 : 4**

```text
Conc()
Leer()
```

**4 : 102**

```text
Si TPR(lex):
    Gen_T(TPR(lex), -)
Si no:
    posTS := TS(lex)
    Gen_T(id, posTS)

```

## Cadenas de caracteres

**0 : 5**

```text
Ini()
Conc()
long_cad := 0
Leer()
```

**5 : 5**

```text
Conc()
long_cad := long_cad + 1

Si car = '\n':
    num_linea := num_linea + 1

Leer()
```

**5 : 103**

```text
Conc()
Si long_cad <= 64:
    Gen_T(string, lex sin las comillas)
Si no:
    Error("Cadena mayor a 64 caracteres", num_linea, lex)

Leer()
```

## Comentarios multilínea

**0 : 6**

```text
Leer()
```

**6 : 7**

```text
Leer()
```

**7 : 7**

```text
Si car = '\n':
    num_linea := num_linea + 1
Leer()
```

**7 : 8**

```text
Leer()
```

**8 : 7**

```text
Si car = '\n':
    num_linea := num_linea + 1
Leer()
```

**8 : 8**

```text
Leer()
```

**8 : 104**

```text
Leer()
```

## Operadores

### Asignación e igualdad

**0 : 9**

```text
Ini()
Conc()
Leer()
```

**9 : 105**

```text
Gen_T(opeq, -)
Leer()
```

**9 : 106**

```text
Gen_T(assig, -)
```

### Operador lógico '|='

**0 : 10**

```text
Ini()
Conc()
Leer()
```

**10 : 107**

```text
Gen_T(logor, -)
Leer()
```

### Operadores de un carácter

**0 : 108**

```text
Gen_T(opsum, -)
Leer()
```

**0 : 109**

```text
Gen_T(opsub, -)
Leer()
```

**0 : 110**

```text
Gen_T(not, -)
Leer()
```

## Símbolos de agrupación y delimitadores

**0 : 111**

```text
Gen_T(parenclosed, -)
Leer()
```

**0 : 112**

```text
Gen_T(parenopen, -)
Leer()
```

**0 : 113**

```text
Gen_T(curlclosed, -)
Leer()
```

**0 : 114**

```text
Gen_T(curlopen, -)
Leer()
```

**0 : 115**

```text
Gen_T(semc, -)
Leer()
```

**0 : 116**

```text
Gen_T(comma, -)
Leer()
```
