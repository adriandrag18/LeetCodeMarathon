// title: Can Place Flowers
// timestamp: 2024-04-18 01:28:59
// problemUrl: https://leetcode.com/problems/can-place-flowers/
// memory: 6.5 MB
// runtime: 14 ms

func canPlaceFlowers(flowerbed []int, n int) bool {
    switch len(flowerbed) {
        case 0:
            return n == 0
        case 1:
            return n == 0 || (n == 1 && flowerbed[0] == 0)
    }
    if len(flowerbed) <= n {
        return false
    }

    var count int
    if flowerbed[0] == 0 && flowerbed[1] == 0 {
        count++
        flowerbed[0] = 1
    }

    for i := 1; i < len(flowerbed) - 1; i++ {
        if flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0 {
            count++
            flowerbed[i] = 1
        }
    }

    if flowerbed[len(flowerbed) - 2] == 0 && flowerbed[len(flowerbed) - 1] == 0 {
        count++
    }

    return count >= n
}