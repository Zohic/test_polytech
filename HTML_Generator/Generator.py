import os
import msvcrt

from TagLib import *
appVer = 0.1
fatherName = "Zohich"
loadWarn = "!!! Note that you can only load projects from files created in this program !!!"
instructionLine = " You can create and save html files. \n Adding You can put tags at your page selecting line and tag or template \nAlso you can add script and styles to your page with built in text editor\n For exiting press esc button"
textEditorInfo = "You can use enter,tab and backspace. Only English. For finishing editing press esc\nNote that you cannot move your cursor over here"
screenWidth = 120
indent = "\n"+"-_"*int(screenWidth/2)+"\n"
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

projectName = ""
choice = -1
thePage = Html([
            
              ])

globalTags = [thePage]

redactorState=[0,        0,0]
#             [0]add tag

putLine = -1

tagList=""
tagList+="1. <div>\n"
tagList+="2. <a>\n"
tagList+="3. <img>\n"
tagList+="4. <br>\n"
tagList+="5. <p>\n"
tagList+="6. <title>\n"
tagList+="7. <meta>\n"
tagList+="8. <head>\n"
tagList+="9. <body>\n"
tagList+="10. <button>\n"
tagList+="11. <input>\n"
tagList+="12. <style>\n"
tagList+="13. <script>\n"


lastPage = 0
tagsAvaible = 13

textE=""

def GetTag(num):
    if num==1:
        return Div([])
    elif num==2:
        return A("")
    elif num==3:
        return Img("")
    elif num==4:
        return Br()
    elif num==5:
        return P("")
    elif num==6:
        return Title("")
    elif num==7:
        return Meta("")
    elif num==8:
        return Head([])
    elif num==9:
        return Body([])
    elif num==10:
        return Button("","")
    elif num==11:
        return Input()
    elif num==12:
        return Style("")
    elif num==13:
        return Script("")



def GetToPage(id):
    if id==0:
        MainMenu()
    elif id==1:
        Redactor()
    elif id==2:
        LoadingProject()
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def cls():
    os.system('cls')

def printC(theline:str):
    bars = int(screenWidth/2-len(theline))
    print(" "*bars+theline+" "*bars)

def GetChoice():
    global choice
    print(indent)
    try:
        choice = int(input("your choice: "))
    except BaseException:
        ErrorPage("INVALID INPUT")
   
def GetRangeChoice(min, max, err):
    global choice
    print(indent)
    try:
        choice = int(input("your choice: "))
    except BaseException:
        ErrorPage("INVALID INPUT")
        return False
    if choice>=min and choice<=max:
        return True
    else:
        ErrorPage(err)
        return False

"""
def LoadFromFile(fileName):
    global thePage
    file = open(fileName,"r")
    pg=None
    curTag=None
    gotTag = False
    gotAtr = False
    gotTxt = False
    lastParent = None
    wasEnd = False
    while True:
        
        sym = file.read(1)

        if sym=="":
            break
        else:
            if sym=='\n':
                wasEnd = True
            if sym=="<" and gotTag==False:
                tagName = ""
                while not (sym=='>' or sym==' '):
                    sym = file.read(1)
                    if sym=='/':
                        #if wasEnd:
                            #if not lastParent==None:
                                #lastParent = lastParent.parent
                        break
                    if not (sym=='>' or sym==' '):
                        tagName+=sym
                if not sym=='/':
                    for i in range(1,tagsAvaible+1):
                        tt = GetTag(i)
                        #print(tt.tagName)
                        if tagName==tt.tagName:
                            print("GOT")
                            curTag = tt
                            gotTag = True
                            print(curTag.tagName)
            if gotTag:
                atr=""
                while not sym=='>':
                    atr+=sym
                    sym=file.read(1)
                curTag.attributes = atr
                gotAtr = True
                print("got atr")

            if gotAtr:
                txt=""
                while not (sym=='<'):
                    sym=file.read(1)
                    txt+=sym
                gotTxt=True
                #curTag.text = txt
                print("gotEnd")
                if sym=='<':
                    print("AAA")
                    sym=file.read(1)
                    if sym=='/':
                        
                        if wasEnd:
                            print("EVENWAS")
                            wasEnd=False
                            if not lastParent==None:
                                print("PARENT IS NIT GONE")
                                curTag.parent = lastParent
                                curTag.parent.inside.append(curTag)
                                #if not lastParent.parent==None:
                                #    lastParent = lastParent.parent
                            else:
                                pass
                        print("/ but not END")
                    gotTag=False
                    gotAtr=False
                    gotTxt=False
                elif sym=='\n':
                    print("NEXT")
                    wasEnd = True
                    if pg==None:
                        print("GOT HTML")
                        pg=curTag
                        lastParent=curTag

                        gotTag=False
                        gotAtr=False
                        gotTxt=False
                    else:
                        print("parent UP")
                        curTag.parent = lastParent
                        if not lastParent==None:
                            lastParent.inside.append(curTag)
                        
                        gotTag=False
                        gotAtr=False
                        gotTxt=False

            
                    
    thePage = pg
    ShowPage()
    pass
"""

def NumerateString(tstr):
    cnt = 2
    out = "_1_ "+tstr
    i=0
    while i < len(out):
        if out[i]=='\n':
            out = out[:(i+1)]+"_"+str(cnt)+"_ "+out[(i+1):]
            cnt+=1
            i+=1
        else:
            i+=1
            continue
    return out
    

def HowMuchLines(tag):
    if len(tag.inside)==0:
        lines = 1
    else:
        lines = 2
    for i in range(len(tag.inside)):
        lines+=HowMuchLines(tag.inside[i])
    return lines


    


def GenerateFromTag(itag,linesList,theLine):

        curLine = theLine

        tabs = 0
        ptag = itag.parent
        
        while not (ptag==None):
            ptag = ptag.parent
            tabs+=1

        tab = "\t"*tabs

        ostr = tab+"<"+itag.tagName+" "+itag.attributes+">"+itag.text

        linesList[curLine]=itag

        if len(itag.inside)>0:
            ostr=ostr+"\n"
            linesList[curLine+HowMuchLines(itag)-1]=itag

        passedLines = 1
        for tag in itag.inside:
            ostr = ostr+GenerateFromTag(tag,linesList, curLine+passedLines)
            passedLines+=HowMuchLines(tag)
   

        if itag.single:
            ostr = ostr+"\n"
        else:
            if len(itag.inside)>0:
                ostr = ostr+tab+"</"+itag.tagName+"> \n"
            else:
                ostr = ostr+"</"+itag.tagName+"> \n"

        return ostr


def PutNewTag(tag, par, pos,above):
    
    if par==None:
        ErrorPage("!!!Cannot put tag here!!!")
        return False
    if above:
        for i in range(pos, len(par.inside)):
            par.inside[i].localPos+=1
    else:
        for i in range(pos+1, len(par.inside)):
            par.inside[i].localPos+=1
    tag.localPos = pos
    tag.parent=par
    par.inside = par.inside[:pos]+[tag]+par.inside[pos:]
    return True

def RemoveTag(itag, keep):

    if itag.parent==None:
        ErrorPage("!!!Cannot remove the tag!!!")
        return False

    if len(itag.inside)>0:
        if keep:
            le = len(itag.inside)
            for i in range(le):
                PutNewTag(itag.inside[i], itag.parent, itag.localPos+i ,True)
            p = itag.localPos
            itag.parent.inside.pop(p)
            for i in range(p, len(itag.parent.inside)):
                itag.parent.inside[i].localPos-=1
        else:
            p = itag.localPos
            itag.parent.inside.pop(p)
            for i in range(p+1, len(itag.parent.inside)):
                itag.parent.inside[i].localPos-=1
    else:
        p = itag.localPos
        itag.parent.inside.pop(p)
        for i in range(p+1, len(itag.parent.inside)):
            itag.parent.inside[i].localPos-=1


def ShowPage():
    global globalTags
    tags = len(globalTags)
    pageStr = ""
    if tags==0:
        printC("empty page")
        return
    totalLines = HowMuchLines(thePage)
    globalTags = [None]*totalLines
    pageStr = GenerateFromTag(thePage,globalTags,0)
    pageStr = NumerateString(pageStr)
    print(pageStr)
    
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def ErrorPage(err):
    cls()
    print(indent)
    printC(err)
    print(indent)
    input()
    GetToPage(lastPage)

def InstructionsInfo():
    cls()
    print(indent)
    print(instructionLine)
    print(indent)
    input()
    MainMenu()

def MainMenu():
    global lastPage
    lastPage = 0
    cls()
    
    print("xXx_<HTML_Generator>_xXx by "+fatherName)
    print("version "+str(appVer))
    print(indent)
    printC("action list:")
    print("1. Create New Project")
    print("2. Instruction")
    print("3. Exit")
    valid  = GetRangeChoice(1,3,"NO SUCH OPTION")
    
    if   choice==1:
        CreatingProject()
    elif choice==2:
        InstructionsInfo()
    elif choice==3:
        Exiting()
    else:
        MainMenu()


def TextEditor():
    global textE
    cls()
    a = ""
    textE=""
    OneDoll = False
    while True:
        cls()
        print(textE)
        print(indent)
        print(textEditorInfo)
        a = msvcrt.getch()
        if a[0]==224:
            a=''
            continue

        A=a.decode("utf-8")
        if a==b'\x1b':
            break
        if A=='\b':
            textE=textE[0:len(textE)-1]
        elif A=='\r':
            textE+='\n'
        elif a=='\t':
            textE+='\t'
        else:
            textE+=str(A)
   




def PlacingTag(par=None):
    global globalTags
    putLine=0
    if par==None:
        cls()
        ShowPage()
        print(indent)
        printC("Select Line")
        valid = GetRangeChoice(1,len(globalTags),"NO SUCH LINE")
        if not valid:
            return

        putLine = choice-1

    cls()
    ShowPage()
    print(indent)
    printC("Select Tag")
    print(tagList)
    valid = GetRangeChoice(1,tagsAvaible,"NO SUCH TAG")
    if not valid:
        return

    newTag = GetTag(choice)

    if par==None:
        cls()
        ShowPage()
        print(indent)
        printC("1. above     2. under    3.inside")
        print(indent)
        valid = GetRangeChoice(1,3,"NO SUCH OPTION")
        if not valid:
            return

        if choice==3:
            if not isinstance(globalTags[putLine], InsideTag):
                ErrorPage("CANT DO THAT")

        up=True
        addPos=0
        if choice==2:
            up=False
            addPos=1
    

    succ = True

    if par==None:
        if not choice==3:
            succ = PutNewTag(newTag, globalTags[putLine].parent, globalTags[putLine].localPos+addPos,up)
        else:
            succ = PutNewTag(newTag, globalTags[putLine], 0, True)
        if succ:
            Redactor()
    else:
        succ = PutNewTag(newTag, thePage, 0, False)

    if succ:
        Redactor()


def TemplatePlace():
    global globalTags

    cls()
    ShowPage()
    print(indent)
    printC("Select Line")
    valid = GetRangeChoice(1,len(globalTags),"NO SUCH LINE")
    if not valid:
        return

    putLine = choice-1

    cls()
    ShowPage()
    print(indent)
    printC("Select Template")
    print("1. text link")
    print("2. image")
    print("3. button")
    print("4. input-button")

    valid = GetRangeChoice(1,tagsAvaible,"NO SUCH OPTION")
    if not valid:
        return

    newTags = []

    cls()
    ShowPage()
    print(indent)

    if choice==1:
        a = input("text of the link: ")
        b = input("url of the link: ")
        newTags.append(A(a,b))
    elif choice==2:
        a = input("image source: ")
        b = input("width of image in px or %: ")
        c = input("height of imgage in px or %: ")
        newTag=Img(a)
        newTag.attributes = "width="+b+" "+"height="+c+" "
        newTags.append(newTag)
    elif choice==3:
        a = input("button's text: ")
        b = input("button's action: ")
        newTags.append(Button(a,b))
    elif choice==4:
        a = input("placeholder(a hint for user): ")
        b = input("placeholder's id: ")
        c = input("button's text: ")
        d = input("button's action: ")
        newTag1=Input(a)
        newTag1.attributes+="id='"+b+"' "
        newTags.append(newTag1)
        newTags.append(Button(c,d))



    cls()
    ShowPage()
    print(indent)
    printC("1. above     2. under    3. inside")
    print(indent)
    valid = GetRangeChoice(1,3,"NO SUCH OPTION")
    if not valid:
        return

    up=True
    addPos=0
    if choice==2:
        up=False
        addPos=1
    if not choice==3:
        for i in range(len(newTags)):
            succ = PutNewTag(newTags[i], globalTags[putLine].parent, globalTags[putLine].localPos+addPos,up)
    else:
        
        succ = PutNewTag(newTags[0], globalTags[putLine], 0, False)
        for i in range(1,len(newTags)):
            succ = PutNewTag(newTags[i], globalTags[putLine], addPos+i,False)
    if succ:
        Redactor()
    

def ChangingAttribute():
    cls()
    ShowPage()
    print(indent)
    printC("Select Line")
    valid = GetRangeChoice(1,len(globalTags),"NO SUCH LINE")
    if not valid:
        return

    attLine = choice-1
    theTag=globalTags[attLine]

    cls()
    ShowPage()
    print(indent)
    printC("1. Change  2. Add")
    valid = GetRangeChoice(1,2,"NO SUCH OPTION")
    if not valid:
        return

    if choice==1:
        att = input("attributes: ")
        theTag.attributes = att
    if choice==2:
        att = input("addition: ")
        theTag.attributes += att+" "
    Redactor()
        



def ChangingText():
    cls()
    ShowPage()
    print(indent)
    printC("Select Line")
    valid = GetRangeChoice(1,len(globalTags),"NO SUCH LINE")
    if not valid:
        return

    attLine = choice-1
    theTag=globalTags[attLine]

    cls()
    ShowPage()
    print(indent)
    printC("1. Change  2. Add")
    valid = GetRangeChoice(1,2,"NO SUCH OPTION")
    if not valid:
        return

    chad = choice

    cls()
    ShowPage()
    print(indent)
    printC("1. Simple  2. MultiLine ")
    valid = GetRangeChoice(1,2,"NO SUCH OPTION")
    if not valid:
        return

    if choice==1:
        text = input("text: ")
    else:
        TextEditor()
        text = textE

    if chad==1: 
        theTag.text = text
    if chad==2:
        theTag.text += text
    Redactor()




def RemovingTag():
    cls()
    ShowPage()
    print(indent)
    printC("Select Line")
    valid = GetRangeChoice(1,len(globalTags),"NO SUCH LINE")
    if not valid:
        return

    rLine = choice-1
    theTag = globalTags[rLine]

    if len(theTag.inside)>0:
        cls()
        ShowPage()
        print(indent)
        printC("1. Remove child tags    2. Keep child tags")
        valid = GetRangeChoice(1,2,"NO SUCH OPTION")
        if not valid:
            return

        if choice==1:
            RemoveTag(theTag,False)
        else:
            RemoveTag(theTag,True)
    else:
        RemoveTag(theTag,False)

    Redactor()
    pass


def Redactor():
    global lastPage, thePage
    lastPage = 1
    cls()
    print(indent)
    printC("REDACTOR: "+projectName)
    print(indent)
    ShowPage()
    print(indent)
    printC("action list")
    print("1. add tag")
    print("2. change attribute")
    print("3. change text")
    print("4. remove tag")
    print("5. save")
    print("6. exit")
    print(indent)
    valid = GetRangeChoice(1,6,"NO SUCH OPTION")
    
    if not valid:
        return

    if choice==1:
        cls()
        print(indent)
        ShowPage()
        print(indent)
        print("1. manually      2. template")
        valid = GetRangeChoice(1,2,"NO SUCH OPTION")

        if not valid:
            return

        if choice==1:
            if len(thePage.inside)>0:
                PlacingTag()
            else:
                PlacingTag(thePage)
        else:
            TemplatePlace()
    elif choice==2:
        ChangingAttribute()
    elif choice==3:
        ChangingText()
    elif choice==4:
        RemovingTag()
    elif choice==5:
        thePage.GenerateFile(projectName+".html")
        Redactor()
    else:
        thePage=Html([])
        MainMenu()


def CreatingProject():
   global projectName, thePage
   cls()
   print(indent)
   printC("NEW PROJECT")
   print(indent)
   print("1. empty      2. standart")
   valid = GetRangeChoice(1,2,"NO SUCH OPTION")

   if not valid:
       return

   if choice==2:
       thePage = Html([Head([Title("")]),Body([])])
   cls()
   print(indent)
   printC("NEW PROJECT")
   print(indent)
   print("Set the name of the project")
   print(indent)
   projectName = input("Name: ")
   Redactor()

def LoadingProject():
   global lastPage
   lastPage = 0
   cls()
   print(indent)
   printC("LOAD PROJECT")
   print(indent)
   printC(loadWarn)
   print(indent)

   print("on reconstruction")
   print(indent)
   print("Get Back to The Main Menu")
   input()
   MainMenu()




def GoodByeScreen():
    cls()
    print("Good Bye")
    print(indent)

def Exiting():
    cls()
    print("Are you sure you want to Exit ?")
    print(indent)
    print("1. Yes      2. No")
    print(indent)
    GetChoice()
    if choice==1:
        GoodByeScreen()
    else:
        MainMenu()
        

MainMenu()