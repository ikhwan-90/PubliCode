import re #regex function to clean text

filename = 'preproinsulin-seq.txt'
File = open(filename, 'rt')
text = File.read()
File.close()

cleanInsulinLst = re.findall(r'\w{10}', text)                   #regex function - find all alphanumeric with 10 characters
print(cleanInsulinLst)
wordCount = sum(len(words) for words in cleanInsulinLst)
print("Cleaned character(s) amount: " + str(wordCount))

#Convert items in list to single string
insulinStr = ""
for item in cleanInsulinLst[0:20]:
    insulinStr = insulinStr + item

wordShift = 0
char, char2, char3, char4 = "", "", "", ""

for ltr in insulinStr:
    char = char + ltr
    wordShift += 1
    if wordShift == 24:
        isInsulin = open("Isinsulin-seq-clean.txt", "w")
        iicount = isInsulin.write(char)
        isInsulin.close()
    elif wordShift == 54:
        char2 = char[24:]                                           #Slice word from to select only from 24 onwards
        bInsulin = open("binsulin-seq-clean.txt", "w")
        bicount = bInsulin.write(char2)
        bInsulin.close()
    elif wordShift == 89:
        char3 = char[54:]                                           #Slice word from to select only from 54 onwards
        cInsulin = open("cinsulin-seq-clean.txt", "w")
        cicount = cInsulin.write(char3)
        cInsulin.close()
    elif wordShift == 110:
        char4 = char[89:]                                           #Slice word from to select only from 89 onwards
        aInsulin = open("ainsulin-seq-clean.txt", "w")
        aicount = aInsulin.write(char4)
        aInsulin.close()

print("Isinsulin-seq-clean.txt character(s) count: " + str(iicount))
print("binsulin-seq-clean.txt character(s) count: " + str(bicount))
print("cinsulin-seq-clean.txt character(s) count: " + str(cicount))
print("ainsulin-seq-clean.txt character(s) count: " + str(aicount))
