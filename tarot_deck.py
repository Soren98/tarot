import json

from copy import deepcopy

from random import shuffle

cards = ['magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers', 'chariot', 'justice', 'hermit',
         'wheel of fortune', 'strength', 'hanged man', 'death', 'temperance', 'devil', 'tower', 'star', 'moon', 'sun',
         'judgement', 'world', 'fool', 'king of wands', 'queen of wands', 'knight of wands', 'page of wands',
         'ten of wands', 'nine of wands', 'eight of wands', 'seven of wands', 'six of wands', 'five of wands',
         'four of wands', 'three of wands', 'two of wands', 'ace of wands', 'king of cups', 'queen of cups',
         'knight of cups', 'page of cups', 'ten of cups', 'nine of cups', 'eight of cups', 'seven of cups',
         'six of cups', 'five of cups', 'four of cups', 'three of cups', 'two of cups', 'ace of cups', 'king of swords',
         'queen of swords', 'knight of swords', 'page of swords', 'ten of swords', 'nine of swords', 'eight of swords',
         'seven of swords', 'six of swords', 'five of swords', 'four of swords', 'three of swords', 'two of swords',
         'ace of swords', 'king of coins', 'queen of coins', 'knight of coins', 'page of coins', 'ten of coins',
         'nine of coins', 'eight of coins', 'seven of coins', 'six of coins', 'five of coins', 'four of coins',
         'three of coins', 'two of coins', 'ace of coins']
upright = {'magician': 'creativity, self-confidence, dexterity, sleight of hand,will-power, skill',
           'high priestess': 'knowledge, wisdom, learning, intuition, impatience, virtue, purity',
           'empress': 'development, accomplishment action, evolution',
           'emperor': 'authority, father-figure, structure, solid foundation',
           'hierophant': 'mercy, conformity, forgiveness, social approval, bonded, inspiration',
           'lovers': 'harmony, trust,romance, optimism, honor, love, harmony',
           'chariot': 'perseverance, rushed decision, turmoil, vengeance, adversity',
           'justice': 'equality, righteousness, virtue, honor, harmony, balance',
           'hermit': 'inner strength, prudence, withdrawal, caution, vigilance',
           'wheel of fortune': 'unexpected events, advancement, destiny, fortune, progress',
           'strength': 'courage, conviction, strength, determination, action, heroism, virility',
           'hanged man': 'change, reversal, boredom, improvement, rebirth, suspension, change',
           'death': 'unexpected change, loss, failure, transformation, death, bad luck',
           'temperance': 'temperance, patience, good influence, confidence, moderation',
           'devil': 'downfall, unexpected failure, controversy, ravage, disaster, ill tempered',
           'tower': 'downfall, unexpected failure, controversy, ravage, disaster, ill tempered',
           'star': 'balance, pleasure, optimism, insight, spiritual love, hope, faith',
           'moon': 'double-dealing Deception, disillusionment, trickery, error, danger, disgrace',
           'sun': 'accomplishment, success, love, joy, happy marriage, satisfaction',
           'judgement': 'awakening, renewal, rejuvenation, rebirth, improvement, promotion, atonement, judgment',
           'world': 'perfection, recognition, success, fulfillment, eternal life',
           'fool': 'beginnings possibilities, pleasure, thoughtlessness, adventure, opportunity',
           'king of wands': 'passionate, good leader, noble',
           'queen of wands': 'fondness, attraction, command	',
           'knight of wands': 'generous, journey, impetuous',
           'page of wands': 'enthusiasm, exploration, discovery, free spirit',
           'ten of wands': 'pain, ruined, failure',
           'nine of wands': 'victory, good health, obstinacy',
           'eight of wands': 'new ideas, love, journey',
           'seven of wands': 'stiff competition, victory, courage, energy',
           'six of wands': 'leadership, good news, success',
           'five of wands': 'lawsuit or quarrel, courage, competition',
           'four of wands': 'dissatisfaction, kindness, reevaluation	',
           'three of wands': 'cooperation, good partnership, success',
           'two of wands': 'generous person, courage, patience, courage	',
           'ace of wands': 'profitable journey, new business, beginning, new career, birth, inheritance',
           'king of cups': 'kindness, willingness, enjoyment',
           'queen of cups': 'loving mother, gentle, happiness',
           'knight of cups': 'emotional, romantic dreamer, intelligence',
           'page of cups': 'sweetness, interest in literature, gentleness',
           'ten of cups': 'friendship, happiness, life',
           'nine of cups': 'physical well-being, hopes, security',
           'eight of cups': 'disappointment, abandonment, misery',
           'seven of cups': 'imagination, illusion, directionless',
           'six of cups': 'acquaintance, good memories, acquaintance, happiness',
           'five of cups': 'broken marriage,vain regret, sorrow, loss',
           'four of cups': 'dissatisfaction, kindness, reevaluation, redemption',
           'three of cups': 'fortune, hospitality, discovery',
           'two of cups': 'romance, friendship, cooperation',
           'ace of cups': 'good health, love, joy, beauty',
           'king of swords': 'powerful, friendship, counselor',
           'queen of swords': 'skillful, brave, clever, rush',
           'knight of swords': 'strong man, braver, clever person',
           'page of swords': 'grace, diplomacy, dexterity, grace',
           'ten of swords': 'defeat, failure, pain',
           'nine of swords': 'desolation, illness, suspicion, cruelty',
           'eight of swords': 'weakness, indecision, censure',
           'seven of swords': 'betrayal, insolence, unwise attempt',
           'six of swords': 'harmony, sorrow, journey',
           'five of swords': 'defeat, cowardliness, empty victory',
           'four of swords': 'temporary exile, strife, retreat',
           'three of swords': 'broken relationship, civil war',
           'two of swords': 'indecision, trouble, balanced',
           'ace of swords': 'love, valiant, victory',
           'king of coins': 'reliable person, steadiness	',
           'queen of coins': 'thoughtfulness, intelligence, talents, melancholy	',
           'knight of coins': 'dull outlook, patience, animal lover, trustworthy	',
           'page of coins': 'kindness,new ideas/opinions, scholar	',
           'ten of coins': 'wealth, property, stability	',
           'nine of coins': 'solitude, well-being, green thumb	',
           'eight of coins': 'employment, money, learning, trade',
           'seven of coins': 'development, re-evaluation, effort, hard work	',
           'six of coins': 'prosperity, philanthropy, charity, gifts	',
           'five of coins': 'destitution, poor health, despair, loneliness	',
           'four of coins': 'ungenerous, greed, miserly	',
           'three of coins': 'abilities, approval,effort, abilities	',
           'two of coins': 'harmony, new projects, helpful	',
           'ace of coins': 'prosperity, happiness, pleasure'}
reverse = {'magician': 'delay, unimaginative, insecurity, lack of self-confidence',
           'high priestess': 'selfishness, shallowness, misunderstanding, ignorance',
           'empress': 'inaction, lack on concentration, vacillation, anxiety, infidelity',
           'emperor': 'domination, excessive control, rigidity, inflexibility',
           'hierophant': 'vulnerability, unconventionality, foolish generosity, impotence, frailty, unorthodoxy',
           'lovers': 'separation, frustration, unreliability,fickleness, untrustworthy',
           'chariot': 'vanquishment, defeat, failure, unsuccessful',
           'justice': 'alse accusation, unfairness, abuse, biased',
           'hermit': 'hastiness, rashness,immaturity, imprudence, foolishness',
           'wheel of fortune': 'interruption, outside influences, failure, bad luck',
           'strength': 'pettiness, sickness, unfaithfulness, weakness',
           'hanged man': 'alse prophecy, useless sacrifice, unwillingness',
           'death': 'immobility, slow changes, cheating, death, stagnation',
           'temperance': 'conflict, disunion, frustration, impatience, discord',
           'devil': 'release, enlightenment, divorce, recovery',
           'tower': 'entrapment, imprisonment, old ways, rustic',
           'star': 'disappointment, bad luck, imbalance, broken dreams',
           'moon': 'trifling mistakes, deception discovered, negative advantage',
           'sun': 'loneliness, canceled plans, unhappiness, break ups',
           'judgement': 'disappointment, indecision, death, failure, ill-health, theft, worry',
           'world': 'ack of vision, disappointment, imperfection',
           'fool': 'indecision, hesitation, injustice, apathy, bad choice',
           'king of wands': 'unyielding, prejudice, quarrels',
           'queen of wands': 'jealous, revengeful, infidelity',
           'knight of wands': 'suspicion, jealousy, narrow-mindedness',
           'page of wands': 'setbacks to new ideas, pessimism, lack of direction',
           'ten of wands': 'cleverness, energy, strength',
           'nine of wands': 'weakness, ill-health, adversity',
           'eight of wands': 'violence, quarrels, courage',
           'seven of wands': 'advantage, patience, indecision',
           'six of wands': 'postponement, bad news, pride in riches',
           'five of wands': 'new opportunities, harmony, generosity',
           'four of wands': 'new relationship, new ambitions, action',
           'three of wands': 'carelessness, arrogance, pride, mistakes',
           'two of wands': 'impatience, domination',
           'ace of wands': 'selfishness, lack of determination, setback',
           'king of cups': 'double-dealer, scandal, crafty, violent',
           'queen of cups': 'perverse, unhappy, gloom, over-active imagination',
           'knight of cups': 'idleness, untruthful, fraud, sensuality',
           'page of cups': 'poor imagination, selfishness, no desires',
           'ten of cups': 'waste, broken relationships, quarrel',
           'nine of cups': 'illness, failure, overindulgence',
           'eight of cups': 'pleasure, success, joy',
           'seven of cups': 'will-power, determination',
           'six of cups': 'friendship, disappointment, past',
           'five of cups': 'return, summon, hope',
           'four of cups': 'new goals, ambitions, beginning',
           'three of cups': 'hidden, overindulgence, pain, gossip',
           'two of cups': 'violent passion, misunderstanding',
           'ace of cups': 'egotism, selfishness, hesitancy',
           'king of swords': 'obstinate, evil intentions, judgments',
           'queen of swords': 'sly, keen, deceitful',
           'knight of swords': 'troublemaker, a crafty, tyranny',
           'page of swords': 'imposture, ill-health, cunningness',
           'ten of swords': 'courage, positive energy, good health',
           'nine of swords': 'unselfishness, good news, healing',
           'eight of swords': 'freedom, new beginnings, relaxation',
           'seven of swords': 'counsel, helpful, advice',
           'six of swords': 'obstacles, difficulties, defeat',
           'five of swords': 'unfairness, defeat, loss',
           'four of swords': 'social unrest, labor strikes, renewed activity',
           'three of swords': 'sorrow, loss, confusion',
           'two of swords': 'unscrupulous, release',
           'ace of swords': 'obstacles, tyranny, power',
           'king of coins': 'bribes, materialistic, calm',
           'queen of coins': 'mistrust, suspicion, neglect',
           'knight of coins': 'carelessness, standstill, irresponsible',
           'page of coins': 'luxury, rebellious, bad news',
           'ten of coins': 'dull, slothfulness, misfortune',
           'nine of coins': 'caution, possible loss',
           'eight of coins': 'void, no ambition, dislike',
           'seven of coins': 'impatience, slow progress, investments',
           'six of coins': 'jealousy, miserliness, unfairness',
           'five of coins': 'employment, courage, revival',
           'four of coins': 'spendthrift, obstacles, earthy possessions',
           'three of coins': 'preoccupation, ambitions',
           'two of coins': 'difficulty, discouragement',
           'ace of coins': 'misery, greedy, money'}


class TarotDeck:
    def __init__(self):
        self.deck = None
        self.reset()

    def draw(self):
        if len(self.deck) == 0:
            return 'the deck is empty. use !tarot reset to reset the deck', None
        card = self.deck.pop()
        ret = []
        if card in {'justice', 'strength', 'death', 'temperance', 'judgement'}:
            ret.append('you drew {}'.format(card))
        ret.append('you drew the {}'.format(card))
        ret.append('upright meaning: {}'.format(upright[card]))
        ret.append('reverse meaning: {}'.format(reverse[card]))
        return '\n'.join(ret), '{}.jpg'.format(card.replace(' ', '_'))

    def reset(self):
        self.deck = deepcopy(cards)
        shuffle(self.deck)
        return 'tarot deck reset'

    def save(self, save_path):
        with open(save_path, 'w') as file:
            json.dump(self.deck, file)
        print('saved deck')

    def load(self, load_path):
        with open(load_path, 'r') as file:
            self.deck = json.load(file)
        print('loaded deck')
