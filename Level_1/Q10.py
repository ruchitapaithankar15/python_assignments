# Taking input from the user
sentence = input("Enter a sentence: ")

# Manually splitting the sentence into words
words = []
word = ''
for char in sentence:
    if char == ' ':
        if word:
            words.append(word)
            word = ''
    else:
        word += char
if word:  # Append the last word
    words.append(word)

# Reversing the order of words manually
reversed_sentence = ''
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + ' '

# Removing the trailing space
reversed_sentence = reversed_sentence.strip()

# Displaying the reversed sentence
print("Reversed sentence:", reversed_sentence)
