word_without_vowels = ""
word=input('enter a word:').upper()
for letter in word:
    if letter=='A'or letter=='E'or letter=='I'or letter=='O'or letter=='U':
        continue
    else:
        word_without_vowels+=letter

print(word_without_vowels)