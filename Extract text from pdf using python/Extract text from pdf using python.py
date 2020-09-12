import PyPDF2
a=PyPDF2.PdfFileReader('Git Cheat Sheet.pdf')

print(a.documentInfo)
print(a.getNumPages())

str=''
for i in range (1,11):
    str+=a.getPage(2).extractText()

with open("text.txt","w",encoding='utf-8') as f:
    f.write(str)
