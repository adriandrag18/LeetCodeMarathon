// title: Maximum Number of Vowels in a Substring of Given Length
// timestamp: 2024-04-16 19:36:39
// problemUrl: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
// memory: 4.9 MB
// runtime: 9 ms

func maxVowels(s string, k int) int {
    vowels := countVowels(s[0:k])
    max := vowels
    for i := k; i < len(s); i++ {
        if isvowel(s[i]) {
            vowels++
        }
        if isvowel(s[i-k]) {
            vowels--
        }
        if max < vowels {
            max = vowels
        }
        if max == k {
            break
        }
    }

    return max
}

func countVowels(s string) int {
    count := 0
    for _, c := range s {
        if isvowel(byte(c)) {
            count++
        }
    }

    return count
}

func isvowel(s byte) bool {
    switch s {
        case 'a': return true
        case 'e' : return true
        case 'i' : return true
        case 'o' : return true
        case 'u' : return true
    }
    return false
}
