// title: Keys and Rooms
// timestamp: 2024-04-20 23:24:34
// problemUrl: https://leetcode.com/problems/keys-and-rooms/
// memory: 3.9 MB
// runtime: 6 ms

func canVisitAllRooms(rooms [][]int) bool {
    seen := map[int]bool{0: true}
    queue := rooms[0]
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        seen[node] = true
        for _, n := range rooms[node] {
            if _, ok := seen[n]; ok {
                continue
            }
            queue = append(queue, n)
        }
    }
    
    for i := 0; i < len(rooms); i++ {
        if _, ok := seen[i]; !ok {
            return false
        } 
    }
    return true
}