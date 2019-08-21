from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['alface'],['tomate']) # let's define all words we would like to have a look for
    tso.set_language('pt') # we want to see Brasil tweets only
    tso.set_geocode(-23.560667,-46.624279,35,imperial_metric=False)
    tso.set_include_entities(False)
    f = open("demoTwitter.txt", "w", encoding="utf-8")
    

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'TUo7W2voi1bQ1AZGzCPmw73jb',
        consumer_secret = 'Ttl4aNxO8UyTCd4nfZ0VIBdVnAnIyZ06QztUbcrSKBXMtdW2Qk',
        access_token = '268042601-ZIKDaKRhT7vdAFgb8WS1nZqDSD3NDXNja0klRaiN',
        access_token_secret = 'jiqH3Lhbogtz9pHGC70hfOIyWK7QQ1regeSWvnPdvqs8D'
     )
    numbertweets = 0;
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        writeVariable = str( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        f.write(writeVariable+"%n")
        print(writeVariable)
        if (numbertweets == 30):
            break;
        numbertweets = numbertweets + 1;
    f.close()


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)