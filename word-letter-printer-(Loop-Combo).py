## This Program:
# - uses for/while -loop
# - keeps asking for words using (while-loop)
# - prints every letter on a new line using (for-loop)
# - stops when person types "stop"


user_word = ""

while user_word != "stop":
    user_word = input("Type any word, or type 'stop' to stop: ")
    if user_word.lower() == "stop":
        break  ### Stops the loop directly, code below will not be runned

    for word in user_word:
        print(word)
