''' 
    Welcome to Text Adventure RPG! Go through an original text adventure as a character of your choice and try 
    to get to the ending.     
    Credits: Online ASCII Images
'''

import random as ra

# All ASCII art
boy = r'''

        ////^\\\\
        | ^   ^ |
       @ (o) (o) @
        |   <   |
        |  ___  |
         \_____/
      ____|  |____
     /    \__/    \
    /              \
   /\_/|        |\_/\
  / /  |        |  \ \
 ( <   |        |   > )
  \ \  |        |  / /
   \ \ |________| / /
   
   '''
girl = r'''
        w*W*W*W*w
         \"."."/
          //`\\
         (/a a\)
         (\_-_/) 
        .-~'='~-.
       /`~`"Y"`~`\
      / /(_ * _)\ \
     / /  )   (  \ \
     \ \_/\\_//\_/ / 
      \/_) '*' (_\/
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        w*W*W*W*w
        
        '''
trophy = r'''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
              
              '''
tombstone = r'''

      _.---,._,'
       /' _.--.<
         /'     `'
       /' _.---._____
       \.'   ___, .-'`
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
        |                 |           |
        |                 |           |
         \              \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   '''
troll = r'''
     /\
    /  \                               
   / || \    ,/  _____  \.             
   \_||_/    ||_/     \_||             
     ||       \_| . . |_/              
     ||         |  L  |                
    ,||         |`==='|                
    |>|      ___`>  -<'___             
    |>|\    /             \            
    \>| \  /  ,    .    .  |           
     ||  \/  /| .  |  . |  |           
     ||\  ` / | ___|___ |  |          
     || `--'  | _______ |  | 
     ||       | - --- - | -|
     ||       | -- - -- |  | 
     ||       |         |  |
     
     '''
castle = r'''
                        
         |~        www        
        /.\       /#^^\_     /\
       /#  \     /#%    \   /# \
      /#%   \   /#%______\ /#%__\
     /#%     \   |= I I ||  |- |
     ~~|~~~|~~   |_=_-__|'  |[]|
       |[] |_______\__|/_ _ |= |`.
^V^    |-  /= __   __    /-\|= | :;
       |= /- /\/  /\/   /=- \.-' :;
       | /_.=========._/_.-._\  .:'
       |= |-.'.- .'.- |  /|\ |.:'
       \  |=|:|= |:| =| |~|~||'|
        |~|-|:| -|:|  |-|~|~||=|      ^V^
        |=|=|:|- |:|- | |~|~|| |
        | |-_~__=_~__=|_^^^^^|/___
        |-(=-=-=-=-=-(|=====/=_-=/\
        | |=_-= _=- _=| -_=/=_-_/__\ 
        | |- _ =_-  _-|=_- |]#| I II
        |=|_/ \_-_= - |- = |]#| I II
        | /  _/ \. -_=| =__|]!!!I_II!!
       _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
     _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
    / .-'  __/_   `.   _/.' .-' `-. ; ====;\
   /.   `./    \ `. \ / -  /  .-'.' ====='  >
  /  \  /  .-' `--.  / .' /  `-.' ======.' /
  
  '''
sphinx = r'''
        _____,    _..-=-=-=-=-====--,
     _.'a   /  .-',___,..=--=--==-'`
    ( _     \ /  //___/-=---=----'
     ` `\    /  //---/--==----=-'
  ,-.    | / \_//-_.'==-==---='
 (.-.`\  | |'../-'=-=-=-=--'
  (' `\`\| //_|-\.`;-~````~,        _
       \ | \_,_,_\.'        \     .'_`\
        `\            ,    , \    || `\\
          \    /   _.--\    \ '._.'/  / |
          /  /`---'   \ \   |`'---'   \/
         / /'          \ ;-. \
      __/ /           __) \ ) `|
    ((='--;)         (,___/(,_/
    
    '''
tree = r'''


           \/ |    |/
        \/ / \||/  /_/___/_
         \/   |/ \/
    _\__\_\   |  /_____/_
           \  | /          /
  __ _-----`  |{,-----------~
            \ }{
             }{{
             }}{
             {{}
       , -=-~{ .-^- _
       
       '''
kronos = r'''
       _   
      /*\
     (o.o)
      |=|
     __|__
   //.=|=.\\
  // .=|=. \\
  \\ .=|=. //
   \\(_=_)//
    (:| |:)
     || ||
     () ()
     || ||
     || ||
    ==' '==
    
    '''

# Variables
nameM = ["Sir Chancelot" , "Sir Theodore", "Sir Raj"]
nameF = ["Lady Lisa", "Lady Celestial", "Lady Mary"]
ans = ""
name = "" 
health = 100
skip = False

# Functions
def intro():
  global name
  print("\nWelcome traveler, to the magical world of Cornucopia!\n")

  ans = input("Are you a boy or girl? ")
  if "G" in ans.upper():
    print(girl)
    name = nameF[ra.randint(0,2)]
    print("\nWelcome, " + name + " !") 
  elif "B" in ans.upper():
    print(boy)
    name = nameM[ra.randint(0,2)]
    print("\nWelcome, " + name + " !") 
  else:
    print(boy)   
    name = nameM[ra.randint(0,2)]
    print("\nWelcome, " + name + " !") 
def loseHealth(x):
  global health
  health -= x
def gainHealth(x):
  global health
  health += x
def checkDeath(x):
  global health
  name = x
  if health <= 0:
    print("\nOh no. You have lost all your health. RIP " + name + ".")
    print(tombstone)
    print("Press the play button at the top to restart.")
    exit()
  else:
    print("Health: " + str(health) +"\n")
def step(obj,text,ans1,ans2,rep1,rep2,let1,sk):
  global ans
  global name
  global skip
  print(obj)
  ans = input(text + " ")
  if let1 in ans.upper():
    print(ans1)
    if(rep1 < 0):
      loseHealth(abs(rep1))
    else:
      gainHealth(rep1)
    if sk == 1:
      skip = True
  else:
    print(ans2)
    if(rep2 < 0):
      loseHealth(abs(rep2))
    else:
      gainHealth(rep2)
  checkDeath(name)

''' Main game '''

intro()
print("\nThe king of Cornucopia has been kidnapped by the evil Kronos, and only you can stop him!",end=" ")
print("Reach Kronos's castle first.\n")
checkDeath(name)



step(troll,"You come across a troll. Do you attack or run?","Oof! The troll attacked you back and you lost 20 health!\n","You managed to escape!\n",-20,0,"A",0)

step("","You arrive at cross-roads. Do you take path A or path B?","You took a shortcut, good job!\n","You have taken the long way to the castle.\n",0,0,"A",1)

if not skip:
  step("","You meet a gremlin. Do you attack or run?","You kill the gremlin and gain 10 health!\n","Oh no. The gremlin damages you severely.\n",10,-30,"A",0)
skip = False 

step(sphinx,"You meet a bridge-sphinx. He asks you a question: \'What has a head, a tail, but does not have a body?\'","You are correct! The sphinx lets you pass.\n","You are wrong. You lose 25 health and the sphinx asks you another question.\n",0,-25,"COIN",1)

if not skip:
  step("","\'Which is larger: the Earth or Mars?\'","You are correct! The sphinx lets you pass.\n","Oh no. You manage to run past the sphinx, but he damages you.\n",0,-25,"E",0)
skip = False 

step(tree,"You are almost at the castle! A tree stands in your path. Do you cut it down?","Oh no! The tree was toxic. You lost 10 health.\n","The tree gives you health and lets you pass.\n",-10,+20,"Y",0)

step(castle,"You finally reach the castle and see Kronos.Do you attack him or hide?","Kronos blocks your arrow and fires back! You lose 10 health.\n","You successfully hide from Kronos.\n",-10,0,"A",0)

step(kronos,"You free the king. Kronos sees you. Do you attack or run?","You manage to defeat Kronos!\n","Oh no! Kronos damages you severely but you manage to escape the castle.\n",0,-30,"A",0)



print("Congrats " + name + ", you managed to defeat Kronos and free the king!")
print(trophy)







