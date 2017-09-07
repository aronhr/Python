#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle

PlayerCurrency = 50000
keepgoing = "yes"
while(keepgoing != "no"):
    CurrentBet = 0

    CurrentBet = int(input("Hvað viltu leggja mikið undir? buy-in er 500, þú átt " + str(PlayerCurrency)))
    if(CurrentBet >= 500 and CurrentBet <= PlayerCurrency):
        def deck():
            deck = []
            for suit in ['H', 'S', 'D', 'C']:
                for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
                    deck.append(suit+rank)

            shuffle(deck)
            return deck


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



        def createPlayingHands(mydeck):
            dealerHand = []
            playerHand = []
            dealerHand.append(mydeck.pop())
            dealerHand.append(mydeck.pop())
            playerHand.append(mydeck.pop())
            playerHand.append(mydeck.pop())

            while(pointCount(dealerHand) <= 16):
                dealerHand.append(mydeck.pop())

            return [dealerHand, playerHand]

        game = ""
        myDeck = deck()
        hands = createPlayingHands(myDeck)
        dealer = hands[0]
        player = hands[1]

        while(game != "exit"):
            dealerCount = pointCount(dealer)
            playerCount = pointCount(player)

            print("Dealer er með :")
            print(str(dealer) + "    (" + str(dealerCount) + ") Stig")

            print("Notandi þú ert með:")
            print(str(player) + "    (" + str(playerCount) + ") Stig")

            if(playerCount == 21):
                print("Blackjack! Notandi vinnur!")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break
            elif(playerCount > 21):
                print("Notandi tapar með " + str(playerCount) + "Stig")
                PlayerCurrency = PlayerCurrency - CurrentBet
                break
            elif(dealerCount > 21):
                print("Dealer tapar með " + str(dealerCount) + "Stig")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break

            game = input("Hvað viltu gera? Hit me![H], Stand[S]")

            if(game == 'H'):
                player.append(myDeck.pop())
            elif(playerCount > dealerCount):
                print("Notandi vinnur með "+ str(playerCount) + " Stig")
                print("Dealer hefur" + str(dealer) + " eða " + str(dealerCount) + "points")
                PlayerCurrency = PlayerCurrency + CurrentBet
                break
            else:
                print("Dealer Vinnur")
                print("Dealer hefur" + str(dealer) + " eða " + str(dealerCount) + "points")
                PlayerCurrency = PlayerCurrency - CurrentBet
                break
        if(PlayerCurrency >= 150000):
            print("Þú hefur safnað " + str(PlayerCurrency) + " og bankinn er tómur, game over")
            keepgoing = "no"
            break
        elif(PlayerCurrency < 500):
            print("Þú átt undir 500 eftir og getur ekki keypt buy-in, game over")
            keepgoing = "no"
            break
        print(PlayerCurrency)
        keepgoing = input("Hætta eða halda áfram? [yes/no]")
    elif(PlayerCurrency < CurrentBet):
        print("Þú átt ekki svona mikið inni.")
    else:
        print("Upphæð þarf að vera yfir 500")


input("input to exit")
