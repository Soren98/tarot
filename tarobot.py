import sys

from os.path import exists

from discord import Client, File, DMChannel

from tarot_deck import TarotDeck

from cleanup import register_exit_fun

client = Client()
tarot_deck = TarotDeck()
save_path = 'deck.json'
if exists(save_path):
    tarot_deck.load(save_path)


def cleanup():
    tarot_deck.save(save_path)


register_exit_fun(cleanup)


@client.event
async def on_message(message):
    if message.author == client.user or isinstance(message.channel, DMChannel):
        return
    auth = str(message.author)
    content = str(message.content)
    channel = message.channel
    # hardcoded so only i can kill the bot
    if content == '!tarot kill' and message.author.id == 480300800518782996:
        await client.logout()
    elif content == '!tarot help':
        await channel.send(
            "commands are: **!tarot draw**, **!tarot reset**, **!tarot cards left**, **!hello**\n"
            "add a number to the draw command to draw multiple cards. ex: **!tarot draw 3**")
    elif content == '!hello':
        print('{} greet'.format(auth))
        await channel.send('Fuck off {}, ya cunt!\n'.format(str(auth)))
    elif content.startswith('!tarot draw'):
        num_cards = 1
        try:
            if len(content) > 12:
                num_cards = int(content[12:])
        except ValueError:
            await channel.send("{} ain't a number, idiot".format(content[12:]))
            return
        print('{} draw {}'.format(auth, num_cards))
        for _ in range(num_cards):
            reply, attachment = tarot_deck.draw()
            if attachment:
                await channel.send(reply, file=File(attachment))
            else:
                await channel.send(reply)
                break
    elif content == '!tarot reset':
        print('{} reset'.format(auth))
        await channel.send(tarot_deck.reset())
    elif content == '!tarot cards left':
        print('{} checked how many cards left'.format(auth))
        await channel.send('there are {} cards left in the tarot deck'.format(len(tarot_deck.deck)))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

assert len(sys.argv) == 2, "must provide only one input, the bot's token"
TOKEN = sys.argv[1]
client.run(TOKEN)
