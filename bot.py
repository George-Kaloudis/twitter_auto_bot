import twitter, os, time

"""
Desktop
========
my_tok = 'token.tk'
cons_key = 'conk.tk'
if not os.path.isfile(my_tok):
    twitter.oauth_dance("My App Name", ckey, ckey_sec,my_tok)

tok, tok_sec = twitter.read_token_file(my_tok)
ckey, ckey_sec = twitter.read_token_file(cons_key)


"""



"""
Heroku
=======
"""
tok = os.environ['TOK']
tok_sec = os.environ['TOK_SEC']
ckey = os.environ['CKEY']
ckey_sec = os.environ['CKEY_SEC']


api = twitter.Twitter(auth=twitter.OAuth(tok,
                      tok_sec,
                      ckey,
                      ckey_sec))


#api.statuses.update(status="Test")

print(time.strftime("%Y%m%d-%H%M"))