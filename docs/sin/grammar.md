# Gramática — PdL-JS

## Estructura del Programa

```text

P --> B P
P --> F P
P --> λ

```

## Sentencias Compuestas y Declaración de Variables

```text

B --> let M id T ; 
B --> if ( E ) S 
B --> while ( E ) { C }
B --> S
M --> λ
T --> int | float | bool | str

```

## Sentencias Simples

```text

S --> id = E ;
S --> id logor E ; 
S --> id ( L ) ; 
S --> echo E ; 
S --> prompt id ; 
S --> return X ;
X --> E | λ
L --> E Q | λ
Q --> , E Q | λ

```

## Declaración de funciones

```text

F --> function F1 F2 { C }
F1 --> λ
F2 --> F3 H ( A )
F3 --> id
H --> T | void
A --> id T K | void
K --> , id T K | λ
C --> B C | λ

```

## Expresiones

```text

E --> E == R | R
R --> R + U | R - U | U
U --> ! U | V
V --> id | ( E ) | id ( L ) | integer | realnum | string

```
