


class Tag:
    def __init__(self):
        self.tagName = "tagName"
        self.text = ""
        self.attributes = ""
        self.inside = []
        self.single = True
        self.parent = None
        self.localPos = -1

    def GenerateString(self,tabs):

        tab = "\t"*tabs

        outString = tab+"<"+self.tagName+" "+self.attributes+">"+self.text
        if len(self.inside)>0:
            outString=outString+"\n"

        for tag in self.inside:
            outString = outString+tag.GenerateString(tabs+1)
   
        if self.single:
            outString = outString+"\n"
        else:
            if len(self.inside)>0:
                outString = outString+tab+"</"+self.tagName+"> \n"
            else:
                outString = outString+"</"+self.tagName+"> \n"

        return outString

    def GenerateFile(self, path):
        file = open(path, "w")
        file.write(self.GenerateString(0))
        file.close

    pass
#--------------------------------------------------------

class Img(Tag):
    def __init__(self, imagePath, attr=""):
        Tag.__init__(self)
        self.tagName = "img"
        self.attributes = "src='"+imagePath+"' "+attr
        self.single = True
    

class Br(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.tagName = "br"
        self.single = True

class Script(Tag):
    def __init__(self, text):
        Tag.__init__(self)
        self.tagName = "script"
        self.text = text
        self.attributes="type='text/javascript'"
        self.single = False
    

class Style(Tag):
    def __init__(self, text):
        Tag.__init__(self)
        self.tagName = "style"
        self.text = text
        self.attributes="type='text/css'"
        self.single = False


class P(Tag):
    def __init__(self,text,atr=""):
        Tag.__init__(self)
        self.tagName = "p"
        self.text = text
        self.attributes = atr
        self.single=False

class A(Tag):
    def __init__(self,text,atr=""):
        Tag.__init__(self)
        self.tagName = "a"
        self.text = text
        self.attributes = atr
        self.single=False

class H(Tag):
    def __init__(self,size,text,atr=""):
        Tag.__init__(self)
        if size<1:
            size=1
        if size>6:
            size=6
        self.tagName = "h"+str(size)
        self.text = text
        self.attributes = atr
        self.single=False
    
class Button(Tag):
    def __init__(self,text,atr):
        Tag.__init__(self)
        self.tagName = "button"
        self.text = text
        self.attributes = atr
        self.single=False

class Input(Tag):
    def __init__(self,placeholder=""):
        Tag.__init__(self)
        self.tagName = "input"
        self.attributes = "placeholder='"+placeholder+"' "
        self.single=True

class Meta(Tag):
    def __init__(self,atr):
        self.tagName = "meta"
        Tag.__init__(self)
        self.single = True
        self.attributes = atr

class Link(Tag):
    def __init__(self, text, link):
        Tag.__init__(self)
        self.tagName = "a"
        self.text = text
        self.attributes = "href='"+link+"'"
        self.single=False

class Title(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.tagName = "title"
        self.text = text
        self.single=False
    

class InsideTag(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.inside = data
        self.single = False
        for i in range(len(self.inside)):
            self.inside[i].parent = self
            self.inside[i].localPos = i
    pass

class Html(InsideTag):
    def __init__(self, data):
        InsideTag.__init__(self,data)
        self.tagName = "html"
    

class Div(InsideTag):
    def __init__(self, data, attr=""):
        InsideTag.__init__(self,data)
        self.tagName = "div"
        self.attributes = attr

class Head(InsideTag):
    def __init__(self, data):
        InsideTag.__init__(self,data)
        self.tagName = "head"
       
    

class Body(InsideTag):
    def __init__(self, data,attr=""):
        InsideTag.__init__(self,data)
        self.tagName = "body"
        self.attributes=attr
   



examplePage = Html([

        Head([
                Title("Most incredible page"),
                Meta("charset='utf-8'")
            ]),
        Style(".info{font-size:160%; font-family:comic sans ms; color:white; text-align:center}"),
        Body([
                Div([
                    Div([
                            Img("https://pa1.narvii.com/7602/069f9aa24527d326b9987b4efa11abacbcf50200r1-480-384_128.gif","style='width:20%; height:80%'"),
                            A("WELL ", "style=' font-size:180%; font-family:fantasy; color:white'"),
                            Img("https://sun9-8.userapi.com/impf/pZ8KhmmiETJNf4bHtAPYdUke_f5qgY4ahCQeAg/EYvdPbN0rxQ.jpg?size=756x484&quality=96&proxy=1&sign=f885aad1f633bba5dfaab18600e37908&type=album","style='width:50%;'"),
                            A(" COME","style='font-size:180%; font-family:fantasy; color:white'"),
                            Img("https://pa1.narvii.com/7602/069f9aa24527d326b9987b4efa11abacbcf50200r1-480-384_128.gif","style='width:20%; height:80%'"),
                        ],"style='margin-left:0%;'"),
                        A("to my site", "style='font-size:180%; font-family:fantasy; color:white; margin-left:45%'")
                    ]),
                Div([
                        Div([
                            P("Обо мне","class='info'"),
                            P("Назиров Захар:","class='info'"),
                            P("3431101/00001","class='info'")
                        ],"class='info' style='white-space: nowrap'")
                    ])
            ],"bgcolor='black'")
    ])

examplePage.GenerateFile("exell.html")