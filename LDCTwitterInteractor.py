from tweepy.auth import OAuthHandler
import datetime, tweepy
#Twitter API App Settings:
#Consumer Key for Twitter
consumerKey="MYCONSUMERKEY"
#Consumer Secret for Twitter
consumerSecret="MYCONSUMERSECRETKEY"
#Access Token for Twitter
accessToken= "MYACCESSTOKEN"
#Access Token Secret for Twitter
accessTokenSecret="MYACCESSTOKENSECRET"

def connectToTwitter():
    #Connecting to Twitter, using the credentials specified above.
    authentication = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authentication.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authentication)
    return api

def getTweets():
    #This function will get the first 10 tweets by the people who you follow on Twitter from your timeline.

    api = connectToTwitter();
    print("Hello " + api.me().name + "\nHave a look at first 10 tweets of your timeline:\n")

    publicTweets = api.home_timeline()
    counter = 0
    users = []
    allTweeters = ""
    tweets = ""

    #Getting the Tweets from timeline and displaying them on the screen(terminal).
    for tweet in publicTweets:
        users.append(tweet.user.name)
        tweets = tweets + tweet.user.name + ": " + tweet.text + "\n"
        counter = counter + 1
        if counter > 9:
            for user in list(set(users)):
                allTweeters = allTweeters + user + ", "
            allTweeters = "The following users: "+ allTweeters + "have tweeted on Twitter.\n"
            break
    print(allTweeters)
    print(tweets)

def getTime():
    #This function will return time.
    curTime = datetime.datetime.now()
    return "It is currently, " + curTime.strftime("%A, %d %B %Y %I:%M%p") + ".\n"

print(getTime());
getTweets();

