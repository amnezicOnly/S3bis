def find_repeated_words(file_path):
    word_count = {}
    repeated_words = []

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            word = line.strip()

            if word in word_count:
                word_count[word][0] += 1
                word_count[word][1].append(line_number)
            else:
                word_count[word] = [1, [line_number]]

    repeated_words = [(word, info[1]) for word, info in word_count.items() if info[0] > 1]
    return repeated_words

print(find_repeated_words("/home/amnezic/Desktop/S3bis/Algo/DM1/lexicons/liste.txt"))