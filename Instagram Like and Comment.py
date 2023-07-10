import pyautogui as py
import keyboard
import time
import random
import cv2
import os


#
#holding ctrl+alt and shift to stop the program
#


#limitations  #Begrenzungen
############################
HowManyLikes = 80 #how many picturesand comments
HowManyComments = 80 #how many picturesand comments

############################
float_random = random.uniform(4.3452,  7.4353) #time between every like and comment between a and b (11 to 22 seconds)

############################
commentPicture = ("good work", "do another", "i gotcha :D", "nice", "pretty cool", "you deserve more likes", "creative", "do more, that's good", "ain't lyin but thats good", "like your content", ":D", "Excellent", "Love these. Well done.", "So nice", "So beautiful", "Adorable", "Beautiful", "Amazing job!", "You're so talented", "Keep up the great work", "I'm impressed", "This made my day", "You have a gift", "You're a genius", "This is so inspiring", "Absolutely stunning", "You nailed it", "You've got skills", "This is so entertaining", "Brilliant piece of work", "Wow, just wow", "This is fantastic", "Very impressive", "You have outdone yourself", "This is so creative", "Absolutely loved it", "I'm speechless", "This deserves more views", "You're a true artist", "I can't stop watching this", "This is so well done", "This is top-notch", "I love your style", "This is so original", "You're amazing at what you do", "Incredible", "I'm blown away", "You should be proud", "This is so captivating", "This is a masterpiece", "You've got a fan in me", "You're so innovative", "I'm in awe", "This is so refreshing", "Great content", "Fantastic work", "Can't wait for more", "Well executed", "Super creative", "This is so interesting", "I love your work", "You have a unique vision", "You're an inspiration", "This is truly amazing", "You're a natural", "This is so enjoyable", "Pure talent", "This is exceptional", "This is so well-crafted", "You have a great eye", "This is wonderful", "Such a great concept", "This is a work of art", "I'm a fan", "I'm addicted to your content", "You're a visionary", "This is top-quality", "You never disappoint", "You're a true talent", "This is incredibly well done", "This is so engaging", "You've outdone yourself again", "This is so well thought out", "I can't get enough of your work", "I'm amazed", "You're a true professional", "This is absolutely delightful", "This is so well presented", "You're a gem", "This is a breath of fresh air", "Keep the content coming", "You're a treasure", "I'm in love with your work", "This is extraordinary", "I can't wait to see what's next", "You're a creative force", "This is so fun to watch", "You're a master at your craft", "This is so unique", "I'm obsessed with your content", "This is so mesmerizing")
commentVideo = ("Great video! I enjoyed watching it!", "I can't wait for your next video!", "This video made me smile!", "You're doing an amazing job with your videos!", "This video was so entertaining!", "This video was captivating!", "A fantastic video from start to finish!", "I'm a fan of your video content!", "I'm addicted to watching your videos!", "You never disappoint with your videos!", "You're a true talent in creating videos!", "This video was incredibly well done!", "I couldn't stop watching this video!", "This video is top-quality content!", "I love the style of your videos!", "You're amazing at creating video content!", "I'm in awe of your video-making skills!", "This video was fascinating and interesting!", "I love the work you put into your videos!", "You're an inspiration to aspiring video creators!", "This video is truly amazing and enjoyable!", "You have a natural talent for making videos!", "Your videos are always so engaging!", "You've outdone yourself with this video!", "I can't get enough of your video content!", "I'm amazed by the quality of this video!", "You're a true professional in video creation!", "This video is absolutely delightful to watch!", "This video is a breath of fresh air!", "Keep the amazing video content coming!", "I'm in love with your video work!", "This video is extraordinary!", "I can't wait to see what's next in your video series!", "You're a creative force in the video-making world!", "This video was so fun to watch!", "You're a master at creating videos!", "This video is unique and stands out!", "I'm obsessed with your video content!", "This video is mesmerizing and captivating!")
emojisSpam = (" 🅿️"," 🔥"," ✅", " 🍁","  💙", " 👍", "  🥺", " 🦘", " 📍", " 🌿", " 💜", " 💚", "  🙋‍♂️", " 🚀", " 🤠", " 🌍", " 👉", " 🖤", " 🔔", " 🥀", " ⤵️", " 🔖", " ♥️" )
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")


#Monitor 2556x 1440                                                              1080p BUT 150% SCALING
#Skalierung 150% #scaling VERY IMPORTANT
#Instagram über Opera linke Seite #instagram on left side in opera
#Beenden mit ctrl+alt+shift #stop with ctrl+alt+shift
















def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))

def betterWait(float_random):
    new_randomizer = random.uniform(1.000005,  1.243564)
    num_iterations = round(float_random)
    for i in range(num_iterations):
        time.sleep(new_randomizer)
        beenden()
    

anzahl_der_prozesse = 0
def beenden():
    if keyboard.is_pressed("ctrl+alt+shift"):
        print("Programm beendet")
        exit()

time.sleep(1)
def MausPosition(Champion):
    beenden()
    print("Das Bild: " + Champion + " wird gesucht")
    
    beenden()
    istVideoOderNicht = 0
    beenden()
    time.sleep(0.2)
    beenden()
    picture1 = py.screenshot() #region=(2046, 997, 920, 430) minimap location  #start while in game
    beenden()

    path = get_current_path()
    picture1.save(path+"\Jungle-Tracker-Picture.jpg")
    beenden()


    TestJungle = cv2.imread(path+"\BilderInstagram\m" + Champion + ".PNG", cv2.IMREAD_UNCHANGED)
    beenden()
    DesktopTest = cv2.imread(path+"\Jungle-Tracker-Picture.jpg", cv2.IMREAD_UNCHANGED)
    beenden()

    nesne = cv2.cvtColor(DesktopTest, cv2.COLOR_BGR2GRAY)
    beenden()
    nesne1 = cv2.cvtColor(TestJungle, cv2.COLOR_BGR2GRAY)
    beenden()

    result = cv2.matchTemplate(nesne1, nesne, cv2.TM_CCOEFF_NORMED)
    beenden()

    #result = pyautogui.locateAllOnScreen(TestJungle)


    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    beenden()
    beenden()

    beenden()
    print("Kommentar nochmal geschrieben")
    beenden()

    print(max_loc)
    beenden()
    x, y = max_loc
    beenden()
    if max_val < 0.85 and Champion == "like":
        x = "k"
        beenden()
        y = "k"
        beenden()
        print("hello you ass")
        beenden()
    elif Champion == "deaktiviert":
        if max_val > 0.92:    
            beenden()
            print("kommentar skippen")
            beenden()
            print("Das Bild: " + Champion + " wird beendet")
            return "yes"
        else:
            return "no"
        
    elif Champion == "video" or Champion == "video2" or Champion == "video3":
        beenden()
        if max_val > 0.85:
            beenden()
            IsVideo = 1
            beenden()
            print("Das Bild: " + Champion + " wird beendet")
            return x, y, IsVideo
        else:
            IsVideo = 0
            beenden()
            print("Das Bild: " + Champion + " wird beendet")
            return x, y, IsVideo



    elif Champion == "kommentar" and max_val > 0.90:
        beenden()
        x1, y1, istVideoOderNicht = MausPosition("video")
        x2, y2, istVideoOderNicht2 = MausPosition("video2")
        x3, y3, istVideoOderNicht3 = MausPosition("video3")

        istVideoOderNicht += istVideoOderNicht2
        istVideoOderNicht += istVideoOderNicht3
        print(str(istVideoOderNicht), str(istVideoOderNicht2), str(istVideoOderNicht3)+ "istVideoOderNicht Wert von allen 3")

        
        beenden()
        print("Kommentar geschrieben")
        beenden()
        print("Das Bild: " + Champion + " wird beendet")
        return x, y, istVideoOderNicht
    elif max_val < 0.90 and Champion == "kommentar":
        print("kein Button für Kommentar gefunden")
        x = "no"
        y = "no"
        istVideoOderNicht = "no"
        return "no"
   


    beenden()
    print("Das Bild: " + Champion + " wird beendet")
    return x, y, istVideoOderNicht


def kommentar():
    beenden()
    x, y, IsVideo = MausPosition("kommentar")
    beenden()
    print(str(x),  str(y)+ " koordination des Buttons Kommentar")
    py.moveTo(x, y)
    beenden()
    betterWait(float_random)
    beenden()
    py.click()
    beenden()
    py.moveTo(x+100, y+100)
    beenden()

    if IsVideo == 1:
        if random_accurance_alphabet == 1:
            count = 0
            anzahlBuchstaben = len(commentPicture[random_comment_Video])
            position = random.randint(0, anzahlBuchstaben-1)
            for i in range(len(commentVideo[random_comment_Video])):
                            if count == position:
                                py.typewrite(alphabet[random_alphabet])
                            
                            
                            py.typewrite(commentVideo[random_comment_Video][count])
                            count += 1
                            
        else:
            py.typewrite(commentVideo[random_comment_Video])



        if random_accurance_emoji == 1:
                        keyboard.write(emojisSpam[random_Emoji])
                        keyboard.press_and_release('enter')
                        time.sleep(float_random_more_capa)
        else:
            keyboard.press_and_release('enter')
            time.sleep(float_random_more_capa)



    elif IsVideo == 0:    
        if random_accurance_alphabet == 1:
            count = 0
            anzahlBuchstaben = len(commentPicture[random_comment_Picture])
            position = random.randint(0, anzahlBuchstaben-1)
            for i in range(len(commentPicture[random_comment_Picture])):
                            if count == position:
                                py.typewrite(alphabet[random_alphabet])
                            
                            
                            py.typewrite(commentPicture[random_comment_Picture][count])
                            count += 1
        else:
            py.typewrite(commentPicture[random_comment_Picture])



        if random_accurance_emoji == 1:
                        keyboard.write(emojisSpam[random_Emoji])
                        time.sleep(float_random_more_capa)
        else:
            keyboard.press_and_release('enter')
            time.sleep(float_random_more_capa)


    elif IsVideo == "no":
        pass



def liken():
    x, y, istVideoOderNicht = MausPosition("like")
    beenden()
    if x == "k":
        beenden()
        print("hiiiii")
        beenden()
        return x
    else:
        print("not hiiii")
        beenden()
        print(x, y)
        beenden()
        py.moveTo(x, y)
        beenden()
        betterWait(float_random)
        beenden()
        py.click()
        beenden()
        py.moveTo(x+100, y+100) 
        beenden()




float_random_more_capa = random.uniform(0.57335,  2.46773) #for better safety #don't do more than 2.5 seconds




#bild liken (144, 681) mit doppelklick
#weiter zum nächsten bild (1021, 697) mit einem klick
while HowManyLikes >= 1 or HowManyComments >= 1:
    

    

    random_accurance_emoji = random.randint(0, 1) #50% chance für ein emoji
    random_accurance_alphabet = random.randint(0, 1) #50% chance für ein alphabet


    random_alphabet = random.randint(0, len(alphabet)-1)
    random_Emoji = random.randint(0, len(emojisSpam)-1) #oder 21

    random_comment = random.randint(0, 1)    #50% chance für ein kommentar
    random_comment_Picture = random.randint(0, len(commentPicture)-1)
    random_comment_Video = random.randint(0, len(commentVideo)-1)



    
        
    #like
    if HowManyLikes >= 1:
        x = liken()
        beenden()
        if x == "k":
            beenden()
            anzahl_der_prozesse += 1
            x, y, istVideoOderNicht = MausPosition("next")
            beenden()
            py.moveTo(x, y)        #next post
            beenden()
            time.sleep(float_random_more_capa)
            beenden()
            py.click()
            beenden()
            py.moveTo(x+100, y+100)       
            beenden()
            print(str(anzahl_der_prozesse) + " Prozesse wurden gestartet")
            continue
        else:
            print("after like")
            beenden()
            HowManyLikes -= 1






#comments
    if HowManyComments >= 1:
        if random_comment <= 0:
            deaktivate = MausPosition("deaktiviert")
            
            if deaktivate == "yes": #check if comments are deaktivated
                x, y, istVideoOderNicht  = MausPosition("next")
                anzahl_der_prozesse += 1
                print(str(anzahl_der_prozesse) + " Prozesse wurden gestartet")


                py.moveTo(x, y)        #next post
                time.sleep(float_random_more_capa)
            
                py.click()
                py.moveTo(x+100, y+100) 
                print("kommentar skippen (weil deaktiviert)")
                continue
    
            else: #comments are not deaktivated

                kommentar()
                beenden()
                x, y, istVideoOderNicht = MausPosition("next")
                anzahl_der_prozesse += 1
                print(str(anzahl_der_prozesse) + " Prozesse wurden gestartet")
                beenden()
                py.moveTo(x, y)        #next post
                beenden()
                time.sleep(float_random_more_capa)
                beenden()
                py.click()
                beenden()
                py.moveTo(x+100, y+100) 
                beenden()
                HowManyComments -= 1


        else: #goes to the next post
            x, y, istVideoOderNicht = MausPosition("next")
            anzahl_der_prozesse += 1
            print(str(anzahl_der_prozesse) + " Prozesse wurden gestartet")
            beenden()
            py.moveTo(x, y)        #next post
            beenden()
            time.sleep(float_random_more_capa)
            beenden()
            py.click()
            beenden()
            py.moveTo(x+100, y+100) 
            beenden()
        



