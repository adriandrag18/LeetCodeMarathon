// title: Reverse Integer
// timestamp: 2024-04-24 11:53:07
// problemUrl: https://leetcode.com/problems/reverse-integer/
// memory: 2.3 MB
// runtime: 0 ms

func reverse(x int) int {
    const threashold = 214748364
    var in, out int32 = int32(x), 0
    for in != 0 {
        out *= 10
        out += in%10
        in /= 10

        if in != 0 && (out > threashold || out < -threashold) {
            return 0
        }
    }
    
    return int(out)
}