import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open a file dialog to select the PDF file
book = askopenfilename()

# Create a PDF reader object
pdfreader = PyPDF2.PdfReader(book)

# Get the number of pages in the PDF
num_pages = len(pdfreader.pages)

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Loop through all the pages in the PDF
for num in range(num_pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player.say(text)

# Run and wait for the TTS engine to complete speaking
player.runAndWait()
