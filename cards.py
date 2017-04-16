import random


suits = ['spades','clubs','hearts','diamonds']
mini_suits = ['s','c','h','d']

values = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
mini_values = ['a','2','3','4','5','6','7','8','9','t','j','q','k']

regular_cards = True


class Card:
   def __init__(self, suit, value, face_up=True):
      self.__suit = suit
      self.__value = value
      self.__face_up = face_up

      try:
         assert self.__suit in suits
         assert self.__value in values
         assert self.__face_up in [True,False]
      except AssertionError:
         if regular_cards:
            print 'Warning: This card "{}" is not a regular playing card'.format(self)

   def __str__(self):
      if self.__face_up:
         return '{0} of {1}'.format(self.__value, self.__suit)
      else:
         return 'face down card'

   def as_mini_str(self):
      if self.__face_up:
          return mini_values[values.index(self.__value)] + mini_suits[suits.index(self.__suit)]
      else:
          return 'xx'

   def get_suit(self):
      return self.__suit

   def get_value(self):
      return self.__value

   def get_color(self):
       if self.__suit in ['hearts','diamonds']:
           return 'red'
       elif self.__suit in ['spades','clubs']:
           return 'black'
       else:
           return 'none standard color'

   def get_face_up(self):
      return self.__face_up

   def flip(self):
      self.__face_up = not self.__face_up


class Deck:
   def __init__(self):
      self.cards = []

   def __str__(self):
      s = "deck of {} cards:".format(len(self))
      for card in self.cards:
         s += '\n'
         s += str(card)
      return s

   def __len__(self):
      return len(self.cards)

   def __getitem__(self, key):
      return self.cards[key]

   def add_card(self, card):
      self.cards.append(card)

   def insert_card(self, i, card):
      self.cards.insert(i, card)

   def remove_card(self, card):
      self.cards.remove(card)

   def remove_card_atindex(self, index):
      del self.cards[index]

   def reverse(self):
      self.cards.reverse()

   def deal(self, number=1, retain_order=False):
      new_deck = Deck()
      for i in range(0, number):
         self.flip()
         new_deck.add_card(self.cards.pop())
         self.flip()
      new_deck.flip()
      if retain_order:
         new_deck.reverse()
      return new_deck

   def cut(self, number=52/2):
      return self.deal(number, retain_order=True)

   def flip(self, retain_order=False):
      for card in self.cards:
         card.flip()
      if not retain_order:
         self.cards.reverse()

   def extend(self, deck):
      self.cards.extend(deck.cards)

   def shuffle(self):
      random.shuffle(self.cards)


def create_standard_deck(face_up=False):
   d = Deck()
   for suit in suits:
      for value in values:
         d.add_card(Card(suit,value,face_up))
   return d
