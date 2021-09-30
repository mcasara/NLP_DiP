#%%
import os
import csv
import mailparser

os.chdir('C:/Users/maxim/Desktop')
listeraw=[]
listeclean=[]
with open('emails.csv', 'r') as f:
    reader = csv.reader(f)
    for i in range(17000):
        listeraw.append(next(reader))


for k in listeraw[1:]:
    listeclean.append((k[1].rstrip().splitlines()))
    while '' in listeclean[-1]:
        listeclean[-1].remove('')
    listeclean[-1]=''.join(listeclean[-1][15:])
    
listeterms=['>>>>>>','daily.pdf','Copyright','Abstracted from','The Wall Street Journal','The Economic Times','Assigned to:','*********','----------------','&nbsp','Forwarded by', 'X-Origin', 'X-bcc','Content-Transfer-Encoding','(See attached file','X-From','X-FileName','X-To:','-Original Message-','Subject:','[IMAGE]','If you cannot read this mail','____________','advertisement','<html','Please click']
listemegaclean=[]
for k in listeclean:
    if not any(x in k for x in listeterms):
        listemegaclean.append([k])



#%% LIST SUBJECT
import os
import csv
import mailparser

os.chdir('C:/Users/maxim/Desktop')
listeraw2=[]
listeclean2=[]
with open('emails.csv', 'r') as f1:
    reader = csv.reader(f1)
    for i in range(17000):
        listeraw2.append(next(reader))

listsubject=[]
for k in listeraw2[1:]:
    mail=mailparser.parse_from_string(k[1])
    listsubject.append(mail.subject)

#%%
listsubjectclean=list(filter(None, listsubject))
listsubjectclean=list(filter(lambda string: string!='Re:', listsubjectclean))
listsubjectcleaner=[]
for k in listsubjectclean:
    listsubjectcleaner.append([((((((((k.replace('Re: ','')).replace('RE:','')).replace('RE: ','').replace('fw:','')).replace('FW:','')).replace('Fw:','')).replace('Fwd:','')).replace('fwd:','')).replace('Fwd :',''))])
    
listsubjectcleaner=list(filter(lambda list: list!=[''], listsubjectcleaner))
print(listsubjectcleaner[:40])
#%%
textmail=listeclean[9]
textmail2=listeraw[10][1]

#%%
!pip install mail-parser
#%%

import mailparser

mail = mailparser.parse_from_string(textmail2)
text3=mail.body
mail2=mailparser.parse_from_string(text3)

#%%
o=0
#%%
print(listeclean[o])
o+=1

#%%

with open('cleanmails.csv', 'w',newline ='') as f: 
    write = csv.writer(f) 
    write.writerows(listemegaclean) 
    
    
#%%

with open('cleanmailsubject.csv', 'w',newline ='') as f: 
    write = csv.writer(f) 
    write.writerows(listsubjectcleaner) 