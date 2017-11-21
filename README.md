# sleepNaFriend Bot

This bot runs for [@sleepNaFriend Twitter account](twitter.com/sleepNaFrieind), which tells my night owl friend to go to sleep when she spends her night on Twitter.

## Usage

Create a `credentials.py` file with the structure like this:
```
api_key = '' # Your API Key
api_secret = '' # Your API Secret
token_key = '' # Your app token key
token_secret = '' # Your app token secret
```

In `tweets.py`, change the value of following variables

```
bot_target = 'desired_username' # Target username
debug = False # Set to `True` to dismiss the timer. (0AM - 4AM)
```

and run `tweets.py` to keep the bot running.
