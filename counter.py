def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    emails=dict()
    for line in handle:
        if line.startswith('From '):
            words=line.split()
            emails[words[1]]= emails.get(words[1],0)+1

    #maxi=0    
    #email=None
    #for list in emails:
    #    if emails[list]>maxi:
    #        maxi=emails[list]
    #        email= list
    maxi=max(emails.keys(), key=(lambda k: emails[k]))

    print(maxi, emails[maxi])

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
