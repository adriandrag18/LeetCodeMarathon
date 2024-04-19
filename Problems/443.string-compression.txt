// title: String Compression
// timestamp: 2024-04-19 23:10:31
// problemUrl: https://leetcode.com/problems/string-compression/
// memory: 3 MB
// runtime: 5 ms

func compress(chars []byte) int {
    switch len(chars) {
    case 0:
        return 0
    case 1:
        return 1
    }

    start, i, occ := 0, 1, 1
    char := chars[0]
    for i < len(chars) {
        if chars[i] == char {
            occ++
            i++
            continue
        }
        if occ == 1 {
            char = chars[i]
            start++
            i++
            continue
        }
        occBytes := []byte{}
        for occ != 0 {
            occBytes = append([]byte{byte((occ%10)+'0')}, occBytes...)
            occ /= 10
        }

        chars = append(append(chars[:start + 1], occBytes...), chars[i:]...)
        start += len(occBytes) + 1
        i, occ, char = start + 1, 1, chars[start]
    }

    if occ == 1 {
        return len(chars)
    }

    occBytes := []byte{}
    for occ != 0 {
        occBytes = append([]byte{byte((occ%10)+'0')}, occBytes...)
        occ /= 10
    }

    chars = append(chars[:start + 1], occBytes...)

    return len(chars)
}