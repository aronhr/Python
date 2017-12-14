#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle

PlayerCurrency = 50000
keepgoing = "yes"

# A big while loop
while(keepgoing != "no"):
    CurrentBet = 0
    # Asks for bet
    CurrentBet = int(input("Hvað viltu leggja mikið undir? buy-in er 500, þú átt " + str(PlayerCurrency)))

    # If currentBet is more or same as 500 and payer is not over betting.
    if(CurrentBet >= 500 and CurrentBet <= PlayerCurrency):

        # Function deck
        # Creates array of deck and shuffles it
        def deck():
            deck = []
            for suit in ['H', 'S', 'D', 'C']:
                for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
                    deck.append(suit+rank)

            shuffle(deck)
            return deck

        # Counts points from hands
        def pointCount(myCards):
            myCount = 0
            aceCount = 0

            for i in myCards:
                if (i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T'):
                    myCount += 10
                elif(i[1] != 'A'):
                    myCount += int(i[1])
                else:
                    aceCount += 1
            if(aceCount == 1 and myCount >= 10):
                myCount += 11
            else:
                myCount += 1

            return myCount

        # Creates playing hands with players deck and dealers
        def createPlayingHands(mydeck):
            dealerHand = []
            playerHand = []
            dealerHand.append(mydeck.pop())
            dealerHand.append(mydeck.pop())
            playerHand.append(mydeck.pop())
            playerHand.append(mydeck.pop())

            while(pointCount(dealerHand) <= 16):
                dealerHand.append(mydeck.pop())

            # returns dealers hand and players hand
            return [dealerHand, playerHand]

        game = ""
        myDeck = deck()
        hands = createPlayingHands(myDeck)
        dealer = hands[0]
        player = hands[1]

        # while game is runing
        while(game != "exit"):

            # Counts cards
            dealerCount = pointCount(dealer)
            playerCount = pointCount(player)

            print("Dealer er með :")
            print(str(dealer) + "    (" + str(dealerCount) + ") Stig")

            print("Notandi þú ert með:")
            print(str(player) + "    (" + str(playerCount) + ") Stig")

            # If player has sum of 21 points (BlackJack)
            if(playerCount == 21):
                print("Blackjack! Notandi vinnur!")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break
            elif(playerCount > 21):
                print("Notandi tapar með " + str(playerCount) + "Stig")
                PlayerCurrency = PlayerCurrency - CurrentBet
                break
            # If dealer has sum more than 21 points (dealer looses)
            elif(dealerCount > 21):
                print("Dealer tapar með " + str(dealerCount) + "Stig")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break

            # Asks player if he wants to hit or stand
            game = input("Hvað viltu gera? Hit![H], Stand[S]")

            # if player hits
            if(game == 'H'):
                player.append(myDeck.pop())
            # if player has more points than dealer
            elif(playerCount > dealerCount):
                print("Notandi vinnur með "+ str(playerCount) + " Stig")
                print("Dealer hefur" + str(dealer) + " eða " + str(dealerCount) + "points")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break
            # if dealer has more points than player
            else:
                print("Dealer Vinnur")
                print("Dealer hefur" + str(dealer) + " eða " + str(dealerCount) + "points")
                PlayerCurrency = PlayerCurrency - CurrentBet
                break
        # Player has max money
        if(PlayerCurrency >= 150000):
            print("Þú hefur safnað " + str(PlayerCurrency) + " og bankinn er tómur, game over")
            keepgoing = "no"
            break
        # Player has no money
        elif(PlayerCurrency < 500):
            print("Þú átt undir 500 eftir og getur ekki keypt buy-in, game over")
            keepgoing = "no"
            break
        # Prints players money
        print(PlayerCurrency)
        keepgoing = input("Hætta eða halda áfram? [yes/no]")
    # if player try to bet more money than he owns
    elif(PlayerCurrency < CurrentBet):
        print("Þú átt ekki svona mikið inni.")
    # player has to bet more than 499
    else:
        print("Upphæð þarf að vera yfir 500")


input("input to exit")
