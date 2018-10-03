import os
import time
start_time = time.time()
import pyautogui
from pprint import pprint
from lib.google_search_results import GoogleSearchResults                                                                                           #Test Location Question

#creates screen images
pic = pyautogui.screenshot(region=(1178,123,300,40))
pic.save('Question.png')

pic = pyautogui.screenshot(region=(1178,440,300,40))
pic.save('Answer.png')

#outputs readimage to textfile
os.system("cd C:\\Users\\alber\\Tesseract-OCR & tesseract C:\\Users\\alber\\Downloads\\Botting\\Question.png C:\\Users\\alber\\Downloads\\Botting\\question")
os.system("cd C:\\Users\\alber\\Tesseract-OCR & tesseract C:\\Users\\alber\\Downloads\\Botting\\Answer.png C:\\Users\\alber\\Downloads\\Botting\\answers")
with open('question.txt','r') as fileq:
    qtext=fileq.read()
    print(qtext)
with open('answers.txt','r')as filea:
    atext=filea.read()
    print(atext)


stopwords = ['what','who','when','where','is','a','at','is','which','the','of','these','this']                                                      #Test Location Answer                                
querywords = qtext.split()

resultwords  = [word for word in querywords if word.lower() not in stopwords]
qtext = ' '.join(resultwords)
print(qtext)
#print(qtext)
#print(atext)
answerlist=atext.split('\n')
answerlist = list(filter(None, answerlist))
#print(answerlist)
num=50
answerscore=[0,0,0]

query = GoogleSearchResults({"q":qtext+answerlist[2],"num":num})
json_results = query.get_json()
#pprint(json_results)
for i in range(1,num-1):
    snippet=json_results['organic_results'][i]['snippet']
    print(snippet)
    print('\n')
    for j in range(1,3):
        if answerlist[j].lower() in snippet.lower():
            answerscore[j]=answerscore[j]+1
print(answerscore)


print(time.time()-start_time)

    
    
