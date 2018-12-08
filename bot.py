import twitter, os, time

my_tok = 'token.tk'
cons_key = 'conk.tk'
if not os.path.isfile(my_tok):
    twitter.oauth_dance("My App Name", ckey, ckey_sec,my_tok)

tok, tok_sec = twitter.read_token_file(my_tok)
ckey, ckey_sec = twitter.read_token_file(cons_key)

api = twitter.Twitter(auth=twitter.OAuth(tok,
                      tok_sec,
                      ckey,
                      ckey_sec))

#api.statuses.update(status="I'm going to sleep... Tommorrow i'll have to plan out what i have to do... Good night..")

print(time.strftime("%Y%m%d-%H%M"))