import math

vowels = 'aeiouyAEIOUY'

max_power = 0
most_powerful_word = ''

while True:
    word = input()
    if word == "End of words":
        break

    word_sum = sum(ord(char) for char in word)
    if word[0] in vowels:
        power = word_sum * len(word)
    else:
        power = math.floor(word_sum / len(word))

    if power > max_power:
        max_power = power
        most_powerful_word = word

print(f"The most powerful word is {most_powerful_word} - {max_power}")
