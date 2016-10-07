#  File: htmlChecker.py
#  Description: checks html file for bracketing mistakes
#  Name: Dennis Hannusch


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return(self.items.pop(0))

    def peek(self):
        return(self.items[0])

    def isEmpty(self):
        return (len(self.items) <= 0)

    def size(self):
        return( len(self.items) )

    def __str__(self):
        return str(self.items)


def getTag(infile):
    key = ''
    tags = []
    read = False
    for line in infile:
        for char in line:
            if read == True:
                if char == '>' or char == ' ' :
                    read = False
                    tags.append(key)
                    key = ''
                else:
                    key += char
            if char == '<':
                read = True
    return tags
                



def main():


    htmlFile = open('htmlfile.txt' , 'r')
    tagslist = getTag(htmlFile)
    print(tagslist)
    print()

    EXCEPTIONS = ["meta", "br", "hr"]

    s = Stack()
    VALIDTAGS = []
    for tag in tagslist:
        if tag[0] != '/':
            
            if tag not in VALIDTAGS:
                VALIDTAGS.append(tag)
                print("New tag " + tag + " found and added to list of valid tags")
                print()
                
            s.push(tag)

            if tag in EXCEPTIONS:
                s.pop()
                print("Tag " + tag + " does not need to match:  stack is still", s)
                print()
                #input("pause. . . ")
                
            else:
                print("Tag " + tag + " pushed:  stack is now", s)
                print()
                #input("pause. . . ")

            
        elif tag[0] == '/':
            newtag = tag.replace('/','')
            
            if newtag == s.peek():
                s.pop()
                print("Tag " + tag + " matches top of stack:  stack is now", s)
                print()
                #input("pause. . . ")
            else:
                print("Error:  tag is" , tag, "but top of stack is", s.peek() )
                print()
                break

    
    if s.isEmpty():
        print("Processing complete.  No mismatches found.")
    else:
        print("Processing complete.  Unmatched tags remain on stack:  ", s)

    print()
    print("Valid Tags:", VALIDTAGS)
    print("Exceptions:", EXCEPTIONS)

    

                
    htmlFile.close()


main()
