def sex(i):
    what = None
    if i is True:
        what = " med vad?"
    else:
        what = " med antilop" 
    print("sex" +what)


txt = "me and the birds or not cards"

#splits the string by words and inserts it inside a dictionary
d = {}
tl = len(txt.split())
def txt_Extract(txt):

    l = txt.split()
    for x in range(0,tl):    
        d["txt{0}".format(x)] = l[x]

    print(d)


def gate_Not(d):
    pr = txt.index("not")
    print(pr)

    

def gate_And():
    pass

def gate_Or():
    pass

gate_Not(d)
#txt_Extract(txt)

"""
i = True

while(True):
    
    sex(i)
    
    if i is True:
        i = False
    else:
        i = True
    
"""

