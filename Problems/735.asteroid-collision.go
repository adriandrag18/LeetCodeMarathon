// title: Asteroid Collision
// timestamp: 2024-04-18 01:16:55
// problemUrl: https://leetcode.com/problems/asteroid-collision/
// memory: 4.9 MB
// runtime: 8 ms

import "fmt"

func asteroidCollision(asteroids []int) []int {
    var res []int
    for i := 0; i < len(asteroids); i++ {
        if asteroids[i] < 0 {
            var eq bool
            for len(res) != 0 {
                if res[len(res)-1] < 0 {
                    res = append(res, asteroids[i])
                    break
                }
                if res[len(res)-1] < -asteroids[i] {
                    res = res[0:len(res)-1]
                    continue
                }
                if res[len(res)-1] == -asteroids[i] {
                    res = res[0:len(res)-1]
                    eq = true
                }
                break
            }
            fmt.Println(len(res) == 0, !eq)
            if len(res) == 0 && !eq {
                res = append(res, asteroids[i])
            }
            continue
        }

        res = append(res, asteroids[i])
    }
    return res
}