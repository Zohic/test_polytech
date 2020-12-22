


class Tag:
    def __init__(self):
        self.tagStr = "tagName"
        self.innerHTML = ""
        self.attributes = ""
        self.container = []
        self.single = True
        self.parent = None
        self.localPos = -1
        self.begin = -1
        self.end = -1

    def Generate(self):
        tabs = -1
        ptag = self.parent
        while not (ptag==None):
            ptag = ptag.parent
            tabs+=1
        tab = "\t"*tabs

        ostr = tab+"<"+self.tagStr+" "+self.attributes+">"+self.innerHTML
        if len(self.container)>0:
            ostr=ostr+"\n"

        for tag in self.container:
            ostr = ostr+tag.Generate()
   
        if self.single:
            ostr = ostr+"\n"
        else:
            if len(self.container)>0:
                ostr = ostr+tab+"</"+self.tagStr+"> \n"
            else:
                ostr = ostr+"</"+self.tagStr+"> \n"

        return ostr

    def GenerateFile(self, path):
        file = open(path, "w")
        file.write(self.Generate())
        file.close

    pass
#--------------------------------------------------------

class Img(Tag):
    def __init__(self, imagePath, attr=""):
        Tag.__init__(self)
        self.tagStr = "img"
        self.attributes = "src='"+imagePath+"' "+attr
        self.single = True
    

class Br(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.tagStr = "br"
        self.single = True

class Script(Tag):
    def __init__(self, text):
        Tag.__init__(self)
        self.tagStr = "script"
        self.innerHTML = text
        self.attributes="type='text/javascript'"
        self.single = False
    

class Style(Tag):
    def __init__(self, text):
        Tag.__init__(self)
        self.tagStr = "style"
        self.innerHTML = text
        self.attributes="type='text/css'"
        self.single = False


class tagP(Tag):
    def __init__(self,text,atr=""):
        Tag.__init__(self)
        self.tagStr = "p"
        self.innerHTML = text
        self.attributes = atr
        self.single=False

class tagA(Tag):
    def __init__(self,text,atr=""):
        Tag.__init__(self)
        self.tagStr = "a"
        self.innerHTML = text
        self.attributes = atr
        self.single=False

class tagH(Tag):
    def __init__(self,size,text,atr=""):
        Tag.__init__(self)
        if size<1:
            size=1
        if size>6:
            size=6
        self.tagStr = "h"+str(size)
        self.innerHTML = text
        self.attributes = atr
        self.single=False
    
class Button(Tag):
    def __init__(self,text,atr):
        Tag.__init__(self)
        self.tagStr = "button"
        self.innerHTML = text
        self.attributes = atr
        self.single=False

class Input(Tag):
    def __init__(self,placeholder=""):
        Tag.__init__(self)
        self.tagStr = "input"
        self.attributes = "placeholder='"+placeholder+"' "
        self.single=True

class Meta(Tag):
    def __init__(self,atr):
        self.tagStr = "meta"
        Tag.__init__(self)
        self.single = True
        self.attributes = atr

class Link(Tag):
    def __init__(self, text, link):
        Tag.__init__(self)
        self.tagStr = "a"
        self.innerHTML = text
        self.attributes = "href='"+link+"'"
        self.single=False

class Title(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.tagStr = "title"
        self.innerHTML = text
        self.single=False
    

class ContainerTag(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.container = data
        self.single = False
        for i in range(len(self.container)):
            self.container[i].parent = self
            self.container[i].localPos = i
    pass

class Html(ContainerTag):
    def __init__(self, data):
        ContainerTag.__init__(self,data)
        self.tagStr = "html"
    

class Div(ContainerTag):
    def __init__(self, data, attr=""):
        ContainerTag.__init__(self,data)
        self.tagStr = "div"
        self.attributes = attr

class Head(ContainerTag):
    def __init__(self, data):
        ContainerTag.__init__(self,data)
        self.tagStr = "head"
       
    

class Body(ContainerTag):
    def __init__(self, data,attr=""):
        ContainerTag.__init__(self,data)
        self.tagStr = "body"
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
                            tagA("WELL ", "style=' font-size:180%; font-family:fantasy; color:white'"),
                            Img("https://sun9-8.userapi.com/impf/pZ8KhmmiETJNf4bHtAPYdUke_f5qgY4ahCQeAg/EYvdPbN0rxQ.jpg?size=756x484&quality=96&proxy=1&sign=f885aad1f633bba5dfaab18600e37908&type=album","style='width:50%;'"),
                            tagA(" COME","style='font-size:180%; font-family:fantasy; color:white'"),
                            Img("https://pa1.narvii.com/7602/069f9aa24527d326b9987b4efa11abacbcf50200r1-480-384_128.gif","style='width:20%; height:80%'"),
                        ],"style='margin-left:0%;'"),
                        tagA("to my site", "style='font-size:180%; font-family:fantasy; color:white; margin-left:45%'")
                    ]),
                Div([
                        Div([
                            tagP("Обо мне","class='info'"),
                            tagP("Назиров Захар:","class='info'"),
                            tagP("3431101/00001","class='info'")
                        ],"class='info' style='white-space: nowrap'")
                    ])
            ],"bgcolor='black'")
    ])

examplePage.GenerateFile("out.html")