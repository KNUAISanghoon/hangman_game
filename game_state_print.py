import hangman_image as hi
import time

def GameStatePrint(answersheet, life):
    print('\n남은 빈칸의 수 :', *answersheet)
    print('\n')
    
    print('현재 목숨 상태 :')
    
    if life == 5:
        hi.PrintLife(0)
    elif life == 4:
        hi.PrintLife(1)
    elif life == 3:
        hi.PrintLife(2)
    elif life == 2:
        hi.PrintLife(3)
    elif life == 1:
        hi.PrintLife(4)
    elif life == 0:
        hi.ExplosionHangman()
        time.sleep(2)
        print('\n' * 3)
        hi.GameOver()

if __name__ == '__main__':
    a = ['__' for _ in range(5)]
    
    GameStatePrint(a, 5)
    GameStatePrint(a, 4)
    GameStatePrint(a, 3)
    GameStatePrint(a, 2)
    GameStatePrint(a, 1)
    GameStatePrint(a, 0)
        
    
    