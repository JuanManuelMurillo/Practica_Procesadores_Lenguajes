tokens = (

    'opsum',
    'opsub',
    'opeq',
    'not',
    'logor',
    'assig',

    'parenopen',
    'parenclosed',
    'curlopen',
    'curlclosed',

    'integer',
    'realnum',
    'string',

    'id',

    'semc',
    'comma',
)

reserved = {
    'let': 'let',
    'int': 'int',
    'float': 'float',
    'boolean': 'bool',
    'string': 'str',
    'void': 'void',
    'echo': 'echo',
    'prompt': 'prompt',
    'return': 'ret',
    'if': 'if',
    'while': 'while',
    'function': 'fun',
}

tokens = tokens + tuple(reserved.values())
