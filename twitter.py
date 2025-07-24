class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.post_map = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post_map:
            self.post_map[userId] = []
        self.timestamp += 1
        self.post_map[userId].append((-self.timestamp, tweetId))
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # if userId in self.follow_map:
        #     print(self.follow_map[userId])
        heap = []
        if userId in self.post_map:
            heap.extend(self.post_map[userId][-10:])
        if userId in self.follow_map:
            for followeeId in self.follow_map[userId]:
                if followeeId in self.post_map:
                    heap.extend(self.post_map[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.unfollow(followerId, followeeId)
        if followerId not in self.follow_map:
            self.follow_map[followerId] = [followeeId]
        else:
            self.follow_map[followerId].append(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)