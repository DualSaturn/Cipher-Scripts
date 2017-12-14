def encrypt(msg, key):
    msg = msg.lower()
    ordinary_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code_alphabet = codegen(key.replace(' ', ''))
    new_msg = ''
    for x in msg:
        if x.isalpha():
            new_msg = new_msg + code_alphabet[ordinary_alphabet.index(x)]
        else:
            new_msg = new_msg + x
    return new_msg

def decrypt(msg, key):
    msg = msg.lower()
    ordinary_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code_alphabet = codegen(key.replace(' ', ''))
    old_msg = ''
    for x in msg:
        if x.isalpha():
            old_msg = old_msg + ordinary_alphabet[code_alphabet.index(x)]
        else:
            old_msg = old_msg + x
    return old_msg

def codegen(key):
    stem = ''
    for i in key:
        if not i in stem:
            stem = stem + i
    start_letter = chr(ord(stem[-1])+1) if ord(stem[-1]) != 122 else 'a'
    current_letter = chr(ord(start_letter)+1) if ord(start_letter) != 122 else 'a'
    code_alphabet = stem + start_letter
    while current_letter != start_letter:
        if current_letter not in stem:
            code_alphabet = code_alphabet + current_letter
        current_letter = chr(ord(current_letter)+1) if ord(current_letter) != 122 else 'a'
    return code_alphabet
