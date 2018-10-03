# TessOCRScript
Python-based code for utilizing the Tesseract-OCR to read images. 

Current version for bot.py reads an image of certain dimensions on a screen. The script was developed for the app HQ Trivia to search questions and answers for an approximate answer.

1. To use, set the dimensions of the screenshot to personal requirements based on screen size for the library pyautogui. 
2. Using os, run the tesseract software along with the two newly saved images to create a text file. 
3. The text file will be google searched and using checks with certain keywords, the best approximate answer is determined. 
