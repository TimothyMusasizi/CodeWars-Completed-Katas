class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.abs = ord(alphabet[0])
        self.key_len = len(key)
        self.alp_len = len(self.alphabet)
    
    def encode(self, text):
        l = []
        for i in range(len(text)):
            if text[i] in self.alphabet:
                new_ord = (self.alphabet.index(text[i]) + self.alphabet.index(self.key[i%self.key_len]))%self.alp_len
                new_ch = self.alphabet[new_ord]
                l.append(new_ch)
            else:
                l.append(text[i])
        return ''.join(l)
        
        
    def decode(self, text):
        l = []
        for i in range(len(text)):
            if text[i] in self.alphabet:
                new_ord = (self.alphabet.index(text[i]) + self.alp_len - self.alphabet.index(self.key[i%self.key_len]))%self.alp_len
                new_ch = self.alphabet[new_ord]
                l.append(new_ch)
            else:
                l.append(text[i])
        return ''.join(l)
                