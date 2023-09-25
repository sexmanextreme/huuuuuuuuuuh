def sex(i):
    what = None
    if i is True:
        what = " med vad?"
    else:
        what = " med antilop"
    
    print("sex" +what)
    
i = True

guh=0
while(True):
    
    sex(i)
    
    if i is True:
        i = False
    else:
        i = True
    
    guh+=1
    