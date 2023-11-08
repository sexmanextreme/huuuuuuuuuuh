#from Gate import Gate


def sex(i):
    what = None
    if i is True:
        what = " med vad?"
    else:
        what = " med antilop" 
    print("sex" +what)

class main():

    txt = "me aNd the birds or NOT cards".casefold()

    #splits the string by words and inserts it inside a dictionary
    d = {}
    ls = len(txt.split())
    def ops(txt,d,ls):

        tl = txt.split()
        for x in range(0,):    
            if tl[x] == "not":
                d["not{0}".format(x)] = tl[x]
            elif tl[x] == "or":
                d["or{0}".format(x)] = tl[x]
            elif tl[x] == "and":
                d["and{0}".format(x)] = tl[x]
            else:
                d["txt{0}".format(x)] = tl[x]

        print(d)


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
    ops(txt,d,ls)

    """
    i = True

    while(True):
        
        sex(i)
        
        if i is True:
            i = False
        else:
            i = True
        
    """

