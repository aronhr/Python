# coding=UTF-8              ATH: Nota Ã¾essa lÃ­nu ef komment eiga aÃ° vera Ã¡ Ã­slensku!!!
import random
# -----------------------------------------------CLASSES-----------------------------------------------------
#                      NotaÃ°ir eru tveir klasa Ã­ Ã¾essum leik.  Dice og DoceThrower
# -----------------------------------------------------------------------------------------------------------

# lÃ­till klasi em tÃ¡knar einn stakan tening.
# falliÃ° throw() kastar Ã¾essum tening sÃ© Ã¾ess Ã³skaÃ°
class Dice:
    def __init__(self):
        self.number = 0

    def throw(self):
        self.number = random.randint(1,6)
        return self.number

# Ãžessi klasi sÃ©r um aÃ° kasta Ã¶llum teningunum og endurkasta(rethrow) hluta Ã¾eirra(eÃ°a Ã¶llum)
# SmiÃ°ur klasan hefur default gildiÃ° 5 fyrir fjÃ¶lda Ã¾eirra teninga sem nota Ã¡.
# ÃžaÃ° Ã¾Ã½Ã°ir aÃ° ef Ã¦tlunin er aÃ° nota 5 teninga Ã¾Ã¡ Ã¾arf ekki aÃ° senda fjÃ¶lda Ã¾eirra sem fÃ¦ribreyti
class DiceThrower:
    def __init__(self, how_many=5):
        self.number_of_dice = how_many  # hve marga teninga er veriÃ° aÃ° nota
        self.dice = Dice()  # einn tengingur bÃºinn til
        # listi af teningum sem nota Ã¡ frumstilltur Ã¡ -1
        self.dice_list = [-1 for i in range(self.number_of_dice)]


    # throw() falliÃ° Ã­ Ã¾essum klasa kastar Ã–LLUM teningum sem Ã¡ aÃ° nota
    # Ã¾aÃ° er gert Ã­ lÃºpp sem kallar Ã¡ throw() falliÃ° Ã­ klasanum Dice()
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

    # Ã¾etta fall() er notaÃ° til aÃ° kasta aftur Ã¾eim teningum sem spilarinn Ã³skar.
    # falliÃ° Ã¾arf aÃ° fÃ¡ index af Ã¾eim teningum sem kasta Ã¡ aftur(rethrow_list)
    # til dÃ¦mis ef spilarinn vill kasta aftur teningum 1 og 3 Ã¾Ã¡ setur hann
    # 0 og 2 Ã­ rethrow listann og sendir inn sem fÃ¦rubreytu.
    # sjÃ¡ dÃ¦mi um Ã¾etta Ã­ lÃ­num 87 - 91 hÃ©r aÃ° neÃ°an
    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()

# ----------------------------------------------FUNCTIONS----------------------------------------------------
#   Virkni forritsins er skipt upp Ã­ fjÃ¶gur fÃ¶ll sem, Ã¡samt leikjalÃºppunni ÃºtfÃ¦ra leikinn
#   ÃžaÃ° eru aÃ° sjÃ¡lfsÃ¶gÃ°u til Ã³tal leiÃ°ir aÃ° Ã¾essu marki en Ã¾essi er sÃ¦milega skÃ½r :-)
# -----------------------------------------------------------------------------------------------------------

# Ãžetta fall "teiknar" aÃ°alvalmynd leiksins og skilar niÃ°urstÃ¶Ã°u sem true/false
def main_menu():
    print '------------------------------------------------'
    print '1: New game'
    print '2: Quit'
    print '------------------------------------------------'

    user_input = int(raw_input('Enter your choice(1/2)please: '))

    if user_input == 1:
        return True # spilarinn vill spila leik
    else:
        return False


# HÃ©rna er teningunum kastaÃ°.
# FalliÃ° tekur tilvik af DiceThrower sem fÃ¦ri breytu og nÃ½tir til aÃ° klasta og endurkasta(rethrow)
# HÃ¦tt er Ã­ fallinu ef notandinn Ã¾arf ekki aÃ° kasta meira eÃ°a aÃ° fjÃ¶ldi kasta er kominn Ã­ 3
def dice_menu(dice_thrower):
    still_throwing = True   # spilarin er ennÃ¾Ã¡ aÃ° kasta teningunum
    number_of_throws = 0    # Ãžegar falliÃ° keyrir Ã­ fyrsta sinn Ã¾Ã¡ hefur spilarinn ekki kastaÃ° teningum

    while still_throwing:
        user_dice = dice_thrower.throw()    # HÃ©r er teningunum svo kastaÃ°
        number_of_throws += 1               # Ekki mÃ¡ kasta oftar en 3svar og Ã¾vÃ­ Ã¾arf aÃ° fylgjast meÃ° fjÃ¶lda kasta
        rethrowing_allowed = True           # Spilarinn mÃ¡ bara kasta 2svar og Ã¾aÃ° Ã¾arf aÃ° stoppa hann eftir Ã¾aÃ°.

        print '------------------------------------------------'
        print user_dice     # Prentar teningana Ãºt.
        print '------------------------------------------------'

        while rethrowing_allowed:
            # ÃžaÃ° Ã¾arf aÃ° spyrja spilarann hvort hann vilji endurkasta einhverjum teningum
            # SÃº staÃ°a getur komiÃ° upp aÃ° notandinn Ã¾urfi Ã¾ess ekki(t.d. yatzy Ã­ fyrsta kasti)
            rethrow = raw_input('Do you want to Rethrow? Y/N: ')
            if rethrow == 'Y':
                # indexinn Ã¡ Ã¾eim teningum sem kasta skal er fengiÃ° frÃ¡ spilaranum sem text
                # testa strengnum er svo breytt Ã­ lista af indexum
                s = raw_input("Enter the dices you want to rethrow(0 - 4) space between please: ")
                dice = s.split()
                rethrow_dice = [eval(x) for x in dice]

                # hÃ©rna er rethrow() falliÃ° Ã­ DiceThrower klasanum loks notaÃ°
                user_dice = dice_thrower.rethrow(rethrow_dice)
                number_of_throws += 1

                print '------------------------------------------------'
                print user_dice     # prentar teningana Ãºt aftur
                print '------------------------------------------------'
            else:
                rethrowing_allowed = False  # Keyrt ef notandinn Ã¾arf ekki aÃ° kasta miera

            if number_of_throws == 3:   #  Ef spilarinn er bÃºinn aÃ° kasta 3svar Ã¾Ã¡ er hann stoppaÃ°ur
                rethrowing_allowed = False

        still_throwing = False  # spilarinn er hÃ¦ttur aÃ° kasta Ã­ Ã¾etta skiptiÃ°

    # LokastÃ¶Ã°unni Ã¡ teningunum 5 er skilaÃ° Ãºt Ãºr fallinu
    return user_dice


# Ãžetta fall prentar Ãºt valmynd fyrir spilarann svo aÃ° hann geti
# "skrifaÃ°" niÃ°urstÃ¶Ã°ur sÃ­nar Ã¡ blaÃ°iÃ°(sheet)
# HÃ©rna vantar aÃ° sannprÃ³fa niÃ°urstÃ¶Ã°urnar og leyfa aÃ°eins rÃ©tt gildi Ã¡ rÃ©ttan
# staÃ°.  T.d: spilarinn hefur reynt aÃ° kasta og fÃ¡ stÃ³ru rÃ¶Ã°. ÃžaÃ° hefur ekki tekist og
# hann verÃ°ur nÃº aÃ° setja 0 stig Ã¡ blaÃ°iÃ°.
# Ã Ã¾essu demÃ³i getur spilarinn sett summuna hvar sem er :-(
def sheet_menu(dice,yatzy_sheet):
    print_sheet(yatzy_sheet)
    user_input = int(raw_input('Enter your choice(0 - 4)please: '))
    yatzy_sheet[user_input] = sum(dice)
    print_sheet(yatzy_sheet)


# Ãžetta fall prentar Ãºt yatzy-blaÃ°iÃ° og er notaÃ° af fallinu sheet_menu(). SjÃ¡ t.d. lÃ­nu 123 og 126
def print_sheet(yatzy_sheet):
    print '------------------------------------------------'
    print '0: Small Row', yatzy_sheet[0]
    print '1: Big Row',  yatzy_sheet[1]
    print '2: Full House', yatzy_sheet[2]
    print '3: Chance',  yatzy_sheet[3]
    print '4: Yatzy',  yatzy_sheet[4]
    print '------------------------------------------------'

# Leikurinn samanstendur af 5 tenginum
dt = DiceThrower()
# og blaÃ°i(sheet) sem fyllt er Ãºt(hÃ©rna er Ã¾aÃ° frumstillt meÃ° -1)
sheet = [-1,-1,-1,-1,-1]

# Ã upphafi er spurt hvort spila skuli leik eÃ°a hÃ¦tta viÃ°.
game_is_on = main_menu()

# LeikjalÃºppan fer Ã­ gang.  HÃ©r efit spilast leikurinn algerlega innan
# hennar.
while game_is_on:
    # Ãžessi smÃ¦kkaÃ°a ÃºtgÃ¡fa af Yatzy hefur 5 hluta:
    # "litlu rÃ¶Ã°", "storu rÃ¶Ã°" "fullt hÃºs","Ã¡hÃ¦ttu" og "yatzy"
    # ÃžaÃ° Ã¾arf aÃ° kasta teningunum fyrir hvert Ã¾essara hluta.
    # Muna samt aÃ° venjulegt yatzy hefur fleiri mÃ¶guleika
    # SjÃ¡ dÃ¦mi: http://www.appgamenews.com/mobile_games/mobilegames_dice/Yatzy_HD_33_1467_1.html
    # ÃžaÃ° er vitaÃ° fyrirfram hve oft Ã¾arf aÃ° kasta svo aÃ° hÃ©r er notuÃ° for-lÃºppa.
    for i in range(0,5):
        # Kallar Ã¡ falliÃ° dice_menu() sem sÃ©r um aÃ° kasta teningunum og birta niÃ°urstÃ¶Ã°ur
        # Ã¡samt Ã¾vÃ­ aÃ° bjÃ³Ã°a spilaranum uppÃ¡ aÃ° kasta aftur(alls Ã¾risvar)
        # FalliÃ° skilar svo lokastÃ¶Ã°unni Ã¡ teningunum fimm sem sett er Ã­ breytuna dice.
        dice = dice_menu(dt)
        # sheet_menu() er svo notaÃ° til aÃ° gefa spilaranum val um hvar hann setur niÃ°urstÃ¶Ã°urnar
        sheet_menu(dice,sheet)

    # SamanlÃ¶gÃ° stig eru loksins prentur Ãºt
    print 'Final Score',sum(sheet)
    # Spilarinn er aÃ° lokum spurÃ°ur hvort hann vilji spila nÃ½jan leik eÃ°a hÃ¦tta
    game_is_on = main_menu()

print 'The End!'
