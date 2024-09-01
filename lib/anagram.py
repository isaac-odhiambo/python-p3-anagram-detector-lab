class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Helper function to check if two words are anagrams
        def are_anagrams(word1, word2):
            return sorted(word1) == sorted(word2)
        
        # Find and return words that are anagrams of self.word
        return [word for word in word_list if are_anagrams(self.word, word)]
