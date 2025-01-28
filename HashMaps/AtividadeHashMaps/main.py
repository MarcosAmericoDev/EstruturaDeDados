from Queue import Queue, QueueNode

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
    collision_count = 0
    for key in list(map.keys()):
        keyValue = map.pop(key)
        compressed_key = key % 32
        if compressed_key in map.keys():
            map[compressed_key].enQueue(keyValue)
            collision_count += 1
        else:
            queue = Queue()
            queue.enQueue(keyValue)
            map[compressed_key] = queue
    return map, collision_count

# Compressão por dobra
def compression_fold(map):
    collision_count = 0
    for key in list(map.keys()):
        keyValue = map.pop(key)
        stringKey = str(key)
        while len(stringKey) % 4 != 0:
            stringKey += "0"
        while len(stringKey) > 2:
            compressed_key = ""
            for i in range(0, len(stringKey), 4):
                sum1 = int(stringKey[i]) + int(stringKey[i+3])
                sum2 = int(stringKey[i+1]) + int(stringKey[i+2])
                compressed_key += str(sum1 % 10) + str(sum2 % 10)
            stringKey = compressed_key
        key = int(stringKey) % 32 # tabela de tamanho 32
        if key in map.keys():
            map[key].enQueue(keyValue)
            collision_count += 1
        else:
            queue = Queue()
            queue.enQueue(keyValue)
            map[key] = queue
    return map, collision_count

# Compressão por MAD
def compression_mad(map):
    # Fará seguindo essa fórmula = [(a * numero_da_chave + b) mod numero_primo] mod tamanho_da_tabela
    primeNumber = 1693
    a = 46
    b = 747
    collision_count = 0
    for key in list(map.keys()):
        keyValue = map.pop(key)
        compressed_key = ((a*key + b) % primeNumber) % 32
        if compressed_key in map.keys():
            map[compressed_key].enQueue(keyValue)
            collision_count += 1
        else:
            queue = Queue()
            queue.enQueue(keyValue)
            map[compressed_key] = queue
    return map, collision_count

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
    print(map)
    print("---------")
    newmap, collision_count = compression_fold(map)
    print(newmap[17].printQueue())
    print(collision_count)