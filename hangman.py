import random
import os

def read_data(string):
    list_of_words = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line.rstrip()) #rstrip for delete \n
    return list_of_words

def run():
    spaces = []
    list_of_words = read_data("./files/data.txt")
    chosen_word = random.choice(list_of_words) #get a random word from list_of_words
    word_length = len(chosen_word)
    for i in range(0, word_length): #print the spaces
        spaces.append("_ ")
    string = ''.join([str(item) for item in spaces]) #convert the list to string
    k = 0

    while True: #infinite loop
        os.system("cls")
        print('Adivina la palabra:\n')
        print(string)
        user_letter = input('\nIngresa una letra: ')
        for i, word in enumerate(chosen_word):
            if word == user_letter: # if word == user_letter, write user_letter into spaces
                spaces[i] = user_letter.upper()+" "

        string = ''.join([str(item) for item in spaces])
        k+=1
        if " _ " not in string:
            print("\n¡Adivinaste! La palabra era:", string.replace(" ",""))
            break
        
        if k == 10:
            print('\n¡Has perdido! Agotaste tus intentos.')
            break
        
if __name__ == '__main__':
    run()