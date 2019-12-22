# twitter_grab
Interacts with Twitter to display tweets.

A credentials.secret file is required to include your credentials.  It has to be in JSON format
much like the below - these are not valid credentials, but you could try them if you wish :-)

{
    "twitter_app_credentials":{
        "APIKey":"PUcdjfsdsbytu",
        "APISecret":"nTAEgBARUcZssfsdfsadf6osq8bj0LAjmgS1MBeDPn",
        "AccessToken":"164442224-2sdfsafsdfyIrMrxC3ihMJEDuQ0icWnt",
        "AccessTokenSecret":"sOhAv3Njgasdgsadggs68asfsdf2nQS8j"
    }
}

You have to register your app with Twitter.  https://developer.twitter.com/en/apps
This will result in credentials that you can put into you credentials.secret file. 

You will have to update the accounts you want to follow - you need to get their twitterid.  
I do this via a website - many are available. 

I think it is fairly obvious how to fill out the notable_tweeters file.  Last portion is the 
colour to use for the twitter accounts you are following.


