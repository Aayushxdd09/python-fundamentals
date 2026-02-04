with open("file_handling/prac01poem.txt") as f:
    content = f.read()
    print(content)

    word= input("Enter a word you want to find: ")
    if(word or word.capitalize) in content:
        print("yes it is there")
        print(content.count("twinkle") + content.count("Twinkle"), "times")
    else:
        print("Nope not there")

