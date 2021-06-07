# let us create a game : how about hangman
# this is the letter guessing game and it gives you max 6 wrong guesses.
# the game require us to choose a word by host and a clue / class the word belong to,
# the guesser will ask for specific letters if letters are present in word, if the guess is wrong, 
# player proceed to journey of hanging

#https://www.youtube.com/watch?v=cGOeiQfjYPk
#https://www.wikihow.com/Play-Hangman
# let us keep the host our program / computer

# let us store a dictionary with key and respective requred words
import sys
from termcolor import cprint, colored
from time import *


keys=['fruit','sport','indoor_games','color','animal','bird','music','computer_brand','smartphone_brand']
values_fruit='Apples,Apricots,Avocados,Bananas,Boysenberries,Blueberries,BingCherry,Cherries,Cantaloupe, Crab apples,Clementine,Cucumbers,Damsonplum,DinosaurEggs, Dates,Dewberries,DragonFruit,Elderberry, Eggfruit, Evergreen Huckleberry, Entawak,Fig,Farkleberry, Finger Lime,Grapefruit,Grapes,Gooseberries,Guava,Honeydew melon,Hackberry,HoneycrispApples,Plum, Indonesian Lime, Imbe, Indian Fig,Jackfruit, Java Apple, Jambolan,Kiwi, Kaffir Lime, Kumquat,Lime,Lychee,Loquat,Mango, MandarinOrange,Mulberry,Melon,Nectarine, NavelOrange,NashiPear,Olive,Oranges,Ogeechee Limes,Oval Kumquat,Papaya, Persimmon, Paw Paw, Prickly Pear,Peach,Pomegranate, Pineapple, Passion Fruit,Quince, QueenAnneCherry, Quararibea cordata,Rambutan,Raspberries,RoseHips,StarFruit,Strawberries,SugarBabyWatermelon,Tomato,Tangerine,Tamarind,TartCherries,Ugli Fruit,Uniq Fruit,Ugni,Vanilla Bean,Velvet Pink Banana, Voavanga,Watermelon,Wolfberry,WhiteMulberry,Xigua,Ximenia caffra fruit,XangoMangosteenFruitJuice,Yellowassion Fruit,YunnanHackberry,Yangmei,ZigZagVinefruit,Zinfandel  apes,Zucchini'.replace(' ','').split(',')
values_sports='soccer ,asketball,tennis,baseball,golf,running,volleyball,badminton,swimming,boxing,table tennis,skiing,ice skating,roller skating,cricket,rugby,pool,darts,football,bowling,ice hockey,surfing,karate,horse racing,snowboarding,skateboard,ng cycling,archery,fishing,gymnastics,figureskating,rock climbing,sumo wrestling,taekwondo,fencing water skiing,jet skiing,weight lifting,scuba diving,judo,wind surfing,kickboxing,sky diving,hang gliding,bungee jumping'.replace(' ','').split(',')
values_indoor_games='chess,pocker,cards,scribble,ludo'.split(',')
values_color='red,blue,green,yellow,orange,violet,purple,indigo'.split(',')
values_animal='dog,cat,horse,lion,fish,bear,tiger,deer,rabbit,elephant,wolf,cattle,frog,giraffe,insect,sheep,kangaroo,leaopard,snake,hippopota,monkey,turtle,whale,squirrel,dolphin,zebra,goat,owls,chicken,camels,rhinoceros,bats,sharks,donkey,fox,parrots,spider,eagle,human,gorilla,wildboar,otter,ferret,kitten,badger,raccoon'.split(',')
values_bird='parrot,owl,columbidae,woodpeacker,swan,hummingbird,herons,chicken,finche,stork,falcon,songbird,cormorant,cockatoo,plover,sparrow,crane,swallow,cuckoo,budgerigar,thrush,penguin,sandpiper,wren,pelican,nightingale,lark,mallard,hornbill,loon,sternidae,blackbird,kingfisher,lovebird,lbis,tit,crow,oriole,cockatiel,osprey,eagle,coot,europeanrobin,toucans,bulbul,shrike,americanrobin'.split(',')
values_music='rock,jazz,classical,pop,blues,hiphop,folk,singing,countrymusic,heavymetal,soul,punkrock,reggae,instrumental,orchestra,electronic,dance,house,funk,ambient,disco,techno,musicofafrica,gospel,trance,world,hymn,progressiverock,baroque,opera,soundrack,jazzfusion,indierock,poprock,hardrock,dubstep,swingmusic,ska,industrial,hardcorepunk,bigband,religious'.split(',')
values_computer_brand='apple,dell,lenovo,asus,compacq,hp,hcl,honour,mi,lg,msi,microsoft,razer,sony,toshiba,vaio,lava,micromax,acer'.split(',')
values_smartphone_brand='apple,samsung,mi,xiomi,lenovo,honour,mircromax,sony,lg,panasonic,nokia,microsoft,lava,iball,huawei,google,oppo,vivo,motorola,blackberry'.split(',')


def print_list_values(a_list):
    for j in range(len(a_list)):
        if j<len(a_list)-1:
            cprint(a_list[j],'green',end=' ')
        else:
            cprint(a_list[j],'green')
    
    
def update_the_guess(letter,string,updated_list):
    string=string.lower()
    letter=letter.lower()
    for j in range(len(string)):
        if string[j]==letter:
            updated_list[j]=string[j]
    return updated_list
            
def shape(number):
    if number==0:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint(('\t'*6+' ||\n')*9,'white')
    elif number==1:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint('\t'*6+' ||                   O','green')
        cprint(('\t'*6+' ||\n')*8,'white')
    elif number==2:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+ ' ||                  |\n')*3,'white')
        cprint('\t'*6+' ||                   O','green')
        cprint('\t'*6+' ||                  /','green')
        cprint(('\t'*6+' ||\n')*7,'white')
    elif number==3:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint('\t'*6+' ||                   O','yellow')
        cprint('\t'*6+' ||                  / \\','yellow')
        cprint(('\t'*6+' ||\n')*6,'white')
    elif number==4:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint('\t'*6+' ||                   O','yellow')
        cprint('\t'*6+' ||                  /|\\','yellow')
        cprint(('\t'*6+' || \n')*5,'white')
    elif number==5:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint('\t'*6+' ||                   O','red')
        cprint('\t'*6+' ||                  /|\\','red') 
        cprint('\t'*6+' ||                  /  ','red') 
        cprint(('\t'*6+' |\n')*4,'white')
    elif number==6:
        cprint('\t'*6+' ____________________','white')
        cprint(('\t'*6+' ||                   |\n')*3,'white')
        cprint('\t'*6+' ||                   O','magenta')
        cprint('\t'*6+' ||                  /|\\','magenta') 
        cprint('\t'*6+' ||                  / \\ ','magenta') 
        cprint(('\t'*6+' ||\n')*3,'white')
        
        
def organize_hangman(random_word,word_class):
    for i in range(len(random_word)):
        cprint('_ ','cyan',end='')                                                   # printing the dashes            
    absent_letters=''
    failed_count=0                            # it counts the wrong attempts
    updated_guess=list('_'*len(random_word))
    while(True):
        cprint('The word belongs to class of :'+word_class+'','blue')                                        
        guess=input('enter a letter or word to guess: ')
        print('\x1bc')
        if (guess in random_word and len(guess)==1) or guess==random_word:           # if true it executes the below set of instructions  
            if len(guess)==1:
                updated_guess=update_the_guess(guess,random_word,updated_guess)      #found_position=random_word.find(guess) will only find first matched location
                print_list_values(updated_guess)                                     # let us print the updated guess_list
                shape(failed_count)
                cprint('\n Absent words/letters:\t'+absent_letters.upper()+'\n','red')
                if updated_guess==list(random_word):
                    cprint('\n You won!!!!!! correct word is '+str(random_word),'green')
                    break
            elif guess==random_word:
                cprint('You won, the word was :'+random_word+' ','green')
                break
                
        else:
            print('\x1bc')
            print_list_values(updated_guess)
            failed_count+=1
            shape(failed_count)
            absent_letters+=guess+','
            cprint('\n Absent words/letters:\t'+absent_letters.upper()+'\n','red')
            if failed_count==6:
                cprint('You lost: word was-  '+random_word,'magenta')
                break
                
                
    
# let us create our master key:    
master_key={'fruit':values_fruit,'sport':values_sports,'indoor_games':values_indoor_games,'color':values_color,'animal':values_animal,'bird':values_bird,'music':values_music,'computer_brand':values_computer_brand,'smartphone_brand':values_smartphone_brand}
import random as rd



# main program'


def player_mode_input():
    player_mode_user=input('\n\t Enter player mode:\n\t\t For 1 Player : Enter 1 \n\t\t For 2 players: Enter 2 \n\t\t Any other key to exit: \n\n\t\t\t Your Choice:    ')
    return player_mode_user


def status(play_mode_value):
    if play_mode_value=='1':
        player='Single'
    elif play_mode_value=='2':
        player='Double'

    cprint('\n\t\t Player Status:   '+player+'\t'*16,'white','on_magenta')
    cprint('\t 1) Enter 0 to switch '+'\t'*16,'white','on_magenta')
    cprint('\t 2) Enter q to quit   '+'\t'*16,'white','on_magenta')
    cprint('\t 3) Press enter to continue '+'\t'*16,'white','on_magenta')
    entry_user=input(' \t\t\t Your choice : ')
    return entry_user

def single_play():
    print('\x1bc')
    random_key_position=rd.randint(0,len(keys)-1)
    random_class=keys[random_key_position]             # choosing random key/class of word
 
    word_list=master_key[random_class]                 # selecting the list of perticular class of word
    random_value_position=rd.randint(0,len(word_list)-1)        # choosing random no for that list            
    chosen_word=word_list[random_value_position]                    # this is the choosen word that player has to guess         
    organize_hangman(chosen_word,random_class)                   # calling our function to organise game:
             

def double_play():
    random_class=input('Host should enter the category of word it belongs to :')
    chosen_word=input('Please enter the word to ask ')
    print('\x1bc')
    organize_hangman(chosen_word,random_class)


# main program: starts form here: best is to write expected functions below and then create such functions
def run_deamon():
    player_mode=player_mode_input()      # it will take input choices from user
    if player_mode=='1' or player_mode=='2':
        while(True):
            entry=status(player_mode)               # it let's user to look at current player mode and make changes if required
            print('\x1bc')
        
            if entry=='':
                if player_mode=='1':
                    single_play()
                elif player_mode=='2':
                    double_play()
        
            elif entry=='0':
                if player_mode=='1':
                    double_play()
                    player_mode='2'

                elif player_mode=='2':
                    single_play()
                    player_mode='1'
    
            elif entry=='q':
                print('\x1bc')
                cprint(' Thanks for playing hangman '+'\t'*10,'white','on_magenta')
                break                               
        
            else:
                cprint(' \t\t you have entered wrong key ','white','on_magenta')
                continue                                                       # recurssion of deamon functions
    
             
    else:
        cprint(' \t\t Thanks for playing/trying hangman  '+'\t'*10,'white','on_magenta')
        

# let us run our deamon now:
cprint('\n\n\t\t Warning: Hangman will start in clean terminal   \n','cyan')
run_deamon()                 # this is our main command.
