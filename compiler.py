from treelib import *
equation = "x = 5 * y + 2 * t"
main_list = equation.split()

print ("----------Lexer----------")
#Lexical Analyzer
operators = ['=' , '+' , '-' , '*', '/' , '%']
alphabet = list ()
number = list ()
lex = list ()
i = 1
for item in equation :
    if item.isalpha() :
        item = "id" + str(i)
        lex.append(item)
        alphabet.append(item)
        i+=1
    if item.isnumeric() :
        lex.append(item)
        number.append(item)
    if item in operators :
        lex.append(item)
print (*lex)

id1=int ()
id2=int ()
id3=int ()

print ("----------Parser----------")
#Parsing Tree
tree1 = Tree()

tree1.create_node("=" , "equal1")
tree1.create_node("id1" , "id1" , parent="equal1" )
tree1.create_node("+", "plus1" , parent="equal1")
tree1.create_node("*","cross1",parent="plus1")
tree1.create_node("id2","id2",parent="cross1")
tree1.create_node("int(5)" , "num1" , parent="cross1")
tree1.create_node("*" , "cross2" , parent="plus1")
tree1.create_node("id3" , "id3" , parent="cross2" )
tree1.create_node("int(2)", "num2" , parent="cross2")

tree1.show()

print ("----------Semantic Analyser----------")
tree2 = Tree()
tree2.create_node("=" , "equal1")
tree2.create_node("id1" , "id1" , parent="equal1" )
tree2.create_node("+", "plus1" , parent="equal1")
tree2.create_node("*","cross1",parent="plus1")
tree2.create_node("inttoreal" , "int1" , parent="cross1")
tree2.create_node("id2" , "id2" , parent="cross1")
tree2.create_node("5.0","num1",parent="int1")
tree2.create_node("*" , "cross2" , parent="plus1")
tree2.create_node("inttoreal" , "int2" , parent="cross2")
tree2.create_node("id3", "id3" , parent="cross2")
tree2.create_node("2.0" , "num2" , parent="int2" )

tree2.show()

print ("----------Intermediate Code Generator----------")
def inttoreal(x) :
    v = float(x)
    return v

temp1 = inttoreal(2)
temp2 = id3 * temp1
temp3 = inttoreal(5)
temp4 = id2 * temp3
temp5 = temp2 + temp4
id1 = temp5

print ('''
temp1 = inttoreal(2)
temp2 = id3 * temp1
temp3 = inttoreal(5)
temp4 = id2 * temp3
temp5 = temp2 + temp4
id1 = temp5
''')

print ("----------Intermediate Code Simplifier----------")
temp2 = id3 * 2.0
temp4 = id2 * 5.0
id1 = temp2 + temp4

print ('''
temp2 = id3 * 2.0
temp4 = id2 * 5.0
id1 = temp2 + temp4
''')

print ("----------Final Code Generator----------")

r = float ()
s = float ()
q = float ()
def ADD (m,n) :
    m = m + n
    return m
def MULT (m,n) :
    m = m * n
    return m
def MOVE (m , n) :
    m = n
    return m


MULT (id3 , 2.0)
MOVE (r , id3)
MULT (id2 , 5.0)
MOVE (s , id2)
ADD (id2 , id3)
MOVE (q , id2)

print ('''
MULT (id3 , 2.0)
MOVE (r , id3)
MULT (id2 , 5.0)
MOVE (s , id2)
ADD (id2 , id3)
MOVE (q , id2)
''')
print ("Waiting for Assembler to proceed ...")
print ("PROGRAM COMPILATION SUCEEDED !")
