#!/usr/bin/env python
 # -*- coding: utf-8 -*- #

import collections
from random import shuffle


def ascii_card(rank, suit):
	suit_dict = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
	suit = suit_dict[suit]
	card = ["┌─────────┐", f"│{rank}{' ' if rank != '10' else ''}       │", "│         │",
			   "│         │", f"│    {suit}    │", "│         │",
			   "│         │", f"│       {' ' if rank != '10' else ''}{rank}│", "└─────────┘"]
	return card


def print_ascii_cards(cards):
	lines = ["" for i in range(9)]
	for card in cards:
		for i, line in enumerate(card):
			lines[i] += (line)
	visual_display = "\n".join(lines)
	return visual_display


Card = collections.namedtuple("Card", ["rank", "suit", "power"])

class Deck:
	ranks = [str(rank) for rank in range(2, 11)] + ["J", "Q", "K", "A"]
	suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
	powers = {rank: v for (v, rank) in enumerate(ranks)}

	def __init__(self, decks=1):
		self.cards = [Card(rank, suit, self.powers[rank]) for suit in self.suits for rank in self.ranks] * decks

	def __len__(self):
		return len(self.cards)

	def __getitem__(self, i):
		return self.cards[i]

	def draw_card(self, num=1):
		drawn_cards = [self.cards.pop(self.cards.index(card)) for card in self.cards[:num]]
		return drawn_cards

	def shuffle_deck(self):
		shuffle(self.cards)


class Player:
	def __init__(self, name, hand=[]):
		self.name = name
		self.hand = hand

	def __len__(self):
		return len(self.hand)

	def __repr__(self):
		return self.name

	def __add__(self, other):
		self.hand += [other]

	def use_card(self, card):
		return self.hand.pop(card)


deck = Deck()
deck.shuffle_deck()
players = [Player(f"Player{i + 1}", hand=deck.draw_card(6)) for i in range(4)]

for player in players:
	print(player)
	player_cards = [ascii_card(player.hand[i].rank, player.hand[i].suit) for i in range(len(player.hand))]
	print(print_ascii_cards(player_cards) + "\n")
