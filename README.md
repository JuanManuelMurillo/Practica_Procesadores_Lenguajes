# Procesadores de Lenguajes — Práctica PdL-JS

### Autor: Juan Manuel Murillo López

#### 07/10/2026

Implementación incremental de un **Procesador de Lenguajes** para la asignatura **Procesadores de Lenguajes**, curso **2026/2027**.

El procesador tiene como objetivo analizar programas escritos en **PdL-JS**, realizando las fases de:

* Análisis léxico.
* Análisis sintáctico.
* Análisis semántico.
* Gestión de la Tabla de Símbolos.
* Gestión de errores.

El procesador recibe como entrada un fichero de código fuente y genera los ficheros necesarios para inspeccionar los resultados de las diferentes fases del análisis.

---

## Información de la práctica

| Campo                | Información               |
| -------------------- | ------------------------- |
| Asignatura           | Procesadores de Lenguajes |
| Curso                | 2026/2027                 |
| Lenguaje             | PdL-JS                    |
| Análisis sintáctico  | Ascendente LR             |
| Sentencia repetitiva | `while`                   |
| Operador especial    | `\|=`                     |
| Comentarios          | Bloque `/* */`            |
| Cadenas              | Comillas dobles `" "`     |

### Opciones asignadas al grupo

Esta implementación debe considerar específicamente las siguientes opciones asignadas al grupo:

#### Sentencia repetitiva: `while`

La sentencia `while` permite repetir un bloque de sentencias mientras una condición lógica sea verdadera:

```javascript
while (condición)
{
    cuerpo
}
```

La condición se evalúa antes de cada iteración y debe ser de tipo lógico.

#### ⬆Análisis sintáctico: LR

El análisis sintáctico se implementa mediante una técnica **ascendente LR**.

El procesador deberá generar el fichero `parse` con la secuencia de números de las reglas utilizadas durante el análisis sintáctico. Este fichero podrá utilizarse posteriormente con la herramienta **VASt** para visualizar el árbol sintáctico.

#### Operador de asignación lógica: `|=`

El operador:

```javascript
a |= b;
```

corresponde a una asignación con operación lógica OR y es equivalente conceptualmente a:

```javascript
a = a || b;
```

Los operadores de asignación con operación forman parte de las sentencias de asignación de PdL-JS. No pueden utilizarse como parte de expresiones.

#### Comentarios de bloque

El grupo implementará comentarios delimitados por:

```javascript
/*
    Comentario de bloque
*/
```

Los comentarios pueden ocupar varias líneas y pueden aparecer en cualquier parte del código. No se permiten comentarios de bloque anidados.

#### Cadenas con comillas dobles

Las constantes de tipo cadena utilizarán exclusivamente comillas dobles:

```javascript
"Hola, mundo"
```

Las cadenas pueden estar vacías y pueden contener hasta 64 caracteres. También pueden utilizarse secuencias de escape como `\n` y `\t`, según las características implementadas en la práctica.

---

# Funcionamiento

El procesador recibe un programa fuente mediante un fichero de texto.

```text
             ┌──────────────────┐
             │  Programa fuente │
             │    PdL-JS        │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Análisis Léxico  │
             └────────┬─────────┘
                      │
                      ▼
                 ┌─────────┐
                 │ Tokens  │
                 └────┬────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Análisis         │
             │ Sintáctico LR    │
             └────────┬─────────┘
                      │
             ┌────────┴─────────┐
             ▼                  ▼
        ┌──────────┐      ┌──────────┐
        │  Parse   │      │ Gramática│
        └────┬─────┘      └────┬─────┘
             │                  │
             └────────┬─────────┘
                      ▼
                    VASt
                      │
                      ▼
             Árbol sintáctico

                      │
                      ▼
             ┌──────────────────┐
             │ Análisis         │
             │ Semántico        │
             └────────┬─────────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
       Tabla de Símbolos     Errores
```

---

# Entrada

El procesador recibe un **fichero de texto** que contiene el programa PdL-JS que se desea analizar.

Ejemplo:

```javascript
let n int;

n = 1;

while (n <= 10)
{
    echo n;
    n = n + 1;
}
```

PdL-JS es un lenguaje **case sensitive**, por lo que las mayúsculas y minúsculas se consideran diferentes. Además, permite espacios, tabuladores, saltos de línea y comentarios en cualquier parte del código.

---

# Salidas

El procesador debe generar los siguientes resultados.

## Tokens

Fichero que contiene el listado de todos los tokens generados durante el análisis léxico.

```text
tokens.txt
```

El formato deberá ajustarse al formato oficial especificado para la práctica.

---

## Parse

Fichero que contiene los números de las reglas utilizadas durante el análisis sintáctico.

```text
parse.txt
```

Este fichero, junto con la gramática utilizada por el procesador, podrá utilizarse como entrada de **VASt** para generar el árbol sintáctico.

---

## Tabla de Símbolos

Fichero que contiene un volcado legible de las Tablas de Símbolos utilizadas durante el análisis semántico.

```text
tabla_simbolos.txt
```

Debe incluirse la información de las tablas globales y locales.

Cada tabla debe volcarse una vez que haya sido completada y antes de ser destruida.

PdL-JS utiliza ámbitos globales y locales. Las variables declaradas fuera de una función son globales, mientras que las declaradas dentro de una función son locales. Además, los parámetros de las funciones forman parte de su ámbito local.

---

## Errores

Fichero con los errores detectados durante el procesamiento del programa:

```text
errores.txt
```

Cada error debe incluir como mínimo:

* Número de línea.
* Tipo de error:

  * Léxico.
  * Sintáctico.
  * Semántico.
* Mensaje descriptivo.

Los mensajes deben estar escritos de forma comprensible para el usuario y deben indicar, en la medida de lo posible, cómo corregir el problema.

Ejemplo:

```text
Línea 12 - Error semántico:
La variable 'resultado' es de tipo entero y no puede recibir una expresión de tipo cadena.
```

---

# Fases del procesador

## 1. Análisis léxico

El analizador léxico transforma el programa fuente en una secuencia de tokens.

Entre otros elementos, deberá reconocer:

* Palabras reservadas.
* Identificadores.
* Constantes enteras.
* Constantes reales.
* Cadenas.
* Operadores.
* Delimitadores.
* Comentarios de bloque.
* Errores léxicos.

Los identificadores pueden contener letras, dígitos y `_`, pero deben comenzar por una letra o `_`.

### Características específicas

| Elemento          | Implementación |     |
| ----------------- | -------------- | --- |
| Comentarios       | `/* ... */`    |     |
| Cadenas           | `"..."`        |     |
| Operador especial | `\|=`          |`\|=`|
| Case sensitive    | Sí             |     |

---

## 2. Análisis sintáctico

El analizador sintáctico comprueba que la secuencia de tokens cumple la gramática de PdL-JS.

### Técnica

**LR ascendente**

El resultado del análisis deberá permitir generar el fichero `parse` requerido por la práctica.

El `parse` y la gramática serán utilizados posteriormente por **VASt** para visualizar el árbol sintáctico.

---

## 3. Análisis semántico

El análisis semántico comprueba las restricciones del lenguaje que no pueden determinarse únicamente mediante la gramática.

Entre otras comprobaciones, se deberán considerar:

* Tipos de datos.
* Compatibilidad de tipos en asignaciones.
* Uso de identificadores.
* Declaraciones.
* Ámbitos.
* Parámetros de funciones.
* Valores de retorno.
* Operaciones compatibles con los tipos.
* Uso correcto de `|=`.
* Condiciones lógicas de `while`.

PdL-JS dispone de los tipos:

```text
int
float
boolean
string
void
```

y no permite conversiones automáticas entre tipos.

---

# Tabla de Símbolos

La Tabla de Símbolos almacenará la información necesaria para realizar el análisis semántico.

PdL-JS utiliza:

* Ámbito global.
* Ámbitos locales asociados a funciones.
* Parámetros de funciones.
* Variables locales.
* Variables globales.
* Funciones.

Las variables no declaradas explícitamente se consideran variables globales de tipo entero.

Además, el lenguaje permite **recursividad**, por lo que una función puede llamarse a sí misma. No se permiten funciones anidadas.


> **Nota sobre el uso de Inteligencia Artificial**
>
> Para la elaboración y estructuración de este archivo `README.md` se hizo uso de herramientas de Inteligencia Artificial (IA) como apoyo en la redacción, organización y presentación de la información.

