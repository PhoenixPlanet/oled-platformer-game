from PIL import ImageFont


class PrintManager:
    """
    Print Manager
    """
    
    def __init__(self, gameManager):
        self.currentCursor = [0, 0]
        self.nextLineCursor = [0, 0]
        self.gameManager = gameManager

    def print_text(self, text, fontSize, align=1, font="./fonts/CaviarDreams.ttf", screen=(128, 64), start_y=-1, margin=2):
        """
        print test with PIL library
        
        return y position of the next line
        """

        if start_y == -1:
            start_y = self.nextLineCursor[1]
        elif start_y < -1:
            self.nextLineCursor[1] = self.nextLineCursor[1] - start_y
            start_y = self.nextLineCursor[1]
        
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

        text_y = start_y
        for i, item in enumerate(splitedText):
            # print(splitedText[i])
            if align == 1:
                self.gameManager.draw.text((margin, text_y), item, font=font_data, fill=255)
                
            elif align == 2:
                splited_text_len = font_data.font.getsize(item)[0][0]
                start_x = screen[0] / 2 - splited_text_len / 2
                self.gameManager.draw.text((start_x, text_y), item, font=font_data, fill=255)
            
            elif align == 3:
                splited_text_len = font_data.font.getsize(item)[0][0]
                start_x = screen[0] - splited_text_len
                self.gameManager.draw.text((start_x, text_y), item, font=font_data, fill=255)

            text_y += ascent + descent

        self.nextLineCursor = [margin, text_y]
        self.currentCursor = [start_x + splited_text_len, text_y - ascent - descent]
            
        return text_y

