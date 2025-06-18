import sys

def main():
    if len(sys.argv) != 3:
        print("Usage : python script.py <file1> <file2>")

        file1 , file2 = sys.argv[1],sys.argv[2]

        try:
            fobj1 = open(file1 , 'r')
            fobj2 = open(file2 , 'r')

            if fobj1.read() == fobj2.read():
                print("Success :FIles are same .")
            else:
                print("Failure : files are not same ")
        except FileNotFoundError:
            print("One or Both files are not found .")

if __name__ == "__main__":
    main()