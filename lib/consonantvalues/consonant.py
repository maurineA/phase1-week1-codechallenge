def consonant (s):
    def sub_string(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)
    
    #remove vowels
    consonant_str = ''.join(char for char in s if char not in 'aeiou')

    #split into substring consonant
    consonant_substrings = consonant_str.split('a') 