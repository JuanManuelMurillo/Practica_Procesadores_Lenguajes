# Gramática — PdL-JS

```text

S -> del S | d N | l I | _ I | " C | / O | = E | | P | + | - | ! | ( | ) | { | } | ; | , 
 
# Números
 
N -> d N | . R | del
R -> d R'
R' -> d R' | del
 
# Cadenas
 
C -> l C | d C | o.c.c C | "
 
# Comentarios (Multilínea)
 
O -> * O'
O' -> l O' | d O' | o.c.2 O' | del O' | * O''
O'' ->  / | l O' | d O' | o.c.3 O' | del O'
 
# Identificadores
 
I -> l I | d I | _ I | del
 
# Operadores
 
E -> = | del
P -> =

# Clases de caracteres
l: [a-z] | [A-Z]
d: [0-9]
l, d, " y nl
o.c.c.: Cualquier carácter excepto letras, dígitos, " y salto de línea
o.c.2: Cualquier carácter excepto letras, dígitos, * y delimitadores
o.c.3:Cualquier carácter excepto letras, dígitos, *, / y delimitadores
del: blanco, tabulador, salto de línea
```

## Tabla de palabras reservadas (TPR)

```text
let      -> let
int      -> int
float    -> float
boolean  -> bool
string   -> str
void     -> void
echo     -> echo
prompt   -> prompt
return   -> ret
if       -> if
while    -> while
function -> fun