import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"] for rank in range(1, 14)]
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, num_cards):
        for _ in range(num_cards):
            card = deck.draw()
            if card:
                self.hand.append(card)
            else:
                print("No more cards in the deck.")

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        else:
            print("Invalid index.")
            return None

class TrancaGame:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def deal_initial_cards(self):
        self.player1.draw_cards(self.deck, 9)
        self.player2.draw_cards(self.deck, 9)

    def play(self):
        self.deal_initial_cards()
        turn = 1
        while True:
            print(f"Turn {turn}:")
            self.player1.show_hand()
            index = int(input("Player 1, choose index of card to play (0-8): "))
            card = self.player1.play_card(index)
            if not card:
                break
            print(f"Player 1 plays {card}")
            self.player2.draw_cards(self.deck, 1)
            self.player2.show_hand()
            index = int(input("Player 2, choose index of card to play (0-8): "))
            card = self.player2.play_card(index)
            if not card:
                break
            print(f"Player 2 plays {card}")
            self.player1.draw_cards(self.deck, 1)
            turn += 1

def main():
    print("Welcome to the game of Tranca!")
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    game = TrancaGame(player1_name, player2_name)
    game.play()

if __name__ == "__main__":
    main()
