import requests
import bittensor as bt
from typing import List
from masa.miner.masa_protocol_request import MasaProtocolRequest
from masa.types.discord import DiscordChannelMessageObject


class DiscordChannelMessagesRequest(MasaProtocolRequest):
    def __init__(self):
        super().__init__()

    def get_discord_channel_messages(
        self, channel_id
    ) -> List[DiscordChannelMessageObject]:
        bt.logging.info(f"Getting channel messages from worker {channel_id}")

        # response = self.get(f"/data/discord/channels/{channel_id}/messages")

        # response_json = response.json()

        # if "error" in response_json:
        #     bt.logging.error("Worker request failed")
        #     return None

        # discord_channel_messages = self.format_channel_messages(response_json)
        discord_channel_messages = [
                    DiscordChannelMessageObject(**channel_message)
                    for channel_message in [
            {
                "ID": "111",
                "ChannelID": "222",
                "Author": discord_profiles[0],
                "Content": "Hello, this is a test message.",
                "Timestamp": "2024-07-12T12:34:56Z"
            },
            {
                "ID": "112",
                "ChannelID": "223",
                "Author": discord_profiles[1],
                "Content": "This is another test message.",
                "Timestamp": "2024-07-12T12:35:56Z"
            }
        ]
        ]
        return discord_channel_messages

    def format_channel_messages(
        self, data: requests.Response
    ) -> List[DiscordChannelMessageObject]:
        bt.logging.info(f"Formatting discord channel messages data: {data}")
        channel_messages_data = data["data"]
        discord_channel_messages = [
            DiscordChannelMessageObject(**channel_message)
            for channel_message in channel_messages_data
        ]
        return discord_channel_messages
