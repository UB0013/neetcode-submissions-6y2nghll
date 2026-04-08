class Twitter:
    def __init__(self):
        self.count = 0 
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count +=1 
    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        maxheap = []
        self.followmap[userId].add(userId)
        for user in self.followmap[userId] : 
            if user in self.tweetmap : 
                index = len(self.tweetmap[user])-1
                count , tweetid= self.tweetmap[user][index]
                heapq.heappush_max(maxheap,[count, tweetid,user,index-1])
        while maxheap and len(res) < 10 :
            count, tweetid, user,index = heapq.heappop_max(maxheap)
            res.append(tweetid)
            if index >= 0 :
                count, tweetid  = self.tweetmap[user][index]
                heapq.heappush_max(maxheap,[count, tweetid, user,index-1])
        return res
            

        
                        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]: 
            self.followmap[followerId].remove(followeeId)
        
