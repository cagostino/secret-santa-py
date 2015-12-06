import random
names= ['andrew','adam', 'giotto', 'jp$', 'dman','ollie', 'niq', 'griff', 'radman','grace', 'rob', 'aidan', 
'johnny', 'ryan', 'dave', 'nolan', 'jerry',' seamus', 'joepa', 'jeff'] #input your own
def match(lstnames):
        xlen  =len(lstnames)
        xc= {}
        for j in range(xlen):
            ismatched = False
            print j
            while not ismatched:
                pick =random.randint(0,xlen-1)
                print pick, j

                nam = lstnames[pick]
                print nam
                if nam not in xc.values() and nam != lstnames[j]:
                    xc[lstnames[j]]=lstnames[pick]
                    ismatched=True
                pick = random.randint(0,xlen)
        return xc
matches = match(names)
print matches