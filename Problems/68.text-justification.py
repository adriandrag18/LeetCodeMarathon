# title: Text Justification
# timestamp: 2025-06-10 20:16:14
# problemUrl: https://leetcode.com/problems/text-justification/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[words[0]]]
        curr = len(words[0])
        for word in words[1:]:
            if curr + len(word) + 1 > maxWidth:
                lines.append([word])
                curr = len(word)
                continue
            curr += len(word) + 1
            lines[-1].append(word)
        # print(*lines, sep='\n')
        lines[-1] = ' '.join(lines[-1])
        lines[-1] += ' ' * (maxWidth - len(lines[-1]))
        for i in range(len(lines) - 1):
            line = lines[i]
            if len(line) == 1:
                lines[i] = line[0] + ' ' * (maxWidth - len(line[0]))
                continue
            letters = sum([len(w) for w in line])
            spaces = maxWidth - letters
            n = len(line) - 1
            a, b = divmod(spaces, n)
            if b:
                line = [(' ' * (a + 1)).join(line[:b + 1])] + line[b + 1:]
            # print(spaces, letters, n, a, b, line)
            lines[i] = (' ' * a).join(line)
        
        return lines