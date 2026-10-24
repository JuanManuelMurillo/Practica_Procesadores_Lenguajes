# Tokens — PdL-JS
| **Nombre** | **Token** | **Lexema** | **Patrón** | **Condiciones** |
|---|---|---|---|---|
| **Operadores** | | | | |
| Suma | `<opsum,->` | `+` | | |
| Resta | `<opsub,->` | `-` | | |
| Igualdad | `<opeq,->` | `==` | | |
| No | `<not,->` | `!` | | |
| Asignación o lógico | `<logor,->` | `\|=` | | |
| Asignación | `<assig,->` | `=` | | |
| **Símbolos de Agrupación** | | | | |
| Paréntesis abierto | `<parenopen,->` | `(` | | |
| Paréntesis cerrado | `<parenclosed,->` | `)` | | |
| Llave abierta | `<curlopen,->` | `{` | | |
| Llave cerrada | `<curlclosed,->` | `}` | | |
| **Constantes** | | | | |
| Número entero | `<integer, valor>` | `1, 20, 300` | Uno o más dígitos | **MAX:** 32767 |
| Número real | `<realnum, valor>` | `0.1, 1.20, 2.300` | Uno o más dígitos seguidos de un punto y uno o más dígitos | **MAX:** 117549436.0 |
| Cadena de caracteres | `<string, lexema>` | `"¡Hola mundo!"` | Secuencia de caracteres entre **comillas dobles** | **MAX:** 64 caracteres. Salto de línea no válido |
| **Comentarios** | | | | |
| Comentario | `<comment,->` | `/* Contenido */` | | No se permiten comentarios anidados |
| Identificador | `<id, posTS>` | `num, _res2` | Cualquier cantidad de letras, dígitos y subrayados; el primero siempre tiene que ser una letra o subrayado | |
| **Declaraciones** | | | | |
| Declaración | `<let,->` | `let` | | |
| **Tipos de Datos** | | | | |
| Entero | `<int,->` | `int` | | |
| Real | `<float,->` | `float` | | |
| Lógico | `<bool,->` | `boolean` | | |
| Cadena | `<str,->` | `string` | | |
| Vacío | `<void,->` | `void` | | |
| Semicolon | `<semc,->` | `;` | | |
| Coma | `<comma,->` | `,` | | |
| **Instrucciones Entrada / Salida** | | | | |
| Salida | `<echo,->` | `echo` | | |
| Entrada | `<prompt,->` | `prompt` | | |
| **Sentencias** | | | | |
| Retorno | `<ret,->` | `return` | | |
| If | `<if,->` | `if` | | |
| While | `<while,->` | `while` | | |
| **Funciones** | | | | |
| Definición | `<fun,->` | `function` | | |