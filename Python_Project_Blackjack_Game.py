#Python_Project_Blackjack_Game
#Developed By: Hasan Samir Hasan
#AMIT AI Online 75
import random
import os

#Clean the game screen
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# Card Class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class
class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                value += 11
                aces += 1
            else:
                value += int(card.rank)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

# Player Class
class Player:
    def __init__(self, money=100):
        self.money = money
        self.hand = Hand()

    def place_bet(self, amount):
        if amount > self.money:
            print("You don't have enough money!")
            return False
        self.money -= amount
        return True

    def win_bet(self, amount):
        self.money += amount * 2

    def __str__(self):
        return f"Player's hand: {self.hand} (Value: {self.hand.calculate_value()})"

# Dealer Class
class Dealer(Hand):
    def __str__(self):
        return f"Dealer's hand: {self.cards[0]}, [Hidden Card]"

# Game Class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start_round(self):
        welcome_msg="""
        Welcome to Blackjack Game (Not HALAL)!
        This Game is only developed for practicing OOP programming.
        """
        print(f"{welcome_msg} \nYou have ${self.player.money}.")
        bet = int(input("Place your bet: "))
        if not self.player.place_bet(bet):
            return
        # Deal initial cards
        self.player.hand = Hand()
        self.dealer = Dealer()
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

        print(self.dealer)
        print(self.player)

        # Player's turn
        while self.player.hand.calculate_value() < 21:
            action = input("Do you want to hit or stand? (h or s) ").lower()
            if action == 'h':
                self.player.hand.add_card(self.deck.deal_card())
                print(self.player)
            else:
                break

        # Dealer's turn
        if self.player.hand.calculate_value() <= 21:
            while self.dealer.calculate_value() < 17:
                self.dealer.add_card(self.deck.deal_card())
            print(f"Dealer's hand: {self.dealer} (Value: {self.dealer.calculate_value()})")

        # Check the winner
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.calculate_value()
        if player_value > 21:
            print("You lose! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer loses! You win.")
            self.player.win_bet(bet)
        elif player_value > dealer_value:
            print("You win!")
            self.player.win_bet(bet)
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a tie!")
            self.player.money += bet

        print(f"You now have ${self.player.money}.")

    def play(self):
        end_msg="""
        -------------------------------
        Thanks for playing My Game!, 
        Don't Play it Again, It is not Halal:(
        -------------------------------
        """
        while self.player.money > 0:
            clear_screen()
            self.start_round()
            if input("Do you want to play again? (y/n) ").lower() != 'y':
                break
        print(end_msg)

# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()