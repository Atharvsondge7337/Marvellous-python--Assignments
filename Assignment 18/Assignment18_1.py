import os 

def main():
    filename = input("Enter the Filename :")

    if os.path.isfile(filename):
        print(filename + "exists.") 
    else :
        print(filename +"does not exists")
    
if __name__ == "__main__":
    main()