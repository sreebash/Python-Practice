print('Please, input the character:')
character = input()

if character >= 'a' and character <= 'z' or character >= 'A' and character <= 'z' :
    if character in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Nothing')