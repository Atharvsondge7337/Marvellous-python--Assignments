import sys 

def main():
    if len(sys.argv)  != 2:
        print("Usage: python script.py <sourcefile>")
        return
    
    source = sys.argv[1]
    destination = "Demo.txt"

    try :
        sourcefile = open(source, 'r')
        destinationfile = open (destination, 'w')
        destinationfile.write(sourcefile.read())
        print("copied contents of "+ source +  "to"+ " " +destination)

    except :
        print("Source file is not found.")


if __name__ == "__main__":
    main()