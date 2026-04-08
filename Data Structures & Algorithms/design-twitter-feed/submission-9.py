class Twitter:

    def __init__(self):
        self.tweetmap = defaultdict(list)
        # set already sorts it based on count 
        self.followmap = defaultdict(set)
        self.count = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId,userId])
        self.count += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result =[]
        self.followmap[userId].add(userId)
        for followeduserid in self.followmap[userId]:
            if followeduserid in self.tweetmap:
                index = len(self.tweetmap[followeduserid])-1
                rank, tweetfeedid, userid  = self.tweetmap[followeduserid][index]
                heapq.heappush_max(heap,[rank,tweetfeedid, userid , index-1])
        while heap and len(result) < 10  :
            rank,tweetfeedid, userid ,index =heapq.heappop(heap)
            result.append(tweetfeedid)
            if index >=0 : 
                rank, tweetfeedid, userid = self.tweetmap[userid][index]
                heapq.heappush_max(heap,[rank,tweetfeedid,userid,index-1])
        return result




    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

        
