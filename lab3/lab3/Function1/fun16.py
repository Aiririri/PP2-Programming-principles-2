def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = " ".join(reversed(words))  
    return reversed_sentence


user_input = input("Enter a sentence: ")
print(reverse_words(user_input))
