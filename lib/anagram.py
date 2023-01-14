class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list):
        matched_list = []
        individual_letters = [letter for letter in self.word]
        for word in list:
            if sorted([letter for letter in word]) == sorted(individual_letters):
                matched_list.append(word)
        
        return matched_list