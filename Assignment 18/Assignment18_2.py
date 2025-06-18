import os 

def main():
    filename = input("Enter the Filename :")
    try:
        fobj = open(filename ,'r')
        print(fobj.read())

    except FileNotFoundError:
        print(filename +"not found")

        
if __name__ == "__main__":
    main()