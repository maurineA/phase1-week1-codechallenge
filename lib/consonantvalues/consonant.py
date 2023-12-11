def consonant ():
    def sub_string(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)