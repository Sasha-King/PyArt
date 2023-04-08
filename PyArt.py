#!/usr/bin/env python3
'''Assignment 4 Part 3'''
print(__doc__)

import random
from typing import IO

#Class defining a circle according to the SVG format, also includes methods to write a Circle to an html file   
class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        '''Circle __init__'''  
        #Position and radius of circle 
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        
        #Colour settings 
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def __repr__(self):
        '''Circle repr method'''
        C: str = f"Circle cx = {self.cx}, cy = {self.cy}, rad = {self.rad}, colour = ({self.red}, {self.green}, {self.blue}), op = {self.op}"
        return C 
    
    def getcx(self):
        '''Get cx or cir method'''
        return self.cx

    def getcy(self):
        '''Get cy of cir method'''
        return self.cy

    def getrad(self):
        '''Get rad of cir method'''
        return self.rad

    def getColour(self):
        '''Get Colour of cir method'''
        return (self.red, self.green, self.blue, self.op)

    def setcx(self, cx: int):
        '''Circle setcx method'''
        self.cx: int = cx

    def setcy(self, cy: int):
        '''Circle setcy method'''
        self.cy: int = cy

    def setrad(self, rad: int):
        '''Cricle setrad method'''
        self.rad: int = rad

    def setcolour(self, red: int, green: int, blue: int, op: float()):
        '''Circle setColour method'''
        self.red:int = red
        self.green:int = green
        self.blue:int = blue
        self.op:float = op

    # Wrtites the circle in SVG to the given file
    def drawShape(self, filename: IO[str]):
        '''Draw circle method'''
        indent: str = "   "
        cir: str =  f'{indent*2}<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>\n'
        filename.write(cir)

    #Formats the data to be printed as a table (generates additional numbers for attriubtes not in shape)
    def tableformat(self):
        col: tuple() = self.getColour()
        rXY = GenRandom().genellipse()
        WH = GenRandom().genrectangle()
        TF: str = f"{0:^3} {self.getcx():<3} {self.getcy():<3} {self.getrad():<3} {rXY[0]:<3} {rXY[1]:<3} {WH[0]:^3} {WH[1]:^3} {col[0]:^3} {col[1]:^3} {col[2]:^3} {col[3]:<3}"
        return TF

#Class defining a rectangle to the SVG format also includes methods to write the rectangle to an html file 
class Rectangle:
    '''Rectangle class'''
    def __init__(self, Pos:tuple, rec: tuple, col: tuple):
        '''Rectangle __init__'''
         #Positional settings
        self.x: int = Pos[0]
        self.y: int = Pos[1]
        
        #Dimensions of rectangle 
        self.width: int = rec[0]
        self.height: int = rec[1]
        
        #Colour settings
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def __repr__(self):
        '''Rectangle repr method'''
        R: str = f"Rectangle x = {self.x}, y = {self.y},  width = {self.width}, height = {self.height}, colour = ({self.red}, {self.green}, {self.blue}), op = {self.op}"
        return R

    def getwidth(self):
        '''Get width of rec method'''
        return self.width
    
    def getheight(self):
        '''Get height of rec method'''
        return self.height

    def getx(self):
        '''Get x of rec method'''
        return self.x

    def gety(self):
        '''Get y of rec method'''
        return self.y

    def getColour(self):
        '''Get Colour of rec method'''
        return  (self.red, self.green, self.blue, self.op)

    def setwidth(self, width: int):
        '''Rec setwidth method'''
        self.width:int = width

    def setheight(self, height: int):
        '''Rec setheight method'''
        self.height:int = height

    def setx(self,x: int):
        '''Rec setx method'''
        self.x:int = x
    
    def sety(self,y: int):
        '''Rec sety method'''
        self.y:int = y

    def setcolour(self, red: int, green: int, blue: int, op: float()):
        '''Rec setColour method'''
        self.red:int = red
        self.green:int = green
        self.blue:int = blue
        self.op:float = op

    #Writes the rectangle in SVG to the given file 
    def drawShape(self, filename: IO[str]):
        '''Draw rec method'''
        indent: str = "   "
        rec: str =  f'{indent*2}<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>\n'
        filename.write(rec)

    #Formats the data to be printed as a table (generates additional numbers for attriubtes not in shape)
    def tableformat(self):
        '''Rectangle tableformat method'''
        col: tuple() = self.getColour()
        rXY: tuple = GenRandom().genellipse()
        TF: str = (f"{1:^3} {self.getx():<3} {self.gety():<3} {GenRandom().gencirrad():<3} {rXY[0]:<3} {rXY[1]:<3} {self.getwidth():<3} {self.getheight():<3} {col[0]:^3} {col[1]:^3} {col[2]:^3} {col[3]:<3}")  
        return TF  

#Clas define a Ellipse according to the SVG format, contatins methods to write the circle to an html file 
class Ellipse:
    '''Ellipse class'''
    def __init__(self, Pos:tuple, Ell: tuple,  col: tuple):
        '''Ellipse init'''
        # Position in x and y 
        self.cx: int = Pos[0]
        self.cy: int = Pos[1]
        
        # Radius
        self.rx: int = Ell[0]
        self.ry: int = Ell[1]

        # Colour
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def __repr__(self):
        '''Rectangle repr method'''
        E: str = f"Ellipse cx = {self.cx}, cy = {self.cy},  rx = {self.rx}, ry = {self.ry}, colour = ({self.red}, {self.green}, {self.blue}), op = {self.op}"
        return E
    
    def getcx(self):
        '''Ellipseipse getcx method'''
        return self.cx

    def getcy(self):
        '''Ellipse getcy method'''
        return self.cy

    def getrx(self):
        '''Ellipse getrx method'''
        return self.rx

    def getry(self):
        '''Ellipse getry method'''
        return self.ry

    def setcx(self, cx: int):
        '''Ellipse setcx method'''
        self.cx: int = cx

    def setcy(self, cy: int):
        '''Ellipse setcy method'''
        self.cy: int = cy

    def setrx(self, rx: int):
        '''Ellipse setrx method'''
        self.rx: int = rx

    def setry(self, ry: int):
        '''Ellipse setry method'''
        self.ry: int = ry

    def getColour(self):
        '''Get Colour of Ellipse method'''
        return (self.red, self.green, self.blue, self.op)
    
    def setcolour(self, red: int, green: int, blue: int, op: float()):
        '''Ellipse setColour method'''
        self.red:int = red
        self.green:int = green
        self.blue:int = blue
        self.op:float = op

    # Wrtites the ellipse in SVG to the given file
    def drawShape(self, filename: IO[str]):
        '''Draw Ellipse method'''
        indent: str = "   "
        Ell: str = f'{indent*2}<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></ellipse>\n'
        filename.write(Ell)

    #Formats the data to be printed as a table (generates additional numbers for attriubtes not in shape)
    def tableformat(self) -> str:
        '''Ellipse table format method'''
        col: tuple = self.getColour()
        WH: tuple = GenRandom().genrectangle()
        TF: str =  f"{2:^3} {self.getcx():<3} {self.getcy():<3} {GenRandom().gencirrad():<3} {self.getrx():<3} {self.getry():<3} {WH[0]:^3} {WH[1]:^3} {col[0]:^3} {col[1]:^3} {col[2]:^3} {col[3]:<3}" 
        return TF

#Class to determine an write to a file the Prolouge and epligouge of an HTML file aswell as define an SVG canvas    
class ProEpilogue: 
    '''ProEpilogue class'''
    def __init__(self, filename: IO[str], title: str, comment: str, svgdimensions: tuple):
        '''ProEpilouge init'''
        self.filename: IO[str] = filename
        self.title: str = title
        self.comment: str = comment
        self.svgdimensions: tuple = svgdimensions

    def PrintPrologue(self):
        '''PrintProlouge method'''
        indent: str = "   "
        htmlpro: str = f"<html>\n<head>\n{indent}<title>{self.title}</title>\n</head>\n<body>\n"
        comment: str = f'{indent}<!--{self.comment}-->\n'
        svgbox: str = f'{indent}<svg width="{self.svgdimensions[0]}" height="{self.svgdimensions[1]}">\n'
        self.filename.write(htmlpro + comment + svgbox)

    #SVG canvas body html and closes file 
    def PrintEpilouge(self):
        '''PrintEpilouge method'''
        indent: str = "   "
        self.filename.write(f"{indent}</svg>\n</body>\n</html>\n")

#Generates random numbers within certain ranges
class GenRandom:
    '''GenRandom class'''

    def __init__(self):
        '''GenRandom init'''
        
    #Decides the shape
    def genshape(self):
        '''GenRandom genshape method'''
        return random.randint(0,2)
    
    def gencirrad(self):
        '''GenRandom gencirrad method'''
        return random.randint(0, 100)

    def genxy(self, SVGcanvas: tuple):
        '''GenRandom genxy method'''
        xy: tuple = (random.randint(0, SVGcanvas[0]), random.randint(0, SVGcanvas[1]))
        return xy
        
    def genellipse(self):
        '''GenRandom gen ellipse method'''
        cxandcy: tuple = (random.randint(10, 30), random.randint(10, 30))
        return cxandcy

    def genrectangle(self):
        '''Genrandom rectangle method'''
        rec: tuple = (random.randint(10, 100), random.randint(10, 100))
        return rec 

    def gencolour(self):
        '''GenRandom gencolour method'''
        colour: tuple = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255), round(random.uniform(0,1.0), 1))
        return colour

#Generate random art within the given SVG canvas, Inherits methods from GenRandom  
class ArtConfig(GenRandom):
    '''ArtConfig class'''
    def __init__(self, SVGcanvas: tuple):
        '''ArtConfig innit'''
        self.SVGx = SVGcanvas[0]
        self.SVGy = SVGcanvas[1]
    
    def getcanvas(self):
        '''ArtConfig get canvas method'''
        return (self.SVGx, self.SVGy)

    def setcanvas(self, SVGx: int, SVGy: int):
        '''ArtConfig set canvas method'''
        self.SVGx = SVGx
        self.SVGy = SVGy

    def configshape(self):
        shape: int = self.genshape()
        xy: tuple = self.genxy((self.SVGx, self.SVGy))
        Col: tuple = GenRandom().gencolour()
        #shape is circle Circle((50,50,50), (255,0,0,1.0))
        if(shape == 0):
            c: Circle= Circle((xy[0], xy[1],GenRandom().gencirrad()), Col)
            return c
        
        #shape is rec Rectangle((50, 100), (50, 200), (0,0,255,1.0))
        if(shape == 1):
            r: Rectangle = Rectangle(xy, GenRandom().genrectangle(), Col)
            return r

        #shape is ellipse Ellipse((450, 250), (25, 50), (100,100,155,1.0))
        if(shape == 2):
            e: Ellipse = Ellipse(xy, GenRandom().genellipse(), Col)
            return e



def createArt(amountArt: int, fnam: str, title: str, svgdimensions: tuple):
    '''Create art method'''
    
    #Creating artconfig 
    comment: str = "Define SVG drawing box"
    Art = ArtConfig(svgdimensions)
     
    #Creates a list of random art 
    AlltheArt = []
    for shape in range(amountArt):
        AlltheArt.append(Art.configshape())
    
    #Opens file and writes the Prolouge to the file 
    f: IO[str] = open(fnam, "w")
    PE = ProEpilogue(f, title, comment, svgdimensions)
    PE.PrintPrologue()
    
    #Writes the random shapes to the html file 
    for shape in AlltheArt:
        shape.drawShape(f)
    PE.PrintEpilouge()
    f.close()
        
def main():
    '''Main method'''
    createArt(10000, "a43.html", "a43 art", (1920,1080))
    

if __name__ == '__main__':
    main()
