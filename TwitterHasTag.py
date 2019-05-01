
class HasTagFilter:

    def __init__(self,tweets):
        self.tweets = tweets

    def getRelatedTweets(self, keyword):
        found_tweets = []
        for tweet in self.tweets:
            words = tweet.split(" ")
            for word in words:
                if(word == '#'+keyword):
                    found_tweets.append(tweet)
                    break

        if(len(found_tweets) == 0):
            print("|-------------------------------------------------------------------------------------------|")
            print('can not find any tweet related to this keyword')
        else:
            print('There are ' + str(len(found_tweets)) + " total tweets with this keyword")
            print("|-------------------------------------------------------------------------------------------|")
            for tweet in found_tweets:
                print('******' + tweet)
                print("|-------------------------------------------------------------------------------------------|")

test_data = [
    'President Donald Trump made it out of the congress without any hitch, #America #Trump',
    'Today is first of may, the Nigeria workers day #workersDay',
    'Presidency congratulates workers on workers day, #workersDay'
]

HasTagFilter(test_data).getRelatedTweets('workersDay')