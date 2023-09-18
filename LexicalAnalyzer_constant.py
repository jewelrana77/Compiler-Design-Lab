import nltk
import re

f = open('input.txt', 'r')
program = f.read()
count = 0

Keywords_Output = []

Constant_Output = []


def remove_Spaces(program):
    scanned_Program = []
    for line in prog:
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program


def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed



RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Constant = "^(\d+)$"



program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')


scanned_Prog = remove_Spaces(prog)

scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])



scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0


Source_Code=[]
for line in scanned_Program_lines:
        Source_Code.append(line)


display_counter = 0
for line in Source_Code:
    count = count + 1
    if(line.startswith("#include")):
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if(re.findall(RE_Keywords, token)):
            Keywords_Output.append(token)
        elif(re.findall(RE_Constant,token)):
            Constant_Output.append(token)
        


print("There Are ",len(Constant_Output),"Constant:",Constant_Output)
print("\n")