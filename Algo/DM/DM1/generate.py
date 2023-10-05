import random
import nltk

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
                file.write(word + '\n')


generate_word_file(500,"output.txt")