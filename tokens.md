| **Nombre** | **Token** | **Lexema** | **Patrón** | **Condiciones** |
|---|---|---|---|---|
| **Operadores** | | | | |
| Suma | `<op_sum,->` | `+` | | |
| Resta | `<op_sub,->` | `-` | | |
| Igualdad | `<op_eq,->` | `==` | | |
| No | `<not,->` | `!` | | |
| Asignación o lógico | `<log_or,->` | `\|=` | | |
| Asignación | `<assig,->` | `=` | | |
| **Símbolos de Agrupación** | | | | |
| Paréntesis abierto | `<paren_open,->` | `(` | | |
| Paréntesis cerrado | `<paren_closed,->` | `)` | | |
| Llave abierta | `<curl_open,->` | `{` | | |
| Llave cerrada | `<curl_closed,->` | `}` | | |
| **Constantes** | | | | |
| Número entero | `<integer, valor>` | `1, 20, 300` | Uno o más dígitos | **MAX:** 32767 |
| Número real | `<real_num, valor>` | `0.1, 1.20, 2.300` | Uno o más dígitos seguidos de un punto y uno o más dígitos | **MAX:** 117549436.0 |
| Cadena de caracteres | `<string, lexema>` | `"¡Hola mundo!"` | Secuencia de caracteres entre **comillas dobles** | **MAX:** 64 caracteres. Salto de línea no válido |
| **Comentarios** | | | | |
| Comentario | `<comment,->` | `/* Contenido */` | | No se permiten comentarios anidados |
| Identificador | `<id, posTS>` | `num, _res2` | Cualquier cantidad de letras, dígitos y subrayados; el primero siempre tiene que ser una letra o subrayado | |
| **Declaraciones** | | | | |
| Declaración | `<let,->` | `let` | | |
| **Tipos de Datos** | | | | |
| Entero | `<int_t,->` | `int` | | |
| Real | `<float_t,->` | `float` | | |
| Lógico | `<bool_t,->` | `boolean` | | |
| Cadena | `<str_t,->` | `string` | | |
| Vacío | `<void_t,->` | `void` | | |
| Semicolon | `<semc,->` | `;` | | |
| Coma | `<coma,->` | `,` | | |
| Fin fichero | `<eof,->` | | | |
| **Instrucciones Entrada / Salida** | | | | |
| Salida | `<echo,->` | `echo` | | |
| Entrada | `<promt,->` | `prompt` | | |
| **Sentencias** | | | | |
| Retorno | `<ret,->` | `return` | | |
| If | `<if,->` | `if` | | |
| While | `<while,->` | `while` | | |
| **Funciones** | | | | |
| Definición | `<fun,->` | `function` | | |