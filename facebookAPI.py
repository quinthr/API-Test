import os
import json
import facebook

if __name__ == '__main__':
    token = os.environ.get('FACEBOOK_TEMP_TOKEN')
    if token is None:
        #enter your token in token2 = "mytoken"
        token2 = "EAACaNLQYpNEBAEI5XBkuWo1grvJzpXgpeLDUClj9M0boHTgmUm3GNKa2v7AY9PGGaBHe3yCPe65zkXzIkgFQ1FmrGPNnmuUU3fvltZCKWhXqc45rAsN75QKq3pgx5X0Eg3B3g4kYqrD1KNAqWpvv8Ho1ZBJhyCTMvojgdspjPFCTs3GAjF6jpZAJbKWp7GwjIwPolxPvQZDZD"
        graph = facebook.GraphAPI(access_token=token2)
        profile = graph.get_object('me', fields='name,location,birthday,gender,link,languages')
        user = graph.get_object("me")
        friends = graph.get_connections(user["id"], "friends")
        print(json.dumps(profile, indent=3))
        print(json.dumps(friends, indent=3))
    else:
        graph = facebook.GraphAPI(access_token=token)
        profile = graph.get_object('me', fields='name,location,birthday,gender,link,languages')
        user = graph.get_object("me")
        friends = graph.get_connections(user["id"], "friends")
        print(json.dumps(profile, indent=3))
        print(json.dumps(friends, indent=3))