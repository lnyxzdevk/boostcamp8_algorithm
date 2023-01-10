from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follow_list= defaultdict(list)
        self.upload_list = defaultdict(list)
        self.check = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.upload_list[userId].append((self.check,tweetId))
        self.check += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        for following in self.follow_list[userId]:
            output += self.upload_list[following]
        output += self.upload_list[userId]
        output.sort(reverse=True)
        tmp = []
        for s in output[:10]:
            tmp.append(s[-1])
        return tmp

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_list[followerId]:
            self.follow_list[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId] :
            self.follow_list[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)