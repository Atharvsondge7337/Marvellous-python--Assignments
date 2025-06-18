def main():

    filename = input("Enter a file name :")

    search_word = input("Enter a word to search :")

    try :
        fobj = open(filename , 'r')
        contents  = fobj.read()
        count = contents.count(search_word)
        print("The word" +search_word+ "appers" + count +" times ")
    except  FileNotFoundError :
        print("file not found.")

if __name__ == "__main__":
    main()