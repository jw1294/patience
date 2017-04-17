import cards


class BoardState:
   def __init__(self):
      # create deck
      deck = cards.create_standard_deck()
      deck.shuffle()

      # deal out face down cards
      self.face_down = []
      for i in range(0, 7):
         fd = deck.deal(i)
         self.face_down.append(fd)

      # deal out face up cards
      self.face_up = []
      for i in range(0, 7):
         fu = deck.deal()
         fu.flip(retain_order=True)
         self.face_up.append(fu)

      # put rest of cards into deck
      self.deck_down = deck

      # create blank deck to hold face up deck cards
      self.deck_up = cards.Deck()

      # Create 4 blank decks to represent stacks
      self.stacks = []
      for i in range(0, 4):
          self.stacks.append(cards.Deck())

   def __str__(self):
      s = ''
      for i in range(0, 4):
          try:
              s += self.stacks[i][0].as_mini_str() + ' '
          except IndexError:
              s += 'ss '
      s += '\n'
      for i in range(0, 7):
         for j in range(-1, -len(self.face_down[i])-1, -1):
            s += self.face_down[i].cards[j].as_mini_str() + ' '
         for j in range(-1, -len(self.face_up[i])-1, -1):
            s += self.face_up[i].cards[j].as_mini_str() + ' '
         s += '\n'
      s += '\n'
      try:
          s += self.deck_down[0].as_mini_str() + ' '
      except IndexError:
         s += '   '
      try:
         s += self.deck_up[0].as_mini_str()
      except IndexError:
         s += '   '
      s += '\n'
      return s

   # request to move a set of cards from place to place
   def move_cards(self, col_from, col_to, number):
      try:
         card1 = self.face_up[col_from][number-1]
         if len(self.face_up[col_to]) == 0 and len(self.face_down[col_to]) == 0:
            if card1.get_value() == 'king':
               deck = self.face_up[col_from].deal(number, retain_order=False)
               for card in deck:
                  self.face_up[col_to].insert_card(0, card)
               return 0
            else:
                return 1
         card2 = self.face_up[col_to][0]
         if card1.get_color() != card2.get_color():
            if cards.values.index(card1.get_value())+1 == cards.values.index(card2.get_value()):
               deck = self.face_up[col_from].deal(number, retain_order=False)
               for card in deck:
                  self.face_up[col_to].insert_card(0, card)
               return 0
            else:
                return 1
         else:
            return 1
      except:
          return 1

   # request a deal
   def deal(self):
      if len(self.deck_down) is 0:
         self.deck_down = self.deck_up.deal(len(self.deck_up), retain_order=True)
         self.deck_down.flip()
      elif len(self.deck_down) < 3:
         n_cards = self.deck_down.deal(len(self.deck_down), retain_order=True)
         n_cards.flip(retain_order=True)
         for card in three_cards:
            self.deck_up.insert_card(0, card)
      else:
         three_cards = self.deck_down.deal(3, retain_order=True)  
         three_cards.flip(retain_order=True)
         for card in three_cards:
             self.deck_up.insert_card(0, card)
      return 0

   # raise the top card of the face up deck to the main board
   def raise_card(self, col_to):
      try:
         card1 = self.deck_up[0]
         if len(self.face_up[col_to]) == 0 and len(self.face_down[col_to]) == 0:
            if card1.get_value() == 'king':
               deck = self.deck_up.deal(1, retain_order=False)
               for card in deck:
                  self.face_up[col_to].insert_card(0, card)
               return 0
            else:
                return 1
         card2 = self.face_up[col_to][0]
         if card1.get_color() != card2.get_color():
            if cards.values.index(card1.get_value())+1 == cards.values.index(card2.get_value()):
               deck = self.deck_up.deal(1, retain_order=False)
               for card in deck:
                  self.face_up[col_to].insert_card(0, card)
               return 0
            else:
                return 1
         else:
            return 1
      except:
          return 1

   # promote a card to one of the four main stacks
   def stack_card(self, col_from, stack_to):
      try:
         card1 = self.face_up[col_from][0]
         if len(self.stacks[stack_to]) == 0:
             if card1.get_value() == 'ace':
                 cards = self.face_up[col_from].deal(1, retain_order=False)
                 self.stacks[stack_to].insert_card(0, cards[0])
                 return 0
             else:
                 return 1
         card2 = self.stacks[stack_to][0]
         if card1.get_suit() == card2.get_suit():
            if cards.values.index(card1.get_value()) == cards.values.index(card2.get_value())+1:
               cards = self.face_up[col_from].deal(1, retain_order=False)
               self.stacks[stack_to].insert_card(0, cards[0])
               return 0
            else:
                return 1
         else:
            return 1
      except:
          return 1

   # flip a ready-to-flip colomn
   def flip(self, col):
      if len(self.face_up[col]) == 0 and  len(self.face_down[col]) != 0:
          cards = self.face_down[col].deal(1)
          cards.flip()
          self.face_up[col].insert_card(0, cards[0])
          return 0
      return 1


# return an initialed game of patience
def init_game():
   return BoardState()
