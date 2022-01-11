alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
print('alphabet: ', alphabet)
encrypt = input('Enter e clear massage: ')
key = int(input('Please enter a key (number from 1-25): '))
encrypt = encrypt.lower()
encrypted = ''
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter

print("your cipher is: ", encrypted)
