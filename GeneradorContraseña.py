import random
import string, secrets

tamaño = int(input("Escribe el numero de caracteres para tu contaseña (que sea mayor a 8): "))
caracteres = [
"!", ".", "#", "$", "%", "&", "'", "(",
")", "*", "+", ",", "-", ".", "/", ":", ";", "<",
"=", ">", "?", "@", "[", "^", "_", "`", "{", "|",
"}", "~"
]
contaseña = []

for i in range(tamaño*5):
    rand = secrets.choice(string.ascii_letters)
    caracteres.append(rand)

for i in range(tamaño):
    contaseña.append(random.choice(caracteres))

print ("".join(contaseña))
