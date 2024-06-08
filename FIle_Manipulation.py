from collections import Counter

def count_words_in_file(file_path):
  try:
    with open(file_path, 'r') as file:
      text = file.read().lower().replace('\n', ' ')
      words = text.split()
      word_counts = Counter(words)
      sorted_word_counts = dict(sorted(word_counts.items()))
      return sorted_word_counts
  except FileNotFoundError:
    return "Error: File not found."
  except Exception as e:
    return f"Error: {str(e)}"

file_path = input("Enter the path of the text file: ")
word_counts = count_words_in_file(file_path)

if isinstance(word_counts, dict):
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
else:
    print(word_counts)