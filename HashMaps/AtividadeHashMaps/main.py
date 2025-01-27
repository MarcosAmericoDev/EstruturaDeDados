

### Algoritmos de função hash

# Somatório
def hash_sum(s):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
    return hash_value
        
# Dispersão Polinomial
def hash_polynomial(s):
    hash_value = 0
    i = 0
    primo = 23 #O valor primo pequeno escolhido foi 23
    for c in s:
        hash_value += ord(c)*primo**i
        i += 1
    return hash_value

# Dispersão de Deslocamento Cíclico
def hash_ciclic(s):
    mask = (1 << 32) - 1
    hash_value = 0
    for c in s:
        hash_value = (hash_value << 5 & mask) | (hash_value >> 27)
        hash_value += ord(c)
    return hash_value

### Algoritmos de Compressão

# Compressão por divisão
def compression_division(map):
    for key in list(map.keys()):
        value = map.pop(key)
        map[key%32] = value
    return map

# Strings utilizadas para o teste


if __name__ == "__main__":
    strings = [ "apple", "voadora", "banjo", "banana", "cherry", "date",
    "elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
    "mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
    "IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco" ]
    map = {}
    for string in strings:
        map[hash_sum(string)] = string