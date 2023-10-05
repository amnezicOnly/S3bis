def check_for_duplicates(file_path):
    word_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if word in word_set:
                return (True, word)
            else:
                word_set.add(word)
    return False

print(check_for_duplicates("/home/amnezic/Desktop/S3bis/Algo/DM1/output.txt"))