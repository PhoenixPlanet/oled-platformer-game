from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class PrintManager:
    def __init__(self, gameManager):
        self.currentCursor = [0, 0]
        self.nextLineCursor = [0, 0]
        self.gameManager = gameManager

    def printText(self, text, fontSize, align=1, font="./fonts/CaviarDreams.ttf", screen=(128, 64), startY=-1, margin=2):
        """
        print test with PIL library
        
        return y position of the next line
        """

        if startY == -1:
            startY = self.nextLineCursor[1]
        elif startY < -1:
            self.nextLineCursor[1] = self.nextLineCursor[1] - startY
            startY = self.nextLineCursor[1]
        
        font_data = ImageFont.truetype(font, fontSize)
        
        ascent, descent = font_data.getmetrics()
        (width, baseline), (offset_x, offset_y) = font_data.font.getsize(text)
        height = ascent
        
        splitedText = []

        if width > screen[0]:
            lineNum = int(width / screen[0]) + 1
            textLen = len(text)
            
            splitNum = 0
            splitStart = 0
            for i in range(lineNum):
                if i != lineNum - 1:
                    while font_data.font.getsize(text[splitStart:splitNum])[0][0] < (screen[0] - margin * 2):
                        print(text[splitStart:splitNum])
                        #print(font_data.font.getsize(text[splitStart:splitNum])[-1][0])
                        # print("base"+str(screen[0] - margin * 2))
                        splitNum += 1
                    splitedText.append(text[splitStart:splitNum-1])
                    splitStart = splitNum - 1

                else:
                    splitedText.append(text[splitStart:])
                    
                    if splitedText[i][0] == ' ':
                        splitedText[i] = splitedText[i][1:]
                    if splitedText[i][-1] == '\n':
                        splitedText[i] = splitedText[i][0:-1]
        else:
            splitedText.append(text)

        textY = startY
        for i in range(len(splitedText)):
            # print(splitedText[i])
            if align == 1:
                self.gameManager.draw.text((margin, textY), splitedText[i], font=font_data, fill=255)
                
            elif align == 2:
                splitedTextLen = font_data.font.getsize(splitedText[i])[0][0]
                startX = screen[0] / 2 - splitedTextLen / 2
                self.gameManager.draw.text((startX, textY), splitedText[i], font=font_data, fill=255)
            
            elif align == 3:
                splitedTextLen = font_data.font.getsize(splitedText[i])[0][0]
                startX = screen[0] - splitedTextLen
                self.gameManager.draw.text((startX, textY), splitedText[i], font=font_data, fill=255)

            textY += ascent + descent

        self.nextLineCursor = [margin, textY]
        self.currentCursor = [startX + splitedTextLen, textY - ascent - descent]
            
        return textY

