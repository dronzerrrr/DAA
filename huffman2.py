# # import heapq
# # from collections import defaultdict
# # 
# # # Class to represent each node in the Huffman tree
# # class Node:
# #     def __init__(self, char, freq):
# #         self.char = char    # Character
# #         self.freq = freq    # Frequency of the character
# #         self.left = None    # Left child
# #         self.right = None   # Right child
# # 
# #     # This is required to compare nodes in the priority queue (min-heap)
# #     def __lt__(self, other):
# #         return self.freq < other.freq
# # 
# # # Function to build the Huffman tree
# # def build_huffman_tree(text):
# #     # Step 1: Calculate the frequency of each character
# #     freq = defaultdict(int)
# #     for char in text:
# #         freq[char] += 1
# # 
# #     # Step 2: Build a priority queue (min-heap) with nodes of the Huffman tree
# #     priority_queue = [Node(char, freq) for char, freq in freq.items()]
# #     heapq.heapify(priority_queue)
# # 
# #     # Step 3: Combine nodes to build the Huffman tree
# #     while len(priority_queue) > 1:
# #         # Pop two nodes with the smallest frequency
# #         left = heapq.heappop(priority_queue)
# #         right = heapq.heappop(priority_queue)
# # 
# #         # Create a new internal node with a frequency equal to the sum of both nodes
# #         internal_node = Node(None, left.freq + right.freq)
# #         internal_node.left = left
# #         internal_node.right = right
# # 
# #         # Push the new node back into the priority queue
# #         heapq.heappush(priority_queue, internal_node)
# # 
# #     # Step 4: The final node in the queue is the root of the Huffman Tree
# #     return priority_queue[0]
# # 
# # # Function to generate the Huffman codes by traversing the Huffman Tree
# # def generate_huffman_codes(root):
# #     codes = {}
# # 
# #     # Recursive function to generate codes by traversing the tree
# #     def _generate_codes(node, current_code):
# #         if node is not None:
# #             if node.char is not None:
# #                 codes[node.char] = current_code
# #             # Traverse left and right subtrees
# #             _generate_codes(node.left, current_code + '0')
# #             _generate_codes(node.right, current_code + '1')
# # 
# #     # Start the recursive generation from the root
# #     _generate_codes(root, "")
# #     return codes
# # 
# # # Function to encode the text using the Huffman codes
# # def huffman_encoding(text):
# #     # Step 1: Build the Huffman Tree
# #     root = build_huffman_tree(text)
# #     
# #     # Step 2: Generate the Huffman codes for each character
# #     codes = generate_huffman_codes(root)
# #     
# #     # Step 3: Encode the text using the generated Huffman codes
# #     encoded_text = ''.join([codes[char] for char in text])
# #     
# #     return encoded_text, codes
# # 
# # # Function to decode the encoded text using the Huffman tree
# # def huffman_decoding(encoded_text, root):
# #     decoded_text = []
# #     current_node = root
# # 
# #     for bit in encoded_text:
# #         # Traverse the tree: left = '0', right = '1'
# #         if bit == '0':
# #             current_node = current_node.left
# #         else:
# #             current_node = current_node.right
# # 
# #         # If it's a leaf node, append the character to the decoded text
# #         if current_node.char is not None:
# #             decoded_text.append(current_node.char)
# #             current_node = root  # Move back to the root to decode the next character
# #     
# #     return ''.join(decoded_text)
# # 
# # # Example usage
# # if __name__ == "__main__":
# #     text = "harsh khandelwal"
# #     
# #     # Perform Huffman Encoding
# #     encoded_text, codes = huffman_encoding(text)
# #     print("Huffman Codes:", codes)
# #     print("Encoded Text:", encoded_text)
# #     
# #     # Perform Huffman Decoding
# #     root = build_huffman_tree(text)  # Rebuild the tree to decode
# #     decoded_text = huffman_decoding(encoded_text, root)
# #     print("Decoded Text:", decoded_text)
# #
# import heapq
# 
# # Class to represent each node in the Huffman tree
# class Node:
#     def __init__(self, char, freq):
#         self.char = char    # Character (Leaf Node)
#         self.freq = freq    # Frequency of the character
#         self.left = None    # Left child
#         self.right = None   # Right child
# 
#     # This is required to compare nodes in the priority queue (min-heap)
#     def __lt__(self, other):
#         return self.freq < other.freq
# 
# # Function to build the Huffman tree for the characters based on their frequencies
# def build_huffman_tree(chars, freqs):
#     # Step 1: Create a priority queue (min-heap) with nodes of the Huffman tree
#     priority_queue = [Node(char, freq) for char, freq in zip(chars, freqs)]
#     heapq.heapify(priority_queue)
# 
#     # Step 2: Combine nodes to build the Huffman tree
#     while len(priority_queue) > 1:
#         # Pop two nodes with the smallest frequency
#         left = heapq.heappop(priority_queue)
#         right = heapq.heappop(priority_queue)
# 
#         # Create a new internal node with a frequency equal to the sum of both nodes
#         internal_node = Node(None, left.freq + right.freq)
#         internal_node.left = left
#         internal_node.right = right
# 
#         # Push the new node back into the priority queue
#         heapq.heappush(priority_queue, internal_node)
# 
#     # Step 3: The final node in the queue is the root of the Huffman Tree
#     return priority_queue[0]
# 
# # Function to generate the Huffman codes for the characters
# def generate_huffman_codes(root):
#     codes = {}
# 
#     # Recursive function to generate codes by traversing the tree
#     def _generate_codes(node, current_code):
#         if node is not None:
#             if node.char is not None:  # If it's a leaf node (character)
#                 codes[node.char] = current_code
#             # Traverse left and right subtrees
#             _generate_codes(node.left, current_code + '0')
#             _generate_codes(node.right, current_code + '1')
# 
#     # Start the recursive generation from the root
#     _generate_codes(root, "")
#     return codes
# 
# # Function to encode the text using the Huffman codes
# def huffman_encoding(chars, freqs):
#     # Step 1: Build the Huffman Tree
#     root = build_huffman_tree(chars, freqs)
#     
#     # Step 2: Generate the Huffman codes for each character
#     codes = generate_huffman_codes(root)
#     
#     return codes
# 
# # Function to encode a sequence of characters using Huffman codes
# def encode_text(text, codes):
#     return ''.join([codes[char] for char in text])
# 
# # Example usage
# if __name__ == "__main__":
#     # Characters and their corresponding frequencies
#     chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#     freqs = [10, 15, 12, 3, 4, 13, 1]
# 
#     # Perform Huffman Encoding
#     codes = huffman_encoding(chars, freqs)
#     print("Huffman Codes:", codes)
# 
#     # Encode a sample text using the generated Huffman codes
#     sample_text = "ABCDE"
#     encoded_text = encode_text(sample_text, codes)
#     print(f"Encoded Text for '{sample_text}':", encoded_text)
#
import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):  # for heap comparison
        return self.freq < other.freq

# Build Huffman Tree
def buildHuffmanTree(chars, freq):
    heap = [Node(chars[i], freq[i]) for i in range(len(chars))]
    heapq.heapify(heap)  # create min-heap

    while len(heap) > 1:
        # Pick two smallest nodes (Greedy choice)
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create new internal node
        newNode = Node(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right

        heapq.heappush(heap, newNode)

    return heap[0]  # root of the tree

# Generate Huffman Codes
def generateCodes(root, code, codes):
    if root:
        if root.char:  # leaf node
            codes[root.char] = code
        generateCodes(root.left, code + "0", codes)
        generateCodes(root.right, code + "1", codes)

# Main function
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
freq = [10, 15, 12, 3, 4, 13, 1]

root = buildHuffmanTree(chars, freq)
codes = {}
generateCodes(root, "", codes)

print("Character\tFrequency\tHuffman Code")
for ch in chars:
    print(f"   {ch}\t\t   {freq[chars.index(ch)]}\t\t   {codes[ch]}")
