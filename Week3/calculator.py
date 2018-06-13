import re

def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index] == ' ' or line[index] == '(' or line[index] == ')':
            index += 1
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluate_muldiv(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                tokens[index - 2]['number'] *= tokens[index]['number']
                del tokens[index - 1: index + 1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIVIDE':
                if(tokens[index]['number'] != 0):
                   tokens[index - 2]['number'] /= float(tokens[index]['number'])
                else:
                    print('Error: divisor = 0')
                    exit(1)
                del tokens[index - 1: index + 1]
                index -= 2
            # else:
            #     print('Invalid syntax')
        index += 1
    return tokens

def evaluate(tokens):
    tokens = evaluate_muldiv(tokens)
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
        index += 1
    return answer

def evaluateBracket(line):
    bracketNum = len(re.findall("\(", line))
    while(bracketNum > 0):
        newLine = line.split(")", 1)[0].rsplit("(", 1)[1]
        answer = evaluate(tokenize(newLine))
        line = line.split(")", 1)[0].rsplit("(", 1)[0] + str(answer)+line.split(")", 1)[1]
        bracketNum -= 1
    return evaluate(tokenize(line))


def test(line, expectedAnswer):
    # tokens = tokenize(line)
    # actualAnswer = evaluate(tokens)
    actualAnswer = evaluateBracket(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("1*2+3/4", 2.75)
    test("1.2*3-4/5.0", 2.8)
    test("3.0+4*2-1/5", 10.8)
    test("(1.5+2)*3/(2+3)", 2.1)
    test("3.3*(10/(2+3))+4*5", 26.6)
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ',)
    # line = raw_input()
    line = input()
    # tokens = tokenize(line)
    actualAnswer = evaluateBracket(line)
    print("answer = %f\n" % actualAnswer)
