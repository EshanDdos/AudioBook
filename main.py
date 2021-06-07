#To listen a text
#first type command in terminal as pip install pyttsx3
#code:
'''import pyttsx3
speaker = pyttsx3.init()
speaker.say('Hello, How are you')
speaker.runAndWait()'''
#To listen from a pdf
#Type command in terminal as pip install PyPDF2
#CODE:
'''import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
speaker.say('Hello, How are you')
speaker.runAndWait()'''
#To read a specific page in a pdf book
'''import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()'''
#To read a full pdf
#code

import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(1)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
