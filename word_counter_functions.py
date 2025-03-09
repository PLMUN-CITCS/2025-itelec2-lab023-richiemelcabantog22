def get_sentence_input():
    input_sentence = input("Enter a sentence: ")
    return input_sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

if __name__ == "__main__":
    main()