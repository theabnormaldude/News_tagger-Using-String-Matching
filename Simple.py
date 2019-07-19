# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:55:50 2019

@author: Shiv
"""
import time
import numpy as np
import pandas as pd



'''stream_dict={}
stream_read=pd.read_csv(r"D:/Code/Internship/Stream.csv", sep='delimiter', header=None)
stream_ls=stream_read.values.tolist()
for i in stream_ls:
    print(i)

start_time=time.time()
print(start_time)'''

#OPENING ALL THE REQUIRED TEXT FILES

uni_open=open("University_List.txt")
uni_read=uni_open.readlines()
uni_list=[]
uni_set=set([])
for line in uni_read:
    uni_list.append(line.rstrip())
    
#print(uni_list)

deg_open=open("Degrees.txt")
deg_read=deg_open.readlines()
deg_list=[]
deg_set=set([])
for line_1 in deg_read:
    deg_list.append(line_1.rstrip())
    
#print(deg_list)

exa_open=open("Exams.txt")
exa_read=exa_open.readlines()
exa_list=[]
exa_set=set([])
for line_2 in exa_read:
    exa_list.append(line_2.rstrip())
    
#print(exa_list)

streams_open=open("Streams.txt")
streams_read=streams_open.readlines()
streams_list=[]
streams_set=set([])
for line_3 in streams_read:
    streams_list.append(line_3.rstrip())
    
#print(streams_list)

coll_open=open("Colleges.txt")
coll_read=coll_open.readlines()
coll_list=[]
coll_set=set([])
for line_4 in coll_read:
    coll_list.append(line_4.rstrip())
    
    
#print(coll_list)
    

spec_open=open("Specialization.txt")
spec_read=spec_open.readlines()
spec_list=[]
spec_set=set([])
for line_5 in spec_read:    
    spec_list.append(line_5.rstrip())
    
    
#print(spec_list)



cou_open=open("Courses.txt")
cou_read=cou_open.readlines()
cou_list=[]
cou_set=set([])
for line_6 in cou_read:
    cou_list.append(line_6.rstrip())
    
    
#print(cou_list)
    
from fuzzywuzzy import fuzz   

#READING EACH LINE FROM THE LIST FILE AND COMPARING WITH THE ARTICLE, AND USING FUZZY
news_open=open("TEST_2.txt")
news_read=news_open.readlines()
for keywords in news_read:
    for word in uni_list:
        if fuzz.token_sort_ratio(keywords,word) >=90:
            uni_set.add(word.rstrip())
        if word in keywords:
            #print("UNIVERSITY: ",word)
            uni_set.add(word)
    for word_1 in deg_list:
        if fuzz.token_set_ratio(keywords,word_1) >=90:
            deg_set.add(word_1.rstrip())
        if word_1 in keywords:
            #print("DEGREE: ",word_1)
            deg_set.add(word_1)
    for word_2 in exa_list:
        if fuzz.token_set_ratio(keywords,word_2) >=92:
            exa_set.add(word_2.rstrip())
        if word_2 in keywords:
            #print("EXAMS: ",word_2)
            exa_set.add(word_2)
    for word_3 in streams_list:
        if fuzz.token_sort_ratio(keywords,word_3) >=90:
            streams_set.add(word_3.rstrip())
        if word_3 in keywords:
            #print("STREAM: ",word_3)
            streams_set.add(word_3)
    for word_4 in coll_list:
        if fuzz.token_sort_ratio(keywords,word_4) >=90:
            coll_set.add(word_4.rstrip())
        if word_4 in keywords:
            #print("COLLEGES: ",word_4)
            coll_set.add(word_4)
    for word_5 in spec_list:
        if fuzz.token_sort_ratio(keywords,word_5) >=90:
            spec_set.add(word_5.rstrip())
        if word_5 in keywords:
            spec_set.add(word_5)
            #print(spec_set)
    for word_6 in cou_list:
        if fuzz.token_sort_ratio(keywords,word_6) >=90:
            cou_set.add(word_6.rstrip())
        if word_6 in keywords:
            cou_set.add(word_6)
            #print(cou_set)'''
unq_set=set([])

'''def match(news_open,head,name):
    news_open=open(r"D:/Code/Internship/TEST.txt")
    news_read=news_open.readlines()
    for keywords in news_read:
        for l in head:
            if l.lower() in keywords.lower():
                unq_set.add(name)'''

import requests
from bs4 import BeautifulSoup

#READING H1 and H2 TAGS FROM THE LINK BELOW

page_link="https://www.collegedekho.com/articles/haryana-mbbs-admissions/"
page_response=requests.get(page_link , timeout=5)
page_content=BeautifulSoup(page_response.content, "html.parser")
textContent=[]
head_1=page_content.find_all("h1")
headings=page_content.find_all("h2")
for i in headings:
    textContent.append(i.text)
for j in head_1:
    textContent.append(j.text)
    
#print(textContent)

unq_set=set([])

def match(ls,head,name):
    for a in ls:
        for b in head:
            if b.lower() in a.lower():
                unq_set.add(name)

college_placements=["Campus Placement","Placement Package","Package","Recruitment Drive","Job Offers","Bags package","Placement","Placements Stats","Internship","Summer Placement","Recruiters","Placement Process","Placement Drive","Campus Placement","Highest Package"]
add_process=["Admission Process","Selection Criteria","Admission Process","Admission Begin","Admission Open","Admission <year>","Admission Now Open"]
career=["Career Options","Career Scope","Career as","Career","as a career","career prospects","career in","career path","career journey","pursue a career","career guide","career guidance"]
dates=["Date","Important Date","Important Dates"]
app_form=["Online Application","Application","Application Begin","Application Form","Admit Card","Last date to apply","Date sheet","Date extended","Application Open"]
col_collab=["Research Collaboration","International Collaboration","Collaboration","Academic Collaboration","collaboration in","collaboration with","collaborate for","collaborate to"]
new_course=["New innovative course","Introduces","introduces","plans to introduce","to introduce","likely to introduce","decision to introduce","to introduce","New courses introduce"]
exa_results=["Result","Results Declared","result Declared","Results and Cut-Off","Results Announced","Results Out","Releases Result","Result Available Now","Result Released","Results Expected","Check your results","Results announced","Results declared","Result","Results Annoucement","Results to be announced","Result Declaration","Results delayed","Exam Result","Seat Allotment Result","Result Evaluation Process","Marks Released","Merit List"]
counselling=["Counselling Process","Counselling","Counselling Released","Counselling","Counselling Schedule","Counselling Concluded","Counselling to commence","Counselling for","Counselling on","Counselling to begin","Counselling from","Counselling Dates","Counselling to be conducted","Counselling Procedure","Counselling Session","Counselling starts"]
rank=["Ranking","rank","ranking"]
exa_ans=["Answer key released", "Answers released"]
fee=["Fee","Fees","Revised Fee","Fee Structure"]
cut=["cut-off","cut off","cutoff"]
col_sel=["selection process","selection & counselling process","selection and counselling process","selection process and counselling process","Sekection & Counselling","selection criteria","Selection Details"]
elig=["Eligibility","Eligibility Criteria"]
comp=["vs","versus","VS","v/s"] 
           

        
if uni_set:
    print("UNIVERSITY: ",uni_set)
if deg_set:
    print("DEGREES: ",deg_set)
if exa_set:
    print("EXAMS: ",exa_set)
if streams_set:
    print("STREAMS: ",streams_set)
if coll_set:
    print("COLLEGES: ",coll_set)
if spec_set:
    print("SPECIALIZATION: ",spec_set)
if cou_set:
    print("COURSES: ",cou_set)

match(textContent,college_placements,"PLACEMENT")
match(textContent,add_process,"ADMISSION PROCESS")
match(textContent,career,"CAREER")
match(textContent,dates,"IMPORTANT DATES")
match(textContent,app_form,"APPLICATION FORM")
match(textContent,col_collab,"COLLEGE COLLABORATIONS")
match(textContent,new_course,"NEW COURSES")
match(textContent,exa_results,"EXAM RESULTS")
match(textContent,counselling,"COUNSELLING")
match(textContent,rank,"RANK")
match(textContent,exa_ans,"EXAM ANSWER KEYS")
match(textContent,fee,"FEES")
match(textContent,cut,"CUT OFF")
match(textContent,col_sel,"COLLEGE SELECTION")
match(textContent,elig,"ELIGIBITY CRITERIA")
match(textContent,comp,"COMPARISONS")

print(unq_set)

#TIME TAKEN TO RUN THE CODE
    
print(f"--- {(time.time()-start_time)} seconds ---")
    
"""str_1="B.Sc"
str_2="BSc"
ratio=fuzz.token_sort_ratio(str_1,str_2)
print(ratio)"""
