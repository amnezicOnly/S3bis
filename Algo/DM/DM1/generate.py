import random
import time
"""import nltk

# Download NLTK's words dataset (if not already downloaded)
nltk.download('words')

from nltk.corpus import words

def generate_word_file(n, output_file):
    word_list = words.words()
    
    selected_words = set()
    
    with open(output_file, 'w') as file:
        while len(selected_words) < n:
            word = random.choice(word_list)
            word = word.lower()  # Convert word to lowercase
            
            if word not in selected_words:
                selected_words.add(word)
                file.write(word + '\n')"""


def generate_words(number):
    a=ord('a')
    alph=[chr(i) for i in range(a,a+26)]
    output = open("output.txt","w")
    for i in range(number):
        s = ""
        longueur = random.randint(1,25)
        for j in range(longueur):
            index = random.randint(0,25)
            s+=alph[index]
        output.write(s+"\n")
    output.close()
        
start = time.time()
generate_words(1000*1000*2)
end = time.time()
print(str(end-start))