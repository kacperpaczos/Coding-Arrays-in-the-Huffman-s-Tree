from collections import defaultdict

# Sample sentences
sentences = [
    "lib adw one",
    "lib adw two",
    "lib gtk three",
    "it is example sentence",
    "it is not good example of sentence"
]


# Tokenize and remove punctuation
def preprocess_sentence(sentence):
    # Split "lib adw one" in ['lib','adw','one'] by space
    tokens = sentence.split()
    # check is alppha True/False
    tokens = [word.lower() for word in tokens if word.isalpha()]
    return tokens


# Create a list of tokens for each sentence
# [['lib','adw','one'],['lib','adw','two']]
tokenized_sentences = [preprocess_sentence(sentence) for sentence in sentences]

# We need to find most common word in sentences
counter = defaultdict(int)

# counting words
for sentence in tokenized_sentences:
    for word in sentence:
        counter[word] += 1

# getting max frequency
mostCommonWord = max(counter, key=counter.get)


# Create a tree structure with the most common word as the root
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# Create a tree with the most common word as the root
root = TreeNode(mostCommonWord)

for sentence_tokens in tokenized_sentences:
    current_node = root
    for token in sentence_tokens:
        found = False
        for child in current_node.children:
            if child.value == token:
                current_node = child
                found = True
                break
        if not found:
            new_node = TreeNode(token)
            current_node.children.append(new_node)
            current_node = new_node


# Helper function to print the tree
def print_tree(node, depth=0):
    indent = ""
    if depth >= 1:
        indent = ("- " * (depth-1) + "-> ")
    else:
        indent = ("   " * depth)
    print(indent + node.value)
    for child in node.children:
        print_tree(child, depth + 1)


# Print the tree
print_tree(root)
