def word_counter():
    words={}
    while True:
        word = input("Enter words:").split(" ")
        for i in word:
            if i in words:
                words[i]+=1
            else:
                words[i]=1
        rep = 0
        for r in word:
            words[r]
            rep = rep+1
        print(f"count{rep}")
        if words[r]>rep:
            print(f"most frequent:{r}")

word_counter()
