#  File: htmlChecker.py
#  Description: checks html file for bracketing mistakes
#  Name: Dennis Hannusch

#standard Stack data structure
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
    #initialize variables
    key = ''
    tags = []
    read = False
    for line in infile:
        #parsing line by line
        for char in line:
            #parsing character by character
            if read == True:
                if char == '>' or char == ' ' :
                #if we reach the end bracket or a space we stop reading, append the tag to a list, and reset the key string
                    read = False
                    tags.append(key)
                    key = ''
                else:
                #otherwise we will continue to append the characters to the key string
                    key += char
            if char == '<':
                #if statement indicating when to start reading characters
                read = True
    return tags
                



def main():


    htmlFile = open('htmlfile.txt' , 'r')
    #open html file for reading
    tagslist = getTag(htmlFile)
    #tagslist hold the list of tags that were read and parsed through in getTag()
    print(tagslist)
    #we print the taglist in order to display everything that was produced in getTag()
    print()

    EXCEPTIONS = ["meta", "br", "hr"]
    #list of tags that are exceptions, i.e. do not have close brackets
    #there are many more exceptions which have not been included in this program 
    #this have been left shortened for testing purposes only

    s = Stack()
    #initialize Stack() object
    VALIDTAGS = []
    #initialize and empty list which will store the valid tags read in
    
    for tag in tagslist:
        if tag[0] != '/':
        #looking soley at opening tags    
            if tag not in VALIDTAGS:
                #this statement adds tags into VALIDTAGS list if and only when they are new
                VALIDTAGS.append(tag)
                print("New tag " + tag + " found and added to list of valid tags")
                print()
            
            #tag is pushed on the the bottom of the Stack
            s.push(tag)

            if tag in EXCEPTIONS:
                #if the tag is one of the Exceptions, we do not need it on the stack; so we pop it off
                s.pop()
                print("Tag " + tag + " does not need to match:  stack is still", s)
                print()
                #input("pause. . . ")
                
            else:
                #Otherwise we leave the tag in the stack and display that we have pushed it onto the stack
                print("Tag " + tag + " pushed:  stack is now", s)
                print()
                #input("pause. . . ")

            
        elif tag[0] == '/':
        #looking at closing tags
            newtag = tag.replace('/','')
            #we remove the '/' from the tag
            
            if newtag == s.peek():
            #if the tag matches the tag on the top of the Stack we pop it off the Stack
                s.pop()
                print("Tag " + tag + " matches top of stack:  stack is now", s)
                print()
                #input("pause. . . ")
            else:
            #otherwise, we have an error which we indicate to the user and we break from the program
                print("Error:  tag is" , tag, "but top of stack is", s.peek() )
                print()
                break

    
    if s.isEmpty():
        #After completion, if the Stack is empty, we have a correct html file
        print("Processing complete.  No mismatches found.")
    else:
        #If the Stack still contains tags, we have a mistake in the html file
        print("Processing complete.  Unmatched tags remain on stack:  ", s)

    print()
    #Finally we display our list of Valid Tags and our list of Exceptions
    print("Valid Tags:", VALIDTAGS)
    print("Exceptions:", EXCEPTIONS)

    

    #file is closed           
    htmlFile.close()


main()
