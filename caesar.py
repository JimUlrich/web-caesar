def alphabet_pos(letter):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in lower:
        return lower.index(letter)
    else:
        return upper.index(letter)

def rotate(char, rot):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char not in lower and char not in upper:
        return char
    else:
        pos = alphabet_pos(char)
        new_pos =  (pos + rot) % 26
        if char in lower:
            return lower[new_pos]
        elif char in upper:
            return upper[new_pos]
