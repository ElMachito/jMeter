#SmokeTest user A
from sikuli.Sikuli import *
import glob
import os
import subprocess
import ConfigParser
#import string
#import commands

config = ConfigParser.RawConfigParser()

config.read('C:\\SikuliTest\\UserA.ini')

global WebPath
WebPath =('Z:\\ZZZautomation\\Web\\')


BuildPath = ("Z:\BUILDS\Daily_BUILDS\QA_MainBranch_Install\*.install")
BuildNumber =  glob.glob("Z:\BUILDS\Daily_BUILDS\QA_MainBranch_Install\*.install")
for filename in BuildNumber:
    SmokeTestInfo = "SmokeTest_Build " + filename[45:50] + " Iteration 45"+".htm"
global Number
Number = filename[45:50]

global SmokeTest
SmokeTest = SmokeTestInfo

global count
count = 0


f = open(WebPath + SmokeTest,'a')
#f.write('SmokeTest Build' + Number + '<br />')
f.write('<font color= "#0000FF">A_configuration file read successfully</font><br />')
f.close()


#Install parameters
dirname = config.get('Install', 'dirname')
filespec = config.get('Install', 'filespec')

#SignIn parameters
BundlePathSignIn = config.get('SignIn','BundlePathSignIn')
LoginUser = config.get('SignIn','LoginUser')
Password = config.get('SignIn','Password')
PasswordInputField = config.get('SignIn','SignIn_PasswordInput')
Launch = config.get('SignIn','SignIn_Launch')
LoginPanel = config.get('SignIn','SignIn_BlankPanel')
FullLoginPanel = config.get('SignIn','SignIn_BlankPanel')
TOF1L = config.getint('SignIn','TOF1L')
TOF2L = config.getint('SignIn','TOF2L')
SignIn_Button = config.get('SignIn','SignIn_SignInButton')
TOF1LS = config.getint('SignIn','TOF1LS')
TOF2LS = config.getint('SignIn','TOF2LS')
SignIn_EULA = config.get('SignIn','SignIn_EULA')
SignIn_OKButton = config.get('SignIn','SignIn_OKButton')
TOF1E = config.getint('SignIn','TOF1E')
TOF2E = config.getint('SignIn','TOF2E')
TOF1S = config.getint('SignIn', 'TOF1S')
TOF2S = config.getint('SignIn','TOF2S')
SignIn_SignIn = config.get('SignIn','SignIn_SignIn')#not sure of the function


#EULA parameters
BundlePathEULA = config.get('EULA','BundlePathEULA')
SignIn_EULA = config.get('EULA','SignIn_EULA')
SignIn_MediaRouter = config.get('EULA','SignIn_MediaRouter')

#MediaRouter parameters
BundlePathM = config.get('MediaRouter','BundlePathMediaRouter')
SignIn_MediaRouter = config.get('MediaRouter','SignIn_MediaRouter')
TOF1M = config.getint('MediaRouter','MediaRouter_TOF1M')
TOF2M = config.getint('MediaRouter','MediaRouter_TOF2M')
TOF3M = config.getint('MediaRouter','MediaRouter_TOF3M')
TOF4M = config.getint('MediaRouter','MediaRouter_TOF4M')
SignIn_OKButton = config.get('MediaRouter','SignIn_OKButton')

#AddContact_AtoB parameters
BundlePathCL = config.get('ContactList','BundlePathContactList')
ContactList_WelcomePanel = config.get('ContactList','ContactList_WelcomePanel')
ContactList_Add = config.get('ContactList','ContactList_Add')
ContactList_AddContact = config.get('ContactList','ContactList_AddContact')
ContactList_AddContactUser = config.get('ContactList', 'ContactList_AddContactUser')#Add a path to user B login ID
ContactList_GreenDot = config.get('ContactList','ContactList_GreenDot')
ContactList_TOF1CL = config.getint('ContactList','TOF1CL')
ContactList_TOF2CL = config.getint('ContactList','TOF2CL')
ContactList_AcceptAddToList = config.get('ContactList','ContactList_AcceptAddToList')
ContactList_TOF3CL = config.getint('ContactList','AcceptAddToList_TOF3CL')
ContactList_TOF4CL = config.getint('ContactList','AcceptAddToList_TOF4CL')
ContactList_TOF5CL = config.getint('ContactList','TOF5CL')
ContactList_TOF6CL = config.getint('ContactList','TOF6CL')
ContactList_TOF9CL = config.getint('ContactList','TOF9CL')
ContactList_TOF10CL = config.getint('ContactList','TOF10CL')
ContactList_TOF11CL = config.getint('ContactList','TOF11CL')
ContactList_TOF12CL = config.getint('ContactList','TOF12CL')

#contactList remove contact
ContactList_MessageVerifyRemoval= config.get('ContactList','ContactList_MessageVerifyRemoval')

#contactList sign out
ContactList_SignOut = config.get('ContactList','ContactList_SignOut')
ContactList_DropList = config.get('ContactList','ContactList_DropList')


#Conference
BundlePathCF = config.get('Conference','BundlePathConference')
Conference_GreenDot = config.get('Conference','Conference_GreenDot')
Conference_ControlPanel = config.get('Conference','Conference_ControlPanel')
Conference_BlueLaunchWindow = config.get('Conference','Conference_BlueLaunchWindow')
Conference_Start = config.get('Conference','Conference_Start')
Conference_InConferenceSpeaker = config.get ('Conference', 'Conference_InConferenceSpeaker')
Conference_MeetingSetupTimeout = config.get ('Conference', 'Conference_MeetingSetupTimeout')
Conference_MeetingRequestDeclined = config.get ('Conference', 'Conference_MeetingRequestDeclined')
Conference_Close = config.get ('Conference', 'Conference_Close')
Conference_Leave = config.get ('Conference', 'Conference_Leave')
Conference_AcceptMeetingRequest = config.get('Conference','Conference_AcceptMeetingRequest')
TOF5CL = config.getint('Conference','TOF5CL')
TOF6CL = config.getint('Conference','TOF6CL')
Conference_ViewingLens = config.get ('Conference', 'Conference_ViewingLens')
Conference_EndedAllLeft = config.get ('Conference', 'Conference_EndedAllLeft')
Conference_DrawLens = config.get ('Conference', 'Conference_DrawLens')
Conference_StopSharing = config.get('Conference','Conference_StopSharing')
TOF7CL = config.getint('Conference','TOF7CL')
TOF8CL = config.getint('Conference','TOF8CL')

#desktop
BundlePathDK = config.get('Desktop','BundlePathDesktop')
Desktop_ExpandSysTray = config.get('Desktop','Desktop_ExpandSysTray')
Desktop_SysTrayClose = config.get('Desktop','Desktop_SysTrayClose')
Desktop_SysTraySkyRoomIcon = config.get('Desktop','Desktop_SysTrayIcon')
Desktop_SysTrayIcon = config.get ('Desktop', 'Desktop_SysTrayIcon_RTClickMenu')
Desktop_TOF1DK = config.getint('Desktop','TOF1DK')
Desktop_TOF2DK = config.getint('Desktop','TOF2DK')

setShowActions(True)# shows all activity in the GUI


def SignOut():
    setBundlePath(BundlePathCL)
    global SmokeTest
    global WebPath
    wait(5)
    if exists(ContactList_DropList, 20):
        click (Pattern(ContactList_DropList).targetOffset(ContactList_TOF9CL,ContactList_TOF10CL))
        wait(3)
        type (Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_SignOut sign out</font><br />')
        f.close()
    wait(10)
#    if exists(LoginPanel,FOREVER):
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_fail to exit</font><br />')
#        f.close()
#        wait(10)
#        SignOut()


def RemoveContact():
    setBundlePath(BundlePathCL)
    global SmokeTest
    global WebPath
    if exists(ContactList_GreenDot):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_RemoveContact found contact to remove</font><br />')
        f.close()
        wait(5)
        rightClick(ContactList_GreenDot)
        type(Key.DOWN + Key.ENTER)
        if exists(ContactList_MessageVerifyRemoval, 10):
            click(Pattern(ContactList_MessageVerifyRemoval).targetOffset(TOF5CL,TOF6CL))
            f = open(WebPath + SmokeTest,'a')
            f.write('<font color="#0000FF">A_RemoveContact contact removed</font><br />')
            f.close()



def LeaveConference():

    setBundlePath(BundlePathCF)
    global SmokeTest
    global WebPath
    wait(10)
    click(Pattern(Conference_Leave))
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_LeaveConference left conference</font><br />')
    f.close()

def AllLeftConference():
    setBundlePath (BundlePathCF)
    global SmokeTest
    global WebPath
    if exists(Conference_EndedAllLeft,30):
        wait(5)
        click(Pattern(Conference_EndedAllLeft).targetOffset(TOF7CL,TOF8CL))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#347C2C">A_AllLeftConference</font><br />')
        f.close()
    else:
        pass


def UserADrawsLens():
    setBundlePath(BundlePathCF)
    global SmokeTest
    global WebPath
    wait(10)
    if exists(Conference_ControlPanel,FOREVER ):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_UserADrawsLens control panel present</font><br />')
        f.close()
        wait(10)
        click(Conference_DrawLens)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_UserADrawsLens drawing lens</font><br />')
        f.close()
        setShowActions(True)
        x1, y1, x2, y2 = (100, 100, 500, 600)
        start = Location(x1, y1)
        end = Location(x2, y2)
        stepX = 1 # adjust this as needed
        stepY = int((y2-y1)/((x2-x1)/stepX))
        run = start
        mouseMove(start); wait(1)
        mouseDown(Button.LEFT); wait(1)
        while run.getX() < end.getX():
            run = run.right(stepX).below(stepY) # use below instead of down a
        mouseMove(run)
        mouseMove(end)
        mouseUp()
        wait(5)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_UserADrawsLens lens drawn</font><br />')
        f.close()
        wait (10)
        click (Conference_StopSharing)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_UserADrawsLens stop sharing the lens</font><br />')
        f.close()


def ConferenceInviteAtoB():
    setBundlePath(BundlePathCF)
    global SmokeTest
    global WebPath
    #click on the avaliable user green dot at top contact anonymous to sender
    if exists(Conference_GreenDot, FOREVER): # verifying confernce invite is sent only when recipient is ready
        wait(30)
        click(Conference_GreenDot)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ConferenceInviteAtoB enable user for invite</font><br />')
        f.close()
    if exists(Conference_BlueLaunchWindow, 10): # check for the color change
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ConferenceInviteAtoB user ready for invite</font><br />')
        f.close()
        wait(10)
        click(Conference_Start)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ConferenceInviteAtoB invite sent</font><br />')
        f.close()
    if exists(Conference_InConferenceSpeaker, FOREVER):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ConferenceInviteAtoB meeting request accepted</font><br />')
        f.close()#fails to find the minispeaker


def AddContact_AtoB():
    setBundlePath(BundlePathCL)
    global SmokeTest
    global WebPath
    if exists(ContactList_WelcomePanel, 20):
        wait(20)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_AddContact_AtoB begin add user</font><br />')
        f.close()
        #need to add check for contact list panel with contacts
        click(ContactList_Add)
        wait(2)
        type(Key.DOWN)
        wait(1)
        type(Key.ENTER) #Launches the add contact dialog
        wait(2)# wait displays the add contact hover window
    if exists(ContactList_AddContact, 20):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_AddContact_AtoB add contact dialog displayed</font><br />')
        f.close()
        type(ContactList_AddContactUser)
        wait(10)
        click(Pattern(ContactList_AddContact).targetOffset(ContactList_TOF1CL,ContactList_TOF2CL))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_AddContact_AtoB verified user id exists</font><br />')
        f.close()
        wait(10)
    if exists(ContactList_GreenDot, 60):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_AddContact_AtoB add contact successful</font><br />')
        f.close()
        wait(10)



def MediaRouter():

    setBundlePath(BundlePathM)
    global SmokeTest
    global WebPath
    wait(1)
    if exists(SignIn_MediaRouter, 30):
        click(Pattern(SignIn_MediaRouter).targetOffset(TOF1M, TOF2M))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_MediaRouter media router droplist found</font><br />')
        f.close()
        wait(1)#wait needed to support droplist navigation
        type(Key.DOWN + Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)# selects Fort Collins
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_MediaRouter Fort Collins selected</font><br />')
        f.close()
        wait(3)
        #click(Pattern(SignIn_MediaRouter).targetOffset(123,63))
        click(Pattern(SignIn_MediaRouter).targetOffset(TOF3M, TOF4M))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_MediaRouter media router submitted</font><br />')
        f.close()
        wait(5)
    else:
        pass

def LoopSignIn():
    setBundlePath(BundlePathSignIn)
    global SmokeTest
    global WebPath
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_LoopSignIn Login user A is ' + LoginUser + '</font><br />')
    f.close()
    if exists(SignIn_EULA, 5):
        click(Pattern(SignIn_EULA))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#FF0000">A_LoopSignIn ERROR EULA shown after user accepted during initial sign in ERROR</font><br />')
        f.close()
    if exists (ContactList_WelcomePanel, 30):
        wait(1)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_LoopSignIn user automatically signed in</font><br />')
        f.write('<font color="#0000FF">A_LoopSignIn welcome panel detected</font><br />')
        f.close()
#        type(Pattern(SignIn_SignIn).targetOffset(TOF1S,TOF2S), LoginUser)
#        wait(1)
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_LoopSignIn login user entered</font><br />')
#        f.close()
#        type(Pattern(PasswordInputField).targetOffset(TOF1L,TOF2L), Password)
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_LoopSignIn password entered</font><br />')
#        f.close()
#        wait(1)
#        click (Pattern(SignIn_OKButton))
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_LoopSignIn credentials submitted</font><br />')
#        f.close()
#        #add negative submission check and loop
#        wait(1)



def FirstSignIn():

    setBundlePath(BundlePathSignIn)
    global SmokeTest
    global WebPath
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_FirstSignIn Login user A is ' + LoginUser + '</font><br />')
    f.close()
    if exists (FullLoginPanel, 30):
        wait(1)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_FirstSignIn login panel detected</font><br />')
        f.close()
        type(Pattern(SignIn_SignIn).targetOffset(TOF1S,TOF2S), LoginUser)
        wait(1)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_FirstSignIn login user entered</font><br />')
        f.close()
        type(Pattern(PasswordInputField).targetOffset(TOF1L,TOF2L), Password)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_FirstSignIn password entered</font><br />')
        f.close()
        wait(1)
        click (Pattern(SignIn_OKButton))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_FirstSignIn credentials submitted</font><br />')
        f.close()
        wait(1)
    if exists(SignIn_EULA, 30):
        click(Pattern(SignIn_EULA))
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_FirstSignIn EULA accepted</font><br />')#add handler for if the image does not exist
        f.close


def Uninstall():
    global SmokeTest
    global WebPath
    setBundlePath(BundlePathSignIn)
    dirname = "Z:\BUILDS\Daily_BUILDS\QA_MainBranch_Install\*.install"
    filespec = "setup.exe"
    instlpath = glob.glob (os.path.join (dirname, filespec))
    subprocess.call (instlpath[0] + ' /S /z" /U /A"')
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_Uninstall uninstalling build' + Number +'</font><br />')
    f.close()
    if not exists(Launch, 60):
        wait(1)
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_Uninstall successfuly uninstalled build' + Number +'</font><br />')
        f.close()




def Install():

    dirname = "Z:\BUILDS\Daily_BUILDS\QA_MainBranch_Install\*.install"
    setBundlePath(BundlePathSignIn)
    global SmokeTest
    global WebPath
    filespec = "setup.exe"
    instlpath = glob.glob (os.path.join (dirname, filespec))
    subprocess.call (instlpath[0] + ' /S')#Copy this to all installer
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_Install installing build' + Number +'</font><br />')
    f.close()
    while not exists(Launch, FOREVER):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_Install successfully installed build' + Number+ '</font><br />')
        f.close()




def ExitVCDKillProcess():
    setBundlePath (BundlePathDK)
    global SmokeTest
    global WebPath
    click(Pattern(Desktop_ExpandSysTray).targetOffset(0,0))
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#0000FF">A_ExitVCDKillProcess system tray expanded</font><br />')
    f.close()
    if exists(Desktop_SysTraySkyRoomIcon, 10):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ExitVCDKillProcess click on the VCD icon</font><br />')
        f.close()
        rightClick (Desktop_SysTraySkyRoomIcon)
        type(Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER )#keys down to the exit command of the Right Click menu
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ExitVCDKillProcess exit selected from the VCD menu</font><br />')
        f.close()
        rightClick (Desktop_SysTrayClose)#Right click called to close the systray menu via the escape key
        type(Key.ESC)#closes the systray window
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ExitVCDKillProcess VCD exited</font><br />')
        f.close()
        wait(2)
    else:
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_ExitVCDKillProcess VCD icon not found</font><br />')
        f.close()



#def VerifyVCDDesktopIconExists():
#    setBundlePath(BundlePathSignIn)
#    global SmokeTest
#    global WebPath
#    if exists(Launch,10):
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_ExitVCDProcess function launched</font><br />')
#        f.close()
#    else:
#        f = open(WebPath + SmokeTest,'a')
#        f.write('<font color="#0000FF">A_desktop VCD icon not found, begin install</font><br />')
#        f.close()



def LaunchApp():
    setBundlePath(BundlePathSignIn)
    global SmokeTest
    global WebPath
    wait(5)
    if exists(Launch, 10):
        doubleClick(Pattern(Launch))
    else:
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#FF000">A_LaunchApp find VCD icon failed</font><br />')
        f.write('<font color="#0000FF">A_LaunchApp retry finder VCD icon</font><br />')
        f.close()
        LaunchApp()
    if exists(FullLoginPanel, 10): # Looking for the login screen
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#0000FF">A_LaunchApp launches VCD</font><br />')
        f.close()
        wait(1)



def LoopSignInConferenceExit():
    global SmokeTest
    global WebPath
    global count
    count = 0
    while (count < 10):

        f = open(WebPath + SmokeTest,'a')
        f.write('A_LaunchApp iteration ' + (str (count)) + '<br />')
        f.close()
        LaunchApp()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_LoopSignIn iteration ' + (str (count)) + '<br />')
        f.close()
        LoopSignIn()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_AddContactAtoB iteration ' + (str (count)) + '<br />')
        f.close()
        AddContact_AtoB()#needs synch

        f = open(WebPath + SmokeTest,'a')
        f.write('A_ConferenceInviteAtoB iteration ' + (str (count)) + '<br />')
        f.close()
        ConferenceInviteAtoB()#needs synch

        f = open(WebPath + SmokeTest,'a')
        f.write('A_UserADrawsLens iteration ' + (str (count)) + '<br />')
        f.close()
        UserADrawsLens()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_LeaveConference iteration ' + (str (count)) + '<br />')
        f.close()
        LeaveConference()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_AllLeftConference iteration ' + (str (count)) + '<br />')
        f.close()
        AllLeftConference()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_RemoveContact iteration ' + (str (count)) + '<br />')
        f.close()
        RemoveContact()

        f = open(WebPath + SmokeTest,'a')
        f.write('A_SignOut iteration ' + (str (count)) + '<br />')
        f.close()
        SignOut()
        count = count + 1
    f = open(WebPath + SmokeTest,'a')
    f.write('A_ Smoke test Complete' + (str (count)) + '<br />')
    f.close()
    exit()

def FirstPass():
    global SmokeTest
    global WebPath
    global count
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_Firstpass executing</font><br />')
    f.close()
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_LaunchApp executing </font><br />')
    f.close()
    LaunchApp()

    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_FirstSignIn executing </font><br />')
    f.close()
    FirstSignIn()

    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_Media Router executing</font><br />')
    f.close()
    MediaRouter()

    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_SignOut executing </font><br />')
    f.close()
    SignOut()

def MasterInstall():
    global count
    global SmokeTest
    global WebPath
    setBundlePath(BundlePathSignIn)
    f = open(WebPath + SmokeTest,'a')
    f.write('<font color="#000000">A_MasterInstall executing</font><br />')
    f.close()
    if exists(Launch,10):
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#000000">A_ExitVCDKillProcess executing</font><br />')
        f.close()
        ExitVCDKillProcess()

        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#000000">A_Uninstall executing</font><br />')
        f.close()
        Uninstall()

        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#000000">A_Install executing</font><br />')
        f.close()
        Install()
    else:
        f = open(WebPath + SmokeTest,'a')
        f.write('<font color="#000000">A_Install executing</font><br />')
        f.close()
        Install()




#MasterInstall()
#FirstPass()
LoopSignInConferenceExit()