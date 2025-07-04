# title: Design Twitter
# timestamp: 2025-01-02 19:51:39
# problemUrl: https://leetcode.com/problems/design-twitter/
# memory: 27.6 MB
# runtime: 6350 ms

class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.count, tweetId, userId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.tweets)
        count = 10
        tweets = []
        for tweet in self.tweets[::-1]:
            if (userId not in self.follows or tweet[2] not in self.follows[userId]) and tweet[2] != userId:
                continue
            tweets.append(tweet[1])
            count -= 1
            if count == 0:
                break
        
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = self.follows.get(followerId, set())
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)