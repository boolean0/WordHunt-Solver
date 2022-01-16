import pytesseract

def readImg(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    convertedText = pytesseract.image_to_string(image)
    convertedText = convertedText.strip(); 
    if(len(convertedText) < 16) return [] 
    else{
        grid = []
        for i in range(4):
            curRow = []
            for j in range(4):
                curStringIdx = 4*i + j
                curRow.append(convertedText[curStringIdx])
                grid.append(curRow)
        
        return grid
    }

 
    