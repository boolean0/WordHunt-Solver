import time
wordList = []

def main():
    with open('allwords.txt', 'r') as reader:
        for word in reader: 
            if(len(word) > 3 and len(word) <= 19): 
                wordList.append(word)

    wordList.sort(key=len, reverse = True)

    with open('test.txt', 'w') as writer: 
        for word in wordList: 
            writer.write(word)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))