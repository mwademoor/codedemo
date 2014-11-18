from coincident import *

def main():
    a=[]
    b=[]
    populateLists(a,b)
    matches=findCoincident(a,b)
    print "Found ", len(matches)," matches"

    for x in matches:
        print "Concidence at ",x," ",a[x], " == ", b[x]


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
