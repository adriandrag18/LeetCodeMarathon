// title: Guess Number Higher or Lower
// timestamp: 2024-04-18 12:57:51
// problemUrl: https://leetcode.com/problems/guess-number-higher-or-lower/
// memory: 2.1 MB
// runtime: 0 ms

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    switch guess(n/2) {
        case 0:
            return n/2
        case -1:
            return guessNum(1, n/2 - 1)
        case 1:
            return guessNum(n/2 + 1, n)
    }
    return -1
}

func guessNum(low, high int) int {
    g := (low + high)/2
    switch guess(g) {
        case 0:
            return g
        case -1:
            return guessNum(low, g - 1)
        case 1:
            return guessNum(g + 1, high)
    }
    return -1
}