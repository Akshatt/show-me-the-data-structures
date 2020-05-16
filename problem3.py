# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:46:35 2020

@author: Akshat
"""

import sys
from collections import Counter
from heapq import heapify, heappush, heappop
                

class Huffman:
    def __init__(self):
        self.codes = {}
        
    def huffman_encoding(self,data):
        if data == "":
            return "0", 0
        
        freq = Counter(data)
        heap = []
        for char,freq in freq.items():
            heap.append([freq, [char,'']])
        
        heapify(heap)
        while len(heap) != 1:
            left_node = heappop(heap)
            right_node = heappop(heap)
            for code in left_node[1:]:
                code[1] = '0' + code[1]
            for code in right_node[1:]:
                code[1] = '1' + code[1]
            heappush(heap, [ left_node[0] + right_node[0] ] + left_node[1:] + right_node[1:] )
        
        root = heappop(heap)
        for char,code in sorted(root[1:], key = lambda x: (len(x[-1]), x)):
            self.codes[char] = code
        
        encoded_data = ""
        for i in data:
            encoded_data += self.codes[i]    
        return encoded_data, root
    
    
    def huffman_decoding(self,data,tree):
        decoded = ""
        current = ""
        def get_val(val):
            for key,value in self.codes.items():
                if value == val:
                    return key

        for i in range(0,len(data)):
            current += data[i]
            if current in self.codes.values():
                decoded += get_val(current)
                current = ""
            
        return decoded



if __name__ == "__main__":
    
    print("Testcase 1")
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    H = Huffman()
    encoded_data, tree = H.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = H.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
    print("Testcase 2")
    a_great_sentence = "The"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    H = Huffman()
    encoded_data, tree = H.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = H.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Testcase 3") #Taking an empty input; we encode it as 0 and perform the coding 
    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    H = Huffman()
    encoded_data, tree = H.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = H.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
