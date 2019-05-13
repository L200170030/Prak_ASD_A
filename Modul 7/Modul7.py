# Dicky Febrian Yusanto
# L200170030
# Kelas A

#--------------------------------------- NOMER 1 ------------------------------#
import re
f = open('Indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
p=r'me\w+'
string = re.findall(p,teks)
print(string)

#--------------------------------------- NOMER 2 ------------------------------#
import re
f = open('Indonesia.txt','r', encoding='latin1')
teks2 = f.read()
f.close()
pola2 = r"di\w+"
tampilan2 = re.findall(pola2,teks2)
print(tampilan2)

#--------------------------------------- NOMER 3 ------------------------------#
import re
f = open('Indonesia.txt','r', encoding='latin1')
teks3 = f.read()
f.close()
pola3 = r"di \w+"
tampilan3 = re.findall(pola3,teks3)
print(tampilan3)

#--------------------------------------- NOMER 4 ------------------------------#
#a
import re
f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
p4=r'([\w+]+)</a></td>'
string=re.findall(p4,teks4)
print(string)

#b
f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)

