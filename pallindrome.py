
word = input("Plese input any words?:")
word = word.casefold()
reversed_word = word[::-1]
if word == reversed_word:
    print('Great! It is a pallindrome.')
else:
    print('LOL! It\'s not a pallindrone.')