#!/usr/bin/env python3
"""StickyDJ-Bot Class
This is the Main-Class where all the modules come together.
It handles how they interact with each other.

Author: Jason Cabezuela
"""
import asyncio
import src.botfoundation as BotFoundation
import src.clients.events.discord.client as DiscordClient
import tracemalloc
#import src.clients.events.twitch.client as TwitchClient


class StickyDJ_Bot(BotFoundation.MasterConfig):
    def __init__(self):
        print("INIT StickyDJ")

        BotFoundation.MasterConfig.__init__(self)
        
        print("INIT_END StickyDJ")


    def get_messages(self):
            #print("PRINTED FROM GET_MESSAGE()")
            messageList = []
            for client in self._clientContext:
                if self._clientContext.get(client).get('enable') == True:
                    author = None
                    message = None

                    if client == 'discord':
                        author, message = self._DiscordClient.get_newMessage()
#                    elif client == "twitch":
#                        author, message = self._TwitchClient.get_newMessage()

                    if message is not None:
                        messageContext = (client, author, message)
                        messageList.append(messageContext)

            return messageList


    def get_context(self, messageContext):
        client = str(messageContext[0])
        author = str(messageContext[1])
        message = str(messageContext[2])
        print("RECV %s - %s: %s" %(client, author, message))
        usergroups = self._UserHandler.get_userProperties(author, client, "groups")

        # The following code currently produces errors, since the used handler-classes have not yet been implemented
        try:
            self._PermissionHandler.get_permissions(usergroups)
            commandContext = self._MessageParser(message)
            return (client, userlvl, commandContext)
        except:
            print("PERMISSIONHANDLER AND MESSAGE_PARSER ERROR (not implemented?)")
        

    async def run_loop(self):
        while self._shutdown is False:

            messageList = self.get_messages()
            while(messageList):
                messageContext = messageList.pop()
                context = self.get_context(messageContext)
                
                if messageContext[2] == 'exit':
                    self._shutdown = True

            await asyncio.sleep(0.01) # This is needed 


    async def client_startup(self, client):
        # Checks for enabled Clients and initializes their Classes
        if self._clientContext.get(client).get('enable') is True:
            if client == 'discord':
                self._DiscordClient = DiscordClient.DiscordClient(self._clientContext.get(client).get('path'),
                                                                  self._clientContext.get(client).get('type'))
                await self._DiscordClient.startup()
            elif client == 'twitch':
                print("TWITCH NOT YET SUPPORTED")
#                self._TwitchClient = TwitchClient.TwitchClient(self._clientConfigs.get(client), self._clientConfType.get(client))
#                await self._TwitchClient.startup()
              

    async def bot_startup(self):
        await asyncio.gather(
            self.client_startup('discord'),
            self.client_startup('twitch'),
            self.run_loop()
        )

    def getShutdown(self):
        return self._shutdown


if __name__ == "__main__":
    def run():
        tracemalloc.start()
        process = StickyDJ_Bot()
        eventloop = asyncio.get_event_loop()

        if process.getShutdown() == True:
            print("Shutting down")
            return
        
        try:
            eventloop.run_until_complete(process.bot_startup())
        except KeyboardInterrupt:
            print("ByeBye")
    
    run() 
    input("Press 'Enter' to exit")