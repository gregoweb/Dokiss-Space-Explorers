# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Computer")
define audio.sndPrimal = "music/primal.mp3"
define audio.sndSpace = "music/space.mp3"

# The game starts here.

label start:
$cloning = False

#spaceship fuel
$fuel=10

$charismaSkill=0
$killingSkill=0
$miningSkill=0

# display the story the first at begining if =1 and ask player name
$firstLoop=True
$name = "Cloud"

$travel=0
$planeteName= "Dokiss"

$planeteType=0
$planeteSecurityLevel=20
$planeteRudenessLevel=3
$planeteMiningLevel=3
$planeteFuel=3
$maxPlaneteType=2
image bgLanding = "[planeteType].png"
image bgStars = "stars.png"
image bgPlanete = "p[planeteType].png"

#19 phoneme to generate planete name
$phoneme= ['zu','zo','dor','bi','ko','zan','mi','mo','mor','do','ri','po','pi','ka','chu','ar','di','ta','nia']
$phonemeMax=18
$nameCreature = ['picat','akesi','kala','jan','soweli','waso']
$nameCreatureMax = 5
$nameOre = ['crystals', 'gold', 'andesite', 'silver', 'carbohydrate crystals']
$oreMax= 4
$ore="crystals"

$alienAlive = False
$alienGirlAlive = False

while fuel > 0:
    play music sndSpace fadeout 1.0 fadein 1.0
    scene bgLanding
    
    if planeteType==1:
        show mountains-mars:
            xpos renpy.random.randint(-128,128)*10
            ## ypos min320 max370
            ypos renpy.random.randint(32,37)*10
            xsize 1280
            ysize 290
            ##xsize 2560
            ##ysize 580


    show cockpit
    if firstLoop:
        $firstLoop = False
        c "Congratulation for participating in the Dokiss Space Explorers programm."
        c "I'm glad to welcome you on board spaceship FX3000"
        python:
            name = renpy.input("Please enter your name")
            name = name.strip() or "Cloud"          

        c "Captain [name], please to meet you. You can Jump exploring space as soon as you're ready to go."

    label landed1:
    menu:
        "Take off":
            jump space1
        "Try to establish contact with [planeteName]'s people":
            jump contact
        "Captain's log":
            "Captain [name] - Sector : [planeteName] \n Fuel : [fuel] - Jump : [travel] \n - Skills - \n Mining : [miningSkill] - Combat : [killingSkill] - Charisme : [charismaSkill] "
            jump landed1

    label contact:
        play music sndPrimal fadeout 1.0 fadein 1.0
        hide cockpit
        

        $d10 = renpy.random.randint(0,10)
        $rndQuest = renpy.random.randint(0,1)
        if rndQuest == 0:#mining
            $rndAlien = renpy.random.randint(1,5)
            image imgAlien = "a[rndAlien].png"
            show imgAlien as alien
            if rndAlien>3:
                $alienGirlAlive = True
                play sound "audio/bondaG.wav"
            else:
                $alienAlive = True
                play sound "audio/bonda.wav"

            "Could you mine some [ore] for us, Captain [name] ? \n We will give you [planeteFuel] fuel, if you do so."
            menu:
                "Yes":
                    jump mining
                "No":
                    jump landed2
                "Give me your Fuel for free or it will cost your life":
                    jump killing1
                "Imagine how rewarding it would be for you to give me your fuel ":
                    jump charisma1

        elif rndQuest == 1:#creature
            $rndCreature = renpy.random.randint(0,8)
            
            if rndCreature==0:
                show a1 as alien
                play sound "audio/Grrr.wav"
            elif rndCreature==1:
                show a2 as alien
                play sound "audio/meow.wav"
            elif rndCreature==2:
                show picat as alien
                play sound "audio/meow.wav"
            elif rndCreature==3:
                show picat as alien
                play sound "audio/Shhh.wav"
            elif rndCreature==4:
                show picat as alien
                play sound "audio/Grrr.wav"
            elif rndCreature==5:
                show a4 as alien
                play sound "audio/meow.wav"
            elif rndCreature==6:
                show a5 as alien
                play sound "audio/meow.wav"
            elif rndCreature==7:
                show a3 as alien
                play sound "audio/hu.wav"
            elif rndCreature==7:
                show a3 as alien
                play sound "audio/Grrr.wav"
            
            $creature = nameCreature[renpy.random.randint(0, nameCreatureMax)]
            "A terrifying [creature] approach"
            menu:
                "I will add you to my hunting board ":
                    jump killing1
                "Oh the cute little [creature] look at her eyes":
                    jump charisma1
                   
    
    label mining:
        if d10 > planeteMiningLevel:
            "You successfully mined [ore] and receive [planeteFuel] fuel from [planeteName]'s people"
            $miningSkill +=1
            $fuel += planeteFuel
        else:
            "You failed at mining"
        jump landed2

    label killing1:
        if (d10+killingSkill) > planeteSecurityLevel:
            hide alien
            "You killed your opponents and won [planeteFuel] fuel"
            $killingSkill +=1
            $fuel += planeteFuel
            $alienGirlAlive = False
            $alienAlive = False
        else:
            $cloning = True
        jump landed2
        
    label charisma1:
        if (d10+charismaSkill) > planeteRudenessLevel:
            "You charmed your hosts and won [planeteFuel] fuel"
            $charismaSkill +=1
            $fuel += planeteFuel
        else:
            $cloning = True
        jump landed2

    label landed2:
    
    hide alien
    show cockpit
    if cloning:
        "You wake up and find that you lost 1 fuel"
        $cloning = False
        $fuel -=1
        if fuel <0:
            jump endgame

    if alienAlive:
        play sound "audio/owar.wav"
    
    if alienGirlAlive:
        play sound "audio/owarG.wav"

    menu:
        "Take off":
            jump space1
        "Captain's log":
            "Captain [name] - Sector : [planeteName] \n Fuel : [fuel] - Jump : [travel] \n - Skills - \n Mining : [miningSkill] - Combat : [killingSkill] - Charisme : [charismaSkill] "
            jump landed2



    label space1:
    play music sndSpace fadeout 1.0 fadein 1.0
    show bgStars behind cockpit:
        xpos renpy.random.randint(-128,0)*10

    show cockpit
    label space2:
    menu:
        "Go next sector":
            jump nextSector1
        "Captain's log":
            "Captain [name] - Sector : [planeteName] \n Fuel : [fuel] - Jump : [travel] \n - Skills - \n Mining : [miningSkill] - Combat : [killingSkill] - Charisme : [charismaSkill] "
            jump space2

    label nextSector1:
    $travel += 1
    $fuel -= 1
    if fuel <0:
        jump endgame

    $nbPhoneme = renpy.random.randint(2, 4)
    $planeteName = ''
    while nbPhoneme >0:
        $nbPhoneme -=1
        $planeteName += phoneme[renpy.random.randint(0, phonemeMax)]
    $planeteName = planeteName.capitalize()

    $ore = nameOre[renpy.random.randint(0, oreMax)]

    $planeteType = renpy.random.randint(0,maxPlaneteType)
    $maxLevel=10+travel
    $planeteSecurityLevel=renpy.random.randint(0,maxLevel)
    $planeteRudenessLevel=renpy.random.randint(0,maxLevel)
    $planeteMiningLevel=renpy.random.randint(0,maxLevel)
    $planeteFuel=renpy.random.randint(1,4)
    image bgLanding = "[planeteType].png"
    image bgPlanete = "p[planeteType].png"
    $alienAlive = False
    $alienGirlAlive = False

    if planeteType==0:
        show bgPlanete behind cockpit:
            rotate 0
            xcenter 640
            ycenter 360
    else:
        show bgPlanete behind cockpit:
            rotate renpy.random.randint(0,180)*10
            xcenter 640
            ycenter 360

    "Sector : [planeteName]"
    label nextSector2:
    menu:
        "Scan":
            "- [planeteName] - \n Rudeness : [planeteRudenessLevel] - Mining : [planeteMiningLevel] - Security : [planeteSecurityLevel]"
            jump nextSector2
        "Landing":
            jump landing
        "Go next sector":
            show bgStars behind cockpit:
                xpos renpy.random.randint(-128,0)*10
            jump nextSector1
        "Captain's log":
            "Captain [name] - Sector : [planeteName] \n Fuel : [fuel] - Jump : [travel] \n - Skills - \n Mining : [miningSkill] - Combat : [killingSkill] - Charisme : [charismaSkill] "            
            jump nextSector2
    label landing:
#endwhile

label endgame:
# This ends the game.
c "You run out of Fuel thanks for your participation in the Dokiss Space Explorers programm."
c "Well done Captain [name] \n  Last sector : [planeteName] - Total Jumps : [travel] \n - Skills - \n Mining : [miningSkill] - Combat : [killingSkill] - Charisme : [charismaSkill] "

return
