#new #new 
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime   
import wikipedia # pip install wikipedia # To acess wikipedia directly
import webbrowser  #
import os
import smtplib
import time
import selenium
from selenium import webdriver
# from selenium.webdriver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # used for  detaching  driver , bcoz of which the driver is not closed 
from selenium.webdriver.common.action_chains import ActionChains
from word2number import w2n




master="Vignesh"
myName="chitti"
DOB="8th january 2021"  #jarvis DOB

print(f"...........intializing  {myName}...............")
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning vignesh. Now the time is around {0} am".format(hour))
    elif hour<18:
        speak("Good afternoon vignesh. Now the time is around {0} pm".format(hour))
    elif hour<21 :
        speak("Good evening vignesh. Now the time is around {0} pm ".format(hour))
    else:
        speak("Good night vignesh. Now the time is around {0} pm , you better go to sleep .".format(hour))

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold=0.6
        audio=r.listen(source)
       

    try:
        #print("Recognition...")
        query=r.recognize_google(audio,language="en-in")
        #print(f"user said:{query}\n")

    except Exception as e:
        print("cant recognize u for a instance of 0.6 seconds")
        query= None
        mainif()

    return query


error=" Dirty fellow , idiot , buffalo  , waste fellow not having any common sense , you havent coded me any thing about this "
scoldme=" Dirty fellow , idiot , buffalo , waste fellow not having any common sense "

#Main programme starts
speak(f"{myName} intialized...")

# wishme()
#speak(" How may i help you?")
#query=0
#query=takecommand()
#print(query)

#Basic tasks

def mainif():
            query=takecommand()
            query=query.lower()
            print(query)

            if myName in query:
                 query=query.replace(myName,"")

            # if "active" in query and "mode" in query:
            #     query=str(query)+myName
            #     mainif()

            # if "sleep" in query and "mode" in query:
            #     query=query.replace(myName,'')    

            if "introduce" in query:
                if ("introduce" and "your" and "self") :
                    speak(f" Helloo ... , I am {myName} , speed 2 giggahertz , memory half terabyte , I was created by Vignesh Reddy J , I am here to help him")
                    mainif()


            if ("join" in query and "class" in query) or ("open" in query and "class" in query): #KMIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://kmitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("*****") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("*****")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                driver.implicitly_wait(50000)

                ele_join=driver.find_element_by_xpath("//*[@id='region-main']/div/div/div/div/div[3]/a/span").click()
                Options().add_experimental_option("detach",True)
                time.sleep(500)
                speak("opened")
                mainif()


            elif ( "speakout" in query and "table" in query) or ( "speak out" in query and "table" in query) :
                query=query.replace("speak","")
                query=query.replace("out","")

                query=query.replace("table","")
                query=query.replace(" ","")
                # query.replace("se","")
                print(query)
                if (query.isdigit()):
                    t=int(query)
                    speak (    
                        f"{t} into 1 , {t*1}   , "
                        f"{t} into 2 , {t*2}   , "
                        f"{t} into 3 , {t*3}   , "
                        f"{t} into 4 , {t*4}   , "
                        f"{t} into 5 , {t*5}   , "
                        f"{t} into 6 , {t*6}   , "
                        f"{t} into 7 , {t*7}   , "
                        f"{t} into 8 , {t*8}   , "
                        f"{t} into 9 , {t*9}   , "
                        f"{t} into 10 , {t*10} ,   ")

                else:
                    query=w2n.word_to_num(query)
                    t=0
                    
                    t=int(query)
                    speak (    
                        f"{t} into 1 , {t*1}   , "
                        f"{t} into 2 , {t*2}   , "
                        f"{t} into 3 , {t*3}   , "
                        f"{t} into 4 , {t*4}   , "
                        f"{t} into 5 , {t*5}   , "
                        f"{t} into 6 , {t*6}   , "
                        f"{t} into 7 , {t*7}   , "
                        f"{t} into 8 , {t*8}   , "
                        f"{t} into 9 , {t*9}   , "
                        f"{t} into 10 , {t*10} ,   "






                )
                mainif()
            
            elif "hello" in query:
                speak("hlo {0}".format(master))
                mainif()

            elif "your" in query and "name" in query:
                speak("My name is {0}".format(myName))
                mainif()
        
            elif "your" in query and "date" in query and "birth" in query:
                speak("I am initially initialized on {0}".format(DOB))
                mainif()

            elif "when"in query and "born" in query:
                speak("I am initially initialized on {0}".format(DOB))
                mainif()
                

            elif "open"in query and "python"in query and "ppt"in query and "page" in query: #NGIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://ngitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("******") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("********")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                ele_studyMaterialPage=driver.find_element_by_xpath("//*[@id='region-main']/div/div/ul/li[6]/a").click()
                ele_kmit=driver.find_element_by_xpath("//*[@id='KMIT_anchor']")
                ActionChains(driver).double_click(ele_kmit).perform()

                ele_firstYear=driver.find_element_by_xpath("//*[@id='KMIT/1st-year_anchor']")
                ActionChains(driver).double_click(ele_firstYear).perform()

                ele_ppt=driver.find_element_by_xpath("//*[@id='KMIT/1st-year/PPT_anchor']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
                
            


            elif "open"in query and "tessellator"in query and "ngit" in query: #NGIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://ngitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("******") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("******")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
                
            

            elif "open"in query and "tessellator" in query: #KMIT
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("http://kmitonline.com/login/index.php")
                ele_user=driver.find_element_by_xpath("//*[@id='username']")  # or ele=driver.find_element_by_name("username")
                ele_user.send_keys("******") #  sends the text inside and fills it

                ele_pass=driver.find_element_by_name("password")
                ele_pass.send_keys("******")

                ele_login=driver.find_element_by_xpath("//*[@id='loginbtn']").click()
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
                

            elif ("open google") in  query:
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window()
                driver.get("https://www.google.com/")
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()

            elif ("google") in query:
                speak("opening")
                if myName in query:
                    query=query.replace(myName,"")
                query=query.replace("google","")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window()
                driver.get("https://www.google.com/")
                ele_search=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                ele_search.send_keys(query)
                ele_search.send_keys(Keys.ENTER)
                Options().add_experimental_option("detach",True)
                speak("opened")
                mainif()
            
            


                





            elif "what is" in query:#if "what is " there in our query then it will execute this function
                speak("opening")
                query=query.replace("what is","")
                results=wikipedia.summary(query,sentences=2)
                speak(results)
                mainif()


            elif "calculate"  in query or "add" in query  or "subtract" in query or "multiply"  in query : #This uses eval function when our query involves the word calculate
                if "calculate" in query:
                    query=query.replace("calculate","")
                    if "into" in query:
                            query=query.replace("into","*")
                            query=eval(query)
                            speak(query) 
                            
                            
                        
                    else :
                        query=eval(query)
                        speak(query)
                    mainif()
                

                if "add" in query:
                    query=query.replace("add","")
                    query=eval(query)
                    speak(query)
                    mainif()
                if "subtract" in query:
                    query=query.replace("subtract","")
                    query=eval(query)
                    speak(query)
                    mainif()

                if "multiply" in query:
                    if "into" in query:
                            query=query.replace("into","*")
                            query=eval(query)
                            speak(query)
                            mainif()


            elif "wastefellow" in query: #is ... a waste fellow
                query=query.replace("a waste fellow","")
                query=query.replace("is","")
                speak(" Dirty fellow {0}, idiot {0} , buffalo {0}, waste fellow {0} not having any common sense ".format(query))
                time.sleep(1)
                mainif()
            elif "waste fellow" in query: #is ... a waste fellow
                query=query.replace("a waste fellow","")
                query=query.replace("is","")
                speak(" Dirty fellow {0}, idiot {0} , buffalo {0}, waste fellow {0} not having any common sense ".format(query))
                time.sleep(1)
                mainif()

            elif "the time" in query:
                strtime=datetime.datetime.now().strftime("%H:%M")
                speak(f"The , time is {strtime}")
                time.sleep(1)
                mainif()

            elif "open youtube" in query:#opens youtube 
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("https://www.youtube.com/?feature=ytca")
                speak("opened")
            
                mainif()

            elif "open whatsapp" in query:#opens youtube 
                speak("opening")
                driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver_win32\\chromedriver.exe')
                driver.maximize_window() #will maximize the page
                # driver.implicitly_wait(5) #this function is used to stop the execution of programme for the specified time in seconds , when an element is not still loaded , if it is already loaded then this will not wait , this function should be used only once in a programme block as this will be applicable to all the elements
                driver.get("https://web.whatsapp.com/")
                speak("opened")
                mainif()

            elif "open" in query  and "vs code" in query:
                speak("opening")
                codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
                os.startfile(codepath)
                speak("opened")
                mainif()
            

            elif "hai" in query:
                speak(" hai {0}".format(master))
                mainif()

            elif "ask" in query  and "me" in query  and "question" in query:
                speak("{0} why dont you get any idea?".format(master))
                mainif()

            elif "say" in query  and "why" in query:
                speak("you are not having any brain , that the reason ")
                mainif()
            
            elif "sleep" in query:
                speak("ok bye {0}.".format(master))
                

            elif "sleepmode" in query:
                speak("ok bye {0}.".format(master))

            elif "thank you" in query:
                speak("ok bye {0}.".format(master))

            elif "bye" in query:
                speak("ok bye {0}.".format(master))

            elif ("update" and "yourself") in query:
                        
                with open("‪\\..\\..\\..\\Python\\jarvis\\main.py") as f:
                    newcontent=f.read()

                with open("\\..\\..\\..\\Users\\DELL\\main.py","w") as f:
                    f.write(newcontent)

                speak("updated succesfully")
            
            

            elif "class" in query and "next" in query:
                day=int(datetime.datetime.today().strftime("%w"))
                timenow=datetime.datetime.now().strftime("%H:%M")
                hournow=int(datetime.datetime.now().strftime("%H"))
                minnow=int(datetime.datetime.now().strftime("%M"))

                #Monday
                class11="B E E"
                time11="9:30 AM"
                hour11=int(9)
                min11=int(30)
                mine11=int(50)

                class12="chemistry"
                time12="11 AM"
                hour12=int(11)
                min12=int(0)
                mine12=0

                class13="English"
                time13="12:15 PM"
                hour13=int(12)
                min13=int(15)
                mine13=int(15)


                class14="M 1"
                time14="2:15 PM"
                hour14=int(14)
                min14=int(15)
                mine14=int(45)



                #day 2 i.e tuesday
                
                class21="Chemistry"
                time21="9:30 AM"
                hour21=int(9)
                min21=int(30)
                mine21=int(50)

                class22="Python"
                time22="11 AM"
                hour22=int(11)
                min22=int(0)
                mine22=int(0)

                class23="M 1 lab"
                time23="2:15 PM"
                hour23=int(14)
                min23=int(15)
                mine23=int(45)
                
                
                #day 3 i.e wednesday
                
                class31="Chemistry"
                time31="9:30 AM"
                hour31=int(9)
                min31=int(30)
                mine31=int(50)

                class32="M1"
                time32="11 AM"
                hour32=int(11)
                min32=int(0)
                mine32=0

                class33="B E E"
                time33="12:15 PM"
                hour33=int(12)
                min33=int(15)
                mine33=int(15)


                class34="Chemistry"
                time34="2:15 PM"
                hour34=int(14)
                min34=int(15)
                mine34=int(45)



                # day 4 i.e thursday
                class41="M 1"
                time41="9:30 AM"
                hour41=int(9)
                min41=int(30)
                mine41=int(50)

                class42="Python"
                time42="11 AM"
                hour42=int(11)
                min42=int(0)
                mine42=int(0)

                class43="chemistry"
                time43="2:15 PM"
                hour43=int(14)
                min43=int(15)
                mine43=int(45)
                
                
                #friday i.e day 5
                    
                
                class51="B E E"
                time51="9:30 AM"
                hour51=int(9)
                min51=int(30)
                mine51=int(50)

                class52="M 1"
                time52="11 AM"
                hour52=int(11)
                min52=int(0)
                mine52=0

                class53="English"
                time53="12:15 PM"
                hour53=int(12)
                min53=int(15)
                mine53=int(15)


                class54="Mentor"
                time54="2:15 PM"
                hour54=int(14)
                min54=int(15)
                mine54=int(45)

                #saturday i.e day 6

                class61="English"
                time61="9:30 AM"
                hour61=int(9)
                min61=int(30)
                mine61=int(50)

                class62="Python"
                time62="11 AM"
                hour62=int(11)
                min62=int(0)
                mine62=int(0)

                class63="B E E"
                time63="2:15 PM"
                hour63=int(14)
                min63=int(15)
                mine63=int(45)
                

                #sunday
                if day==0:
                    speak("Rock the day {0} you are not having any class, its sunday".format(master))

                #Monday
                if day==1: 
                    if hournow<(hour11+1) : #class at 9:30
                        if hournow==hour11:  # if time greater than 9
                            if minnow<min11:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class11,int(((hour11-hournow)*60)+(min11-minnow)),time11))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class11,int(((hournow-hour11)*60)+(minnow-min11)),time11))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class11,int(((hour11-hournow)*60)+(min11-minnow)),time11))
                    elif hournow==(hour11+1):
                        if minnow<mine11:
                         speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class11,int(((hournow-hour11)*60)+(minnow-min11)),time11))
                        else:
                          speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class12,int(((hour12-hournow)*60)+(min12-minnow)),time12))

                    elif hournow<(hour12+1) :
                        if hournow==hour12:  
                            if minnow<min12: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class12,int(((hour12-hournow)*60)+(min12-minnow)),time12))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class12,int(((hournow-hour12)*60)+(minnow-min12)),time12))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class12,int(((hour12-hournow)*60)+(min12-minnow)),time12))
                    elif hournow==hour12+1:
                        if minnow<mine12:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class12,int(((hournow-hour12)*60)+(minnow-min12)),time12))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
                    
                    elif hournow<(hour13+1) : #class at 9:30
                        if hournow==hour13:  # if time greater than 9
                            if minnow<min13:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class13,int(((hournow-hour13)*60)+(minnow-min13)),time13))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
                    elif hournow==(hour13+1) :
                        if minnow<mine13:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class13,int(((hournow-hour13)*60)+(minnow-min13)),time13))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
                    elif hournow<(hour14+1) : #class at 9:30
                        if hournow==hour14:  # if time greater than 9
                            if minnow<min14:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class14,int(((hournow-hour14)*60)+(minnow-min14)),time14))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
                    elif hournow==(hour14+1) :
                        if minnow<mine14:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class14,int(((hournow-hour14)*60)+(minnow-min14)),time14))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")


                #Tuesday
                
                if day==2: 
                    if hournow<(hour21+1) : #class at 9:30
                        if hournow==hour21:  # if time greater than 9
                            if minnow<min21:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class21,int(((hour21-hournow)*60)+(min21-minnow)),time21))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class21,int(((hournow-hour21)*60)+(minnow-min21)),time21))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class21,int(((hour21-hournow)*60)+(min21-minnow)),time21))
                    elif hournow==(hour21+1):
                        if minnow<mine21:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class21,int(((hournow-hour21)*60)+(minnow-min21)),time21))
                        else:
                          speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))

                    elif hournow<(hour22+1) :
                        if hournow==hour22:  
                            if minnow<min22: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))
                    elif hournow==hour22+1:
                        speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
                    elif hournow==(hour22+2):
                        if minnow<mine22:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
                    
                    elif hournow<(hour23+1) : #class at 9:30
                        if hournow==hour23:  # if time greater than 9
                            if minnow<min23:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class23,int(((hournow-hour23)*60)+(minnow-min23)),time23))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
                    elif hournow==(hour23+1) :
                        if minnow<mine23:
                         speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class23,int(((hournow-hour23)*60)+(minnow-min23)),time23))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")
                #wednesday
                if day==3: 
                    if hournow<(hour31+1) : #class at 9:30
                        if hournow==hour31:  # if time greater than 9
                            if minnow<min31:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour31-hournow)*60)+(min31-minnow)),time31))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class31,int(((hournow-hour31)*60)+(minnow-min31)),time31))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour31-hournow)*60)+(min31-minnow)),time31))
                    elif hournow==(hour31+1):
                        if minnow<mine31:
                            speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class31,int(((hournow-hour31)*60)+(minnow-min31)),time31))
                        else:
                          speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))

                    elif hournow<(hour32+1) :
                        if hournow==hour32:  
                            if minnow<min32: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class32,int(((hournow-hour32)*60)+(minnow-min32)),time32))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))
                    elif hournow==hour32+1:
                        if minnow<mine32:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class32,int(((hournow-hour32)*60)+(minnow-min32)),time32))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
                    
                    elif hournow<(hour33+1) : #class at 9:30
                        if hournow==hour33:  # if time greater than 9
                            if minnow<min33:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class33,int(((hournow-hour33)*60)+(minnow-min33)),time33))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
                    elif hournow==(hour33+1) :
                        if minnow<mine33:
                            speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class33,int(((hournow-hour33)*60)+(minnow-min33)),time33))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
                    elif hournow<(hour34+1) : #class at 9:30
                        if hournow==hour34:  # if time greater than 9
                            if minnow<min34:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class34,int(((hournow-hour34)*60)+(minnow-min34)),time34))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
                    elif hournow==(hour34+1) :
                        if minnow<mine34:
                            speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class34,int(((hournow-hour34)*60)+(minnow-min34)),time34))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")


                #thursday
                if day==4: 
                    if hournow<(hour41+1) : #class at 9:30
                        if hournow==hour41:  # if time greater than 9
                            if minnow<min41:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class41,int(((hour41-hournow)*60)+(min41-minnow)),time41))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class41,int(((hournow-hour41)*60)+(minnow-min41)),time41))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class41,int(((hour41-hournow)*60)+(min41-minnow)),time41))
                    elif hournow==(hour41+1):
                        if minnow<mine41:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class41,int(((hournow-hour41)*60)+(minnow-min41)),time41))
                        else:
                          speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))

                    elif hournow<(hour42+1) :
                        if hournow==hour42:  
                            if minnow<min42: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))
                    elif hournow==hour42+1:
                        speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
                    elif hournow==(hour42+2):
                        if minnow<mine42:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
                    
                    elif hournow<(hour43+1) : #class at 9:30
                        if hournow==hour43:  # if time greater than 9
                            if minnow<min43:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class43,int(((hournow-hour43)*60)+(minnow-min43)),time43))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
                    elif hournow==(hour43+1) :
                        if minnow<mine43:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class43,int(((hournow-hour43)*60)+(minnow-min43)),time43))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")

                #Friday day 5
                if day==5: 
                    if hournow<(hour51+1) : #class at 9:30
                        if hournow==hour51:  # if time greater than 9
                            if minnow<min51:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class51,int(((hour51-hournow)*60)+(min51-minnow)),time51))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class51,int(((hournow-hour51)*60)+(minnow-min51)),time51))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour51-hournow)*60)+(min51-minnow)),time51))
                    elif hournow==(hour51+1):
                        if minnow<mine51:
                               speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class51,int(((hournow-hour51)*60)+(minnow-min51)),time51))
                        else:
                               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))

                    elif hournow<(hour52+1) :
                        if hournow==hour52:  
                            if minnow<min52: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class52,int(((hournow-hour52)*60)+(minnow-min52)),time52))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))
                    elif hournow==hour52+1:
                        if minnow<mine52:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class52,int(((hournow-hour52)*60)+(minnow-min52)),time52))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
                    
                    elif hournow<(hour53+1) : #class at 9:30
                        if hournow==hour53:  # if time greater than 9
                            if minnow<min53:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class53,int(((hournow-hour53)*60)+(minnow-min53)),time53))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
                    elif hournow==(hour53+1) :
                        if minnow<mine53:
                         speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class53,int(((hournow-hour53)*60)+(minnow-min53)),time53))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
                    elif hournow<(hour54+1) : #class at 9:30
                        if hournow==hour54:  # if time greater than 9
                            if minnow<min54:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class54,int(((hournow-hour54)*60)+(minnow-min54)),time54))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
                    elif hournow==(hour54+1) :
                        if minnow<mine54:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class54,int(((hournow-hour54)*60)+(minnow-min54)),time54))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")


                #saturday i.e day 6
                if day==6: 
                    if hournow<(hour61+1) : #class at 9:30
                        if hournow==hour61:  # if time greater than 9
                            if minnow<min61:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class61,int(((hour61-hournow)*60)+(min61-minnow)),time61))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class61,int(((hournow-hour61)*60)+(minnow-min61)),time61))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class61,int(((hour61-hournow)*60)+(min61-minnow)),time61))
                    elif hournow==(hour61+1):
                        if minnow<mine61:
                          speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class61,int(((hournow-hour61)*60)+(minnow-min61)),time61))
                        else:
                         speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))

                    elif hournow<(hour62+1) :
                        if hournow==hour62:  
                            if minnow<min62: 
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))
                    elif hournow==hour62+1:
                        speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
                    elif hournow==(hour62+2):
                        if minnow<mine62:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
                    
                    elif hournow<(hour63+1) : #class at 9:30
                        if hournow==hour63:  # if time greater than 9
                            if minnow<min63:  # if time less than 30 min
                                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
                            else:
                                speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class63,int(((hournow-hour63)*60)+(minnow-min63)),time63))
                        else:
                            speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
                    elif hournow==(hour63+1) :
                        if minnow<mine63:
                           speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class63,int(((hournow-hour63)*60)+(minnow-min63)),time63))
                        else:
                            speak("No more classes today , You have succesfully completed your classes. ")
                    else:
                        speak("No more classes today , You have succesfully completed your classes. ")
                        
                mainif()

            else:
                mainif()       

    # else:
    #     mainif()
   
mainif()

