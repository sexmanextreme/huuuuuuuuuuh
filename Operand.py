

class ops():
        txt = "me aNd the birds or NOT cards".casefold()

    #splits the string by words and inserts it inside a dictionar
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
