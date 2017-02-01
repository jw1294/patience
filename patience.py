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
   
   def __str__(self):
      s = ''
      for i in range(0, 7):
         for j in range(0, len(self.face_down[i])):
            s += self.face_down[i].cards[j].as_mini_str() + ' '
         for j in range(0, len(self.face_up[i])):
            s += self.face_up[i].cards[j].as_mini_str() + ' '
         s += '\n'
      s += '\n'
      s += self.deck_down[0].as_mini_str() + ' '
      try:
         s += self.deck_up[0].as_mini_str()
      except IndexError:
         s += '  '
      s += '\n'
      return s
      
   def move_card(self):
      pass
      #TODO
      
   def deal(self):
      pass
      #TODO


def init_game():
   return BoardState()
