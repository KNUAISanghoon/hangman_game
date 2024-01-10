def GetWords():
    words = []
    
    with open('c:/Users/SanghoonLee/Desktop/for_python/Hangman/words.txt', 'r') as f:
        for _ in range(100):
            words.append(f.readline().strip().lower())
    
    return words
            

if __name__ == '__main__':
    w = GetWords()
    print(w)