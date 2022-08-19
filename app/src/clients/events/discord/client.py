#!/usr/bin/env python3
"""
Discord-Client Class
This class handles all interactions with the Discord-Client

Author: Jason Cabezuela
"""
import src.clients.events.client as EventClient
import src.clients.events.discord.config as DiscordConfiguration
import asyncio
import concurrent.futures
import discord


class DiscordClient(EventClient.EventClient):
    """Discord-Client Class"""
    def __init__(self, configpath, configtype):
        print("INIT DiscordClient")
        EventClient.EventClient.__init__(self, configpath, configtype)
        self._client = discord.Client()

        @self._client.event
        async def on_ready():
            print('DiscordClient logged in as {0.user}'.format(self._client))            

        @self._client.event
        async def on_message(message):
            if message.author == self._client.user:
                return

            if message.content.startswith(self.cmdSymbol):
                self._add_newMessage(message.content[1:], message.author)
                if message.content == "!exit":
                    await self._client.logout()
#                await message.channel.send(self.prompt + 'Hello!')
        print('INIT_END DiscordClient')


    async def startup(self):
        """async-func for DiscordClient login() and connect()"""
        _credentials = self._getCredentials()
        try:
            _token = _credentials[0].rstrip()
            self._root = _credentials[1]
        except:
            print("Missing either Discord Token or UserID in \"/config/tokens/\" -> Discord-Client is NOT running!")
            return
        loop = asyncio.get_running_loop()
        try:
            await self._client.login(_token, bot=True)
            await loop.run_in_executor(None, await self._client.connect())
        except discord.LoginFailure:
            print("ERROR DISCORD: Discord-Token seems to be wrong!")
        except discord.HTTPException:
            print("ERROR DISCORD: An unknown HTTP related error occurred.")
        except:
            print("ERROR Discord Client - login failed!")
        
