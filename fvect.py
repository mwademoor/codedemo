from coincident import *

def main():
    a=[]
    b=[]
    populateLists(a,b)
    matches=findCoincident(a,b)
    print "Found %s match%s" % (len(matches), "es" if len(matches)!=1 else "")

    for x in matches:
        print "Concidence at %s: %s == %s" % (x, a[x], b[x])


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
