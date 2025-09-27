import random
symvols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password=int(input("Введите длинну пароля в цифрах"))
parol=""
for i in range(password):
    parol += random.choiсe(symvols)
print(parol)