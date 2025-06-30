// title: Reverse Vowels of a String
// timestamp: 2024-04-18 12:28:09
// problemUrl: https://leetcode.com/problems/reverse-vowels-of-a-string/
// memory: 4.2 MB
// runtime: 0 ms

func reverseVowels(str string) string {
    s := []byte(str)
    for i, j := 0, len(s) - 1; i < j; {
        if isVowel(s[i]) && isVowel(s[j]) {
            s[i], s[j] = s[j], s[i]
            i++
            j--
            continue
        }
        if !isVowel(s[i]) {
            i++
        }
        if !isVowel(s[j]) {
            j--
        }
    }
    return string(s)
}

func isVowel (c byte) bool {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}