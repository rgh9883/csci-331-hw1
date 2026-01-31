import sys


if __name__ == "__main__":
    words_file = sys.argv[1]
    start_str = sys.argv[2]
    target_str = sys.argv[3]
    pos_words = []
    with open(words_file, "r") as f:
        for line in f:
            word = line.strip()
            if len(word) == len(start_str):
                pos_words.append(word)

    for word in pos_words:
        print(word)
            
