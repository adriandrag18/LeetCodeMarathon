# title: Find the K-th Character in String Game I
# timestamp: 2025-07-03 12:36:50
# problemUrl: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def kthCharacter(self, k: int) -> str:
        # arr = [0]
        # while len(arr) < k:
        #     arr.extend([(el + 1) % 26 for el in arr])
        # return chr(ord('a') + arr[k-1])

        # s = 'abbcbccdbccdcddebccdcddecddedeefbccdcddecddedeefcddedeefdeefeffgbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhibccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhicddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhideefeffgeffgfggheffgfgghfgghghhieffgfgghfgghghhifgghghhighhihiij'
        # return s[k-1]

        return chr(ord('a') + ((k-1).bit_count() % 26))
