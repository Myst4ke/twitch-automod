import logging
from twitchio.ext import commands

#Configuration du logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d%H:%M:%S',
                    handlers=[logging.FileHandler('chat2.log', encoding='utf-8')])

class BotTwitch(commands.Bot):

    def init(self, token, client_id, nick, prefix, initial_channels):
        # Utilisation de super() pour appeler le init de la classe parent
        print("test")
        super().init(token=token, client_id=client_id, nick=nick, prefix=prefix, initial_channels=initial_channels)

    async def event_ready(self):
        logging.info('Bot ready')
        print('Bot is online!')
        channel = self.get_channel('myst_ake_')
        await channel.send('Bot ready')
    
    async def send_message(self, channel_name, message):
        channel = self.get_channel(channel_name)
        if channel:
            await channel.send(message)
        else:
            logging.error(f'Channel {channel_name} not found')

    async def event_message(self, message):
        # Ignorer les messages du bot lui-même et les messages sans auteur
        # print("test:", message.raw_data)
        if message.author is None or message.author.name.lower() == self.nick.lower():
            return

        logging.info(f'Message from {message.author.name}: {message.content}')
        print(f'Message from {message.author.name}: {message.content}')
        await self.send_message('myst_ake_', f'/ban {message.author.name.lower()}')
        


if __name__ == "__main__":
    bot = BotTwitch(
        token='oauth:uh5kqv0xgbzg0wigwqntrzugzyu0uq',  # Votre token d'authentification IRC
        client_id='fjl7df8lrcx65w8u42eme5bhxevdt0',  # Votre Client ID
        nick='teriad2024',  # Le nom de votre bot
        prefix='!',  # Le préfixe des commandes, par exemple !
        initial_channels=['myst_ake_']  # Les canaux sur lesquels le bot doit être actif
    )
    bot.run()
    