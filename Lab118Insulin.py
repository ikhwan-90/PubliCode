
filename = 'preproinsulin-seq.txt'
File = open(filename, 'rt')
text = File.read()
File.close()

#Separate text with list method
insulinSeq = list(text.split())
cleanInsulinLst = []

for x in range(len(insulinSeq)):
    if len(insulinSeq[x]) >= 7:
        cleanInsulinLst.append(insulinSeq[x])
print(cleanInsulinLst)
wordCount = sum(len(words) for words in cleanInsulinLst)
print("Cleaned character(s) amount: " + str(wordCount))

#Convert items in list to single string
insulinStr = ""
for item in cleanInsulinLst[0:20]:
    insulinStr = insulinStr + item
#To check the converted list
#print(insulinStr)
#print(len(insulinStr))

wordShift = 0
char, char2, char3, char4 = "", "", "", ""

#while wordShift < 24:
for ltr in insulinStr:
    char = char + ltr
    wordShift += 1
    if wordShift == 24:
        isInsulin = open("Isinsulin-seq-clean.txt", "w")
        iicount = isInsulin.write(char)
        isInsulin.close()
    elif wordShift == 54:
        char2 = char[24:]
        bInsulin = open("binsulin-seq-clean.txt", "w")
        bicount = bInsulin.write(char2)
        bInsulin.close()
    elif wordShift == 89:
        char3 = char[54:]
        cInsulin = open("cinsulin-seq-clean.txt", "w")
        cicount = cInsulin.write(char3)
        cInsulin.close()
    elif wordShift == 110:
        char4 = char[89:]
        aInsulin = open("ainsulin-seq-clean.txt", "w")
        aicount = aInsulin.write(char4)
        aInsulin.close()


print("Isinsulin-seq-clean.txt character(s) count: " + str(iicount))
print("binsulin-seq-clean.txt character(s) count: " + str(bicount))
print("cinsulin-seq-clean.txt character(s) count: " + str(cicount))
print("ainsulin-seq-clean.txt character(s) count: " + str(aicount))
