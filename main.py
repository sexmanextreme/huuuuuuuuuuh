def sex(i):
    what = None
    if i is True:
        what = " med vad?"
    else:
        what = " med antilop" 
    print("sex" +what)

s0 = Gate()

txt = "me aNd the birds or NOT cards".casefold()

#splits the string by words and inserts it inside a dictionary
d = {}
tl = len(txt.split())
def txt_Extract(txt):

    l = txt.split()
    for x in range(0,tl):    
        if l[x] == "not":
            d["not{0}".format(x)] = l[x]
        elif l[x] == "or":
            d["or{0}".format(x)] = l[x]
        elif l[x] == "and":
            d["and{0}".format(x)] = l[x]
        else:
            d["txt{0}".format(x)] = l[x]

    print(d)
    for x in d.keys():
        print(x)

def gate_Not(d):
    for x in d.keys():
        print(x)
        
    #pr = txt[txt.index("not"),3]
    
    
    #print(pr)

    

def gate_And():
    pass

def gate_Or():
    pass

#gate_Not(d)
txt_Extract(txt)

"""
i = True

while(True):
    
    sex(i)
    
    if i is True:
        i = False
    else:
        i = True
    
"""

