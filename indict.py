from collections import defaultdict

# Sample sentences
sentences = [
    "lib adw one",
    "lib adw two",
    "lib gtk three",
    "it is example sentence",
    "it is not a good example of a sentence"
]

# Tokenize and remove punctuation
def preprocess_sentence(sentence):
    # Split "lib adw one" into ['lib','adw','one'] by space
    tokens = sentence.split()
    # Check if each token is alphabetic
    tokens = [word.lower() for word in tokens if word.isalpha()]
    return tokens

# Create a list of tokens for each sentence
tokenized_sentences = [preprocess_sentence(sentence) for sentence in sentences]

# We need to find the most common word in sentences
counter = defaultdict(int)

# Count words
for sentence in tokenized_sentences:
    for word in sentence:
        counter[word] += 1

# Get the max frequency
mostCommonWord = max(counter, key=counter.get)

# Create a tree structure with the most common word as the root using a dictionary
tree = {mostCommonWord: {}}

for sentence_tokens in tokenized_sentences:
    current_node = tree[mostCommonWord]
    for token in sentence_tokens:
        current_node = current_node.setdefault(token, {})

# Helper function to print the tree
def print_tree(node, depth=0):
    indent = ""
    if depth >= 1:
        indent = ("- " * (depth - 1) + "-> ")
    else:
        indent = ("   " * depth)
    for key, value in node.items():
        print(indent + key)
        print_tree(value, depth + 1)

# Print the tree
print_tree(tree)