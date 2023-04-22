import json

mapa = {
    111111: ('Yana', 33),
    111112: ('Oleh', 32),
    111113: ('Helo', 31),
    111114: ('Chmonya', 30),
    111115: ('Johan', 29),
    111116: ('Messiah', 28)
}

with open('data.json', 'w') as file:
    json.dump(mapa, file, indent=' ')
