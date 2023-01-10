from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets=[]
        self.followers=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        count=0
        newsList=[]
        copytweets=self.tweets[:]
        while copytweets:
            ui,ti=copytweets.pop()
            if ui in self.followers[userId] or userId==ui:
                count+=1
                newsList.append(ti)
                if count==10:
                    break
        return newsList


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]: 
            self.followers[followerId].remove(followeeId)