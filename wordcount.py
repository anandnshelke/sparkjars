# Word Count Code
def word_count(file_path):
    word_counts = {}
    with open(file_path, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    counts = word_count(input_file)
    with open(output_file, "w") as file:
        for word, count in counts.items():
            file.write(f"{word}: {count}\n")
