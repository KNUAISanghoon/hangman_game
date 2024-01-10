import random
import get_words

def MakeAnswer(words):
    randnum = random.randint(0, 99)
    answer = words[randnum]
    answersheet = ['__' for _ in range(len(answer))]
    
    return answer, answersheet

if __name__ == '__main__':
    words = get_words.GetWords()
    
    answer, answersheet = MakeAnswer(words)
    
    print(answer)
    print(*answersheet)