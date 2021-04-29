import random

class Equals:
    def __init__(self) -> None:
        pass
    def produce_equal(self, level, kuohao, max_number):
        equal_stack = [] # 算式栈
        opr = ['+', '-', '*', '/'] # 运算符

        # 生成数字
        number1 = random.randint(1, max_number)
        number2 = random.randint(1, max_number)
        number3 = random.randint(1, max_number)
        number4 = random.randint(1, max_number)

        # 算式生成部分
        equal_stack.append(str(number1))
        opr_pos = random.randint(0, 3)
        equal_stack.append(opr[opr_pos])
        equal_stack.append(str(number2))
        opr_pos = random.randint(0, 3)
        equal_stack.append(opr[opr_pos])
        equal_stack.append(str(number3))
        if level == 0: # 简单难度3元式
            pass
        elif level == 1: # 困难难度4元式
            opr_pos = random.randint(0, 3)
            equal_stack.append(opr[opr_pos])
            equal_stack.append(str(number4))

        if kuohao == 0:
            pass
        elif kuohao == 1:
            if level == 0:
                kuohao_pos = [0, 2]
                index = random.randint(0, 1)
                equal_stack.insert(kuohao_pos[index], '(')

                equal_stack.insert(kuohao_pos[index] + 4, ')')

            elif level == 1:
                kuohao_pos = [0, 2, 4]
                index = random.randint(0, 1)
                equal_stack.insert(kuohao_pos[index], '(')

                equal_stack.insert(kuohao_pos[index] + 4, ')')

        # print(equal_stack)
        equal_str = ''.join(equal_stack)
        # print(equal_str)
        # print(eval(equal_str))
        answer = eval(equal_str)

        for item in range(len(equal_stack)):
            if equal_stack[item] == '*':
                equal_stack[item] = '×'
            elif equal_stack[item] == '/':
                equal_stack[item] = '÷'
            elif equal_stack[item] == '+':
                equal_stack[item] = '＋'
            elif equal_stack[item] == '-':
                equal_stack[item] = '－'
        
        equal_stack.append('=')
        equal_str = ''.join(equal_stack)

        return equal_stack, equal_str, answer


if __name__ == '__main__':
    math = Equals()
    equal_stack, equal_str, answer = math.produce_equal(1, 1, 20)
    print(equal_stack, equal_str, answer)
