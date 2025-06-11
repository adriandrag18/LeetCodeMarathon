# title: Count of Substrings Containing Every Vowel and K Consonants II
# timestamp: 2025-03-10 23:57:34
# problemUrl: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/
# memory: 18.7 MB
# runtime: 2542 ms

class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in ["a", "e", "i", "o", "u"]

    def _atLeastK(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = 0
        end = 0
        # keep track of counts of vowels and consonants
        vowel_count = {}
        consonant_count = 0

        # start sliding window
        while end < len(word):
            # insert new letter
            new_letter = word[end]

            # update counts
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # shrink window while we have a valid substring
            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] = (
                        vowel_count.get(start_letter) - 1
                    )
                    if vowel_count.get(start_letter) == 0:
                        vowel_count.pop(start_letter)
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)