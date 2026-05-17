class Tweet:
    def __init__(self, tweetId, lastUpdate):
        self.tweetId = tweetId
        self.lastUpdate = lastUpdate

class Twitter:

    def __init__(self):
        self.userid_to_followeeId = {} # user id to set
        self.userid_to_tweetId = {}
        self.lastUpdate = 1

    def instantiateUser(self, userId):
        if userId not in self.userid_to_followeeId:
            self.userid_to_followeeId[userId] = set()
        
    def instantiateTweet(self, userId):
        if userId not in self.userid_to_tweetId:
            self.userid_to_tweetId[userId] = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        # When I post, I instantiate the user and the tweets
        self.instantiateUser(userId)
        self.instantiateTweet(userId)

        self.userid_to_tweetId[userId].add(Tweet(tweetId, self.lastUpdate))
        self.lastUpdate += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get the news feed
        allTweets = []
        # I get my own tweet first
        allTweets.extend(self.userid_to_tweetId[userId])

        # Check my followers, get their tweets
        for followeeId in self.userid_to_followeeId[userId]:
            allTweets.extend(self.userid_to_tweetId[followeeId])
        
        # I wanna sort the tweets from highest .lastUpdate, return .tweetId
        allTweets.sort(key = lambda x: x.lastUpdate, reverse = True)

        return [tweet.tweetId for tweet in allTweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        # Instantiate the user and the tweet
        self.instantiateUser(followerId)
        self.instantiateTweet(followerId)

        if followerId != followeeId:
            self.userid_to_followeeId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # I have to make sure I am not following this person to begin with
        if followeeId in self.userid_to_followeeId[followerId]:
            self.userid_to_followeeId[followerId].remove(followeeId)

        
