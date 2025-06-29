import pyttsx3
from PyPDF2 import PdfReader

book = open('oop.pdf', 'rb')
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()

for num in range(7, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    if text: 
        speaker.say(text)
        speaker.runAndWait()
