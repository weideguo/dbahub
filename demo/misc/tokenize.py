# 词法分析器
# https://www.skywind.me/blog/archives/2761

import re

def tokenize(code, specs, eof = None):
    patterns = []
    definition = {}
    extended = {}
    if not specs:
        return None
    for index in range(len(specs)):
        spec = specs[index]
        name, pattern = spec[:2]
        pn = 'PATTERN%d'%index
        definition[pn] = name
        if len(spec) >= 3:
            extended[pn] = spec[2]
        patterns.append((pn, pattern))
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in patterns)
    line_starts = []
    pos = 0
    index = 0
    while 1:
        line_starts.append(pos)
        pos = code.find('\n', pos)
        if pos < 0:
            break
        pos += 1
    line_num = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        start = mo.start()
        while line_num < len(line_starts) - 1:
            if line_starts[line_num + 1] > start:
                break
            line_num += 1
        line_start = line_starts[line_num]
        name = definition[kind]
        if name is None:
            continue
        if callable(name):
            if kind not in extended:
                obj = name(value)
            else:
                obj = name(value, extended[kind])
            name = None
            if isinstance(obj, list) or isinstance(obj, tuple):
                if len(obj) > 0: 
                    name = obj[0]
                if len(obj) > 1:
                    value = obj[1]
            else:
                name = obj
        yield (name, value, line_num + 1, start - line_start + 1)
    if eof is not None:
        line_start = line_starts[-1]
        endpos = len(code)
        yield (eof, '', len(line_starts), endpos - line_start + 1)
    return 0
    


if __name__ == "__main__":

    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    
    def check_name(text):
        if text.upper() in keywords:
            return text.upper()
        return 'NAME'
    
    rules = [
            (None,       r'[ \t]+'),       # Skip over spaces and tabs
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('ASSIGN',   r':='),           # Assignment operator
            ('END',      r';'),            # Statement terminator
            (check_name, r'[A-Za-z]+'),    # Identifiers or keywords
            ('OP',       r'[+\-*/]'),      # Arithmetic operators
            ('NEWLINE',  r'\n'),           # Line endings
            ('MISMATCH', r'.'),            # Any other character
    ]
    
    code = '''
        IF quantity THEN
            total := total + price * quantity;
            tax := price * 0.05;
        ENDIF;
    '''
    
    for token in tokenize(code, rules, None):
        print(token)
        
    """
    ('NEWLINE', '\n', 1, 1)
    ('IF', 'IF', 2, 5)
    ('NAME', 'quantity', 2, 8)
    ('THEN', 'THEN', 2, 17)
    ('NEWLINE', '\n', 2, 21)
    ('NAME', 'total', 3, 9)
    ('ASSIGN', ':=', 3, 15)
    ('NAME', 'total', 3, 18)
    ('OP', '+', 3, 24)
    ('NAME', 'price', 3, 26)
    ('OP', '*', 3, 32)
    ('NAME', 'quantity', 3, 34)
    ('END', ';', 3, 42)
    ('NEWLINE', '\n', 3, 43)
    ('NAME', 'tax', 4, 9)
    ('ASSIGN', ':=', 4, 13)
    ('NAME', 'price', 4, 16)
    ('OP', '*', 4, 22)
    ('NUMBER', '0.05', 4, 24)
    ('END', ';', 4, 28)
    ('NEWLINE', '\n', 4, 29)
    ('ENDIF', 'ENDIF', 5, 5)
    ('END', ';', 5, 10)
    ('NEWLINE', '\n', 5, 11)
    
    """    


    ###########################################################################################

    keywords = {
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default',
        'define', 'do', 'double', 'elif', 'else', 'endif', 'enum',
        'error', 'extern', 'float', 'for', 'goto', 'if', 'ifdef',
        'ifndef', 'include', 'inline', 'int', 'line', 'long', 'noalias',
        'pragma', 'register', 'restrict', 'return', 'short', 'signed',
        'sizeof', 'static', 'struct', 'switch', 'typedef', 'undef',
        'union', 'unsigned', 'void', 'volatile', 'while', }
    
    operators = (
        '++', '--', '.', '->', '~', '!=', '+=', '-=', '&&', '_Alignof',
        'sizeof', '?:', ',', '*=', '/=', '%=', '<<=', '>>=', '<=', '>=', 
        '<<', '>>', '==', '!', '||', '&=', '|=', '^=', '*', '/', '%',
        '+', '-', '>', '<', '&', '=', '|', '?', ':', '^', )
    
    specials = {'(', '[', '{', '}', ']', ')', '#'}
    
    def check_name(text):
        if text in keywords:
            return text
        if text in operators:
            return 'OP'
        return 'NAME'
    
    
    # patterns
    PATTERN_WHITESPACE = r'[ \t\r\n]+'
    PATTERN_COMMENT1 = r'\/\/.*'
    PATTERN_COMMENT2 = r'\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/'
    PATTERN_NAME = r'\w+'
    PATTERN_STRING1 = r"'(?:\\.|[^'\\])*'"
    PATTERN_STRING2 = r'"(?:\\.|[^"\\])*"'
    PATTERN_NUMBER = r'\d+(\.\d*)?'
    PATTERN_CINTEGER = r'(0x)?\d+[uUlLbB]*'
    PATTERN_MISMATCH = r'.'
    
    rules = [
            (None, PATTERN_WHITESPACE),
            (None, PATTERN_COMMENT1),
            (None, PATTERN_COMMENT2),
            ('STRING', PATTERN_STRING1),
            ('STRING', PATTERN_STRING2),
            ('INTEGER', PATTERN_CINTEGER),
            ('NUMBER', PATTERN_NUMBER),
            (check_name, PATTERN_NAME),
            ('SEMICOLON', ';'),
    ]    
    
    
    # 注意：operators 是一个 list，按顺序添加，可以保证 ++ 的匹配优先级高于 +
    for op in operators:  
        rules.append(('OP', re.escape(op)))
    
    for sp in specials:
        rules.append((sp, re.escape(sp)))
    
    rules.append(('MISMATCH', PATTERN_MISMATCH))    
    
    
    code = '''
    // My first C program
    int main(void)
    {
        int x = 10;
        int y = x+++3;
        printf("Hello, World !!\n");
        return 0;
    }
    '''
    
    for token in tokenize(code, rules, None):
        print(token)
        
        
    '''
    ('int', 'int', 3, 1)
    ('NAME', 'main', 3, 5)
    ('(', '(', 3, 9)
    ('void', 'void', 3, 10)
    (')', ')', 3, 14)
    ('{', '{', 4, 1)
    ('int', 'int', 5, 5)
    ('NAME', 'x', 5, 9)
    ('OP', '=', 5, 11)
    ('INTEGER', '10', 5, 13)
    ('SEMICOLON', ';', 5, 15)
    ('int', 'int', 6, 5)
    ('NAME', 'y', 6, 9)
    ('OP', '=', 6, 11)
    ('NAME', 'x', 6, 13)
    ('OP', '++', 6, 14)
    ('OP', '+', 6, 16)
    ('INTEGER', '3', 6, 17)
    ('SEMICOLON', ';', 6, 18)
    ('NAME', 'printf', 7, 5)
    ('(', '(', 7, 11)
    ('STRING', '"Hello, World !!\n"', 7, 12)
    (')', ')', 8, 2)
    ('SEMICOLON', ';', 8, 3)
    ('return', 'return', 9, 5)
    ('INTEGER', '0', 9, 12)
    ('SEMICOLON', ';', 9, 13)
    ('}', '}', 10, 1)
    '''    
    
