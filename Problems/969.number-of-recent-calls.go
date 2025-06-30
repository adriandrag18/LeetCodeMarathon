// title: Number of Recent Calls
// timestamp: 2024-04-18 00:59:15
// problemUrl: https://leetcode.com/problems/number-of-recent-calls/
// memory: 7.6 MB
// runtime: 116 ms

type RecentCounter struct {
    queue []int
}

func Constructor() RecentCounter {
    return RecentCounter{}
}


func (this *RecentCounter) Ping(t int) int {
    this.queue = append(this.queue, t)
    for t - this.queue[0] > 3000 {
        this.queue = this.queue[1:len(this.queue)]
    }
    return len(this.queue)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */