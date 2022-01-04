import json
import PyPDF2 as p2
import re
from docx import Document
import time
import os

start_time = time.time()
#def file_parser(inputFileName):
def docx_reader(filename):
        doc_dict={}
        document=Document(filename)
        indx=0
        for para in document.paragraphs:
            indx = indx+1
            if (len(para.text)>0):
                doc_dict =para.text
        return doc_dict

def csv_reader(filename):
        with open(filename,'r') as csv_file:
            text = ' '.join([i for i in csv_file])  
            text = text.replace(",", " ")
            text = text.replace("\n"," ")

        return text

def txt_file_reader(filename):
        f = open(filename, "r")
        text = ' '.join([i for i in f])
        return text

def json_read(filename):
    file = open(filename,'r')
    data = json.load(file)
    file.close()
    return data
    
def parser(text):
    reg_list=[]
    for k in json_read('allregex.json').keys():
        data = json_read('allregex.json')
        regex = data[k]
        reg_list.append("".join(regex))
        
    for reg in reg_list:
        if re.findall(reg,text):
            content=re.findall(reg,text)
            print(content)
    #file_ext=os.path.splitext(inputFileName)[-1].lower()
def final__output(inputFileName):
    file_ext=os.path.splitext(inputFileName)[-1].lower()
    if file_ext == '.pdf':
        pdf_read=p2.PdfFileReader(inputFileName)
        x=pdf_read.getPage(0)
        l=[]
        l.append(x.extractText())
        for w in l:
            content=parser(w)
        print(content)
    elif file_ext == '.csv':
        l=[]
        l.append(csv_reader(inputFileName))
        for elmt in l:
            content = parser(elmt)
        print(content)
    elif file_ext == '.docx':
        new_l=[]
        new_l.append(docx_reader(inputFileName))
        for elmt in new_l:
            content=parser(elmt)
        print(content)
    elif file_ext == '.txt':
        l=[]
        l.append(txt_file_reader(inputFileName))
        for elmt in l:
            content = parser(elmt)
        print(content)
    else:
        print('File type does not supported.....!')


def main():
    inputFileName = input('enter file name.....\n')
    output=final__output(inputFileName)
    return output
if __name__=="__main__":
    main()