# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Computer")

# The game starts here.

label start:

#spaceship structure point 
$sp=10
$spMax=10

# display the story the first at begining if =1 and ask player name
$firstLoop=1

$travel=0
$planeteName= "Dokiss"

$planeteType=0
$maxPlaneteType=2
image bgPlanete = "[planeteType].png"

#17 phoneme to generate planete name
$phoneme= ['zu','zo','dor','bi','ko','zan','mi','mo','do','ri','po','pi','ka','chu','ar','di','ta','nia']
$phonemeMax=17

while sp > 0:
    #scene bgPlanete
    scene mars2

    #yalign min 0.45 max 1
    #
    #layeredimage paysage:
    #    always "mars2"
    #    group elem auto:
    #        pos (renpy.random.randint(0,640), renpy.random.randint(0,360))
    #        attribute mountain default
    
    #scene paysage

    $varX=renpy.random.randint(0,128)*10
    $varY=renpy.random.randint(28,72)*10

    #$i=renpy.random.randint(0,10)
    $i=10
    while i > 0:
        show mountain:
            xpos renpy.random.randint(0,128)*10
            ypos renpy.random.randint(28,72)*10
            xsize renpy.random.randint(0,100)
            ysize renpy.random.randint(0,100)
        $i -= 1


    #show cockpit
    if firstLoop==1:
        $firstLoop = 0
        c "Congratulation for participating in the Dokiss Space Explorer's programm."
        c "I'm glad to welcome you on board spaceship FX3000"
        python:
            name = renpy.input("Please enter your name")
            name = name.strip() or "Cloud"          

        c "Captain [name], please to meet you. You can Jump exploring space as soon as you're ready to go."

    label phase1:
    menu:
            "Jump":
                jump nextSector
            "Captain's log":
                "Sector : [planeteName] - Structure : [sp]/[spMax] - Jump : [travel]"
                jump phase1

    label nextSector:
    $travel += 1

    $nbPhoneme = renpy.random.randint(2, 4)
    $planeteName = ''
    while nbPhoneme >0:
        $nbPhoneme -=1
        $planeteName += phoneme[renpy.random.randint(0, phonemeMax)]
    $planeteName = planeteName.capitalize()

    $planeteType = renpy.random.randint(0,maxPlaneteType)
    image bgPlanete = "[planeteType].png"

#endwhile

# This ends the game.

return
