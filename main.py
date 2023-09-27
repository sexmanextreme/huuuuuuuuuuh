def sex(i):
    what = None
    if i is True:
        what = " med vad?"
    else:
        what = " med antilop"
    
    print("sex" +what)


txt = "me and the birds or cards"


def txt_Extract(txt):
    d = {}
    l = txt.split()
    for x in range(1, len(txt.split())+1):
        for i in range(1, len(txt.split())+1):
            h =l[i]
        d["txt{0}".format(x)] = h
        
    print(d)
      

def gate_Not(ope):
    return not ope

def gate_And():
    pass


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

