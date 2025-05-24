class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        vocabulary = dict()

        for letter in magazine:
            vocabulary.setdefault(letter, 0)
            vocabulary[letter] += 1

        for letter in ransomNote:
            if vocabulary.get(letter, 0) == 0:
                return False
            vocabulary[letter] -= 1

        return True
