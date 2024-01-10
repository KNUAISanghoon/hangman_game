import hangman_image as hi
import get_words
import make_answer
import game_state_print as gsp
import sys

hi.HangmanLogo()
words = get_words.GetWords()
life = 5

while life != 0:
    command = int(input('1. 게임 시작 / 2. 단어 목록 확인 / 3. 도움말 / 0. 종료 (원하는 항목의 숫자를 입력하세요 ^^) : '))
    
    if command == 0:
        print('\nHangman 게임을 종료합니다.')
        break
    elif command == 2:
        print('\n      ---단어 목록---\n')
        for i in range(0, 100, 5):
            print('{}, {}, {}, {}, {}'.format(words[i], words[i + 1], words[i + 2], words[i + 3], words[i + 4]))
    elif command == 1:
        answer, answersheet = make_answer.MakeAnswer(words)
        print('\n임의의 단어가 선택되었습니다.\n')
        gsp.GameStatePrint(answersheet, life)
        
        while life != 0:
            a = input('\n정답을 입력하세요 :')
            
            if life == 0:
                
                gsp.GameStatePrint(answersheet, 0)
                print(life)
                break
                
            if 65 <= ord(a) <= 90:
                print('\n반드시 소문자를 입력하십시오.\n')
            elif not(97 <= ord(a) <= 122):
                print('\n알파벳 소문자 외의 입력은 허용되지 않습니다.\n')
            else:
                if a in answer:
                    indices = []
                    index = answer.find(a)
        
                    print('\n입력하신 알파벳이 존재합니다!\n')
                    
                    while index != -1:
                        indices.append(index)
                        index = answer.find(a, index + 1)
        
                    for i in indices:
                        answersheet[i] = a
        
                else:
                    life -= 1
                    print('\n입력하신 알파벳이 존재하지 않습니다 !\n')
    
                gsp.GameStatePrint(answersheet, life)
            
            if not ('__' in answersheet):
                print('\n축하합니다 ! 정답을 맞추셨습니다 !\n')
                sys.exit()
            
