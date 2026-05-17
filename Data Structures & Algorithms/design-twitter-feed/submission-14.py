import datetime 

# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#         self.user_id_follows = [] 

#     def follows(self, user_id):
#         self.user_id_follows.append(user_id)

# class Tweet:
#     def __init__(self, tweet_id, user_id, date_posted):
#         self.tweet_id = tweet_id
#         self.user_id = user_id
#         self.date_posted = date_posted

class Twitter:

    def __init__(self):
        self.user_to_tweets = {}
        self.user_to_follows = {}     
        self.counter = 0

    # tweet ID is unique
    def postTweet(self, userId: int, tweetId: int) -> None:
        # new Tweet(tweetId, userId, date.today())
        if userId in self.user_to_tweets:
            # instead of using datetime, lets use counter now?
            self.user_to_tweets[userId].append((tweetId, self.counter))
        else:
            self.user_to_tweets[userId] = [(tweetId, self.counter)]
        self.counter += 1

    # At most 10 recent tweet IDs
    # should only show tweet from someone we follow
    # most recent to least recent... hmmmm
    def getNewsFeed(self, userId: int) -> List[int]:        
        if userId not in self.user_to_follows:
            self.user_to_follows[userId] = set()

        if userId not in self.user_to_tweets:
            self.user_to_tweets[userId] = []
        
        all_users_followed_by_userId = self.user_to_follows[userId] 
        tweets_by_users_followed_by_userId = self.user_to_tweets[userId].copy()
        for followed_user_id in all_users_followed_by_userId:
            if userId != followed_user_id:
                tweets_by_users_followed_by_userId.extend(self.user_to_tweets[followed_user_id])
        # Clean the tweets to 
        # Sort the list in descending order based on date_posted (second element of each tuple)
        sorted_data = sorted(tweets_by_users_followed_by_userId, key=lambda x: x[1], reverse=True)
        print("user_to_tweets", self.user_to_tweets)
        print("sorted_data", sorted_data)

        # Get the top 10 IDs with the latest dates
        top_10_ids = [x[0] for x in sorted_data[:10]]
        return top_10_ids


    # user followerId follows the user with ID followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        # new Tweet(tweetId, userId, date.today())
        if followerId != followeeId:
            if followerId in self.user_to_follows:
                self.user_to_follows[followerId].add(followeeId)
                print("checking follow", self.user_to_follows[followerId])
            else:
                self.user_to_follows[followerId] = set()
                self.user_to_follows[followerId].add(followeeId)

    # user followerId unfollows the user with ID followeeId    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user_to_follows and followeeId in self.user_to_follows[followerId]:
                self.user_to_follows[followerId].remove(followeeId)
            else:
                self.user_to_follows[followerId] = set()

