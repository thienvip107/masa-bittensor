import requests
import bittensor as bt
from masa.miner.masa_protocol_request import MasaProtocolRequest
from masa.types.twitter import TwitterProfileObject


class TwitterProfileRequest(MasaProtocolRequest):
    def __init__(self):
        super().__init__()

    def get_profile(self, profile) -> TwitterProfileObject:
        bt.logging.info(f"Getting profile from worker {profile}")
        # response = self.get(f"/data/twitter/profile/{profile}")

        # if response.status_code == 504:
        #     bt.logging.error("Worker request failed")
        #     return None
        # twitter_profile = self.format_profile(response)

        return TwitterProfileObject(**{
        "UserID": profile+"192",
        "Avatar": "https://example.com/avatar1.jpg",
        "Banner": "https://example.com/banner1.jpg",
        "Biography": "This is a bio.",
        "Birthday": "1990-01-01",
        "FollowersCount": 1200,
        "FollowingCount": 300,
        "FriendsCount": 150,
        "IsPrivate": False,
        "IsVerified": True,
        "Joined": "2010-05-01",
        "LikesCount": 500,
        "ListedCount": 10,
        "Location": "New York, USA",
        "Name": "John Doe",
        "PinnedTweetIDs": ["tweet1", "tweet2"],
        "TweetsCount": 1000,
        "URL": "https://example.com",
        "Username": profile,
        "Website": "https://johndoe.com"
    })

    def format_profile(self, data: requests.Response) -> TwitterProfileObject:
        bt.logging.info(f"Formatting twitter profile data: {data}")
        profile_data = data.json()["data"]
        twitter_profile = TwitterProfileObject(**profile_data)

        return twitter_profile
