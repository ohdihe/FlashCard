import random
import time

# putting a text file to a dictionary.
DataInDic = {}
# to transfer the file content to f and then parse it to save it in a dictionary above
with open('/Volumes/MAC-ONLY/critical-thinking/state_capitals.txt', 'r') as f:
    for line in f:
        # linesplit is just a variable and the method .split(',') splits the words in the txt at the comma
        # then save each split to a list named key and value. join them later to form the dictionary
        linesplit = line.split(",")
        key = linesplit[0].lower()  # putting the text in lowercase
        value = linesplit[1].lower()  # putting the text in lowercase
        charRemove = len(value) - 1
        value = value[0:charRemove]
        DataInDic[key] = value


def main():
    print('Welcome to Flash Card')
    print('To ask a computer question enter 1 to get asked a question enter 2')
    print('')
    choice = 0
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print('That is not an integer!')
            continue
        else:
            break
    if choice == 1:
        youAsk()
    elif choice == 2:
        compAsk()


def compAsk():
    userIn = ''
    time.sleep(3)
    print("Welcome to the Flash Card ")
    print('You would be randomly asked state and capital question and you are required to answer correctly')
    begin = input('To begin enter"Y" and "Q" to quit: ').lower()
    print('Hold on while I select a question........')
    time.sleep(3)
    while userIn != 'q':
        if begin == 'y':
            for key, value in DataInDic.items():
                print(key)
                userIn = input('Enter answer: ').lower()
                if userIn != 'q':
                    if userIn in value:
                        print('That is correct!')
                    else:
                        print('Thats is wrong!. Answer is: %s' % DataInDic[key])
                else:
                    break
        else:
            break

    print('GoodBye')


def youAsk():
    userAsk = ''
    time.sleep(4)
    print('Welcome to Ask the comp')
    print('You can ask the computer a state and capital question and it will present the answer')
    start = input('To begin enter "Y" and "Q" to quit: ').lower()
    while userAsk != 'q':
        if start == 'y':
            userAsk = input('Ask either a state or capital question: ').lower()
            print('Thinking..........')
            time.sleep(3)
            for key, value in DataInDic.items():
                if userAsk != 'q':
                    if userAsk in value:
                        print('The state is %s: ' % key)
                    elif userAsk in key:
                        print('The capital is %s: ' % DataInDic[key])
                else:
                    break
        else:
            break
    print('GoodBye')


if __name__ == '__main__':
    main()
