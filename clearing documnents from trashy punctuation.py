from bs4 import BeautifulSoup
import string,pandas,textwrap
import pyautogui
def striping(word):
    list=["\n",*",","#",',',"-","*"]
    number=0
    for _ in list:
        word=word.strip(_)
    return word        
def read(location):
    
    with open(location,"r+") as file_conent:
         return file_conent.readlines()
with open("my uncle's, Ali, resumes  (2).doc","r+") as file:
    lines=file.readlines()
    # lines=pandas.array(file)
    for line in lines:
        with open("clean_file.doc","+a") as clean_file:
            for word in line:
                word=striping(word)
                clean_file.write(word)
            clean_file.write("\n")