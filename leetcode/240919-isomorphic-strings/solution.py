def isIsomorphic(s, t):
    def encode_string(s):
        char_index_map = {}
        encoded = []
        
        for index, char in enumerate(s):
            if char not in char_index_map:
                char_index_map[char] = index
            encoded.append(char_index_map[char])
        
        return encoded
    return encode_string(s) == encode_string(t)