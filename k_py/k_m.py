def k_math():
    x = ''
    num1 = int(input('\033[33m请输入第一个数字\n\033[4;32mkerr\033[0m \033[36m>\033[0m'))
    fh = input('\033[33m请输入运算方式\033[36m{+,-,*,/,**,%}\033[0m\n\033[4;32mkerr\033[0m \033[36m>\033[0m')
    num2 = int(input('\033[33m请输入第二个数字\n\033[4;32mkerr\033[0m \033[36m>\033[0m'))
    if fh == '+':
        print(num1,fh,num2,'=',num1+num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    elif fh == '-':
        print(num1,fh,num2,'=',num1-num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    elif fh == '*':
        print(num1,fh,num2,'=',num1*num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    elif fh == '/':
        print(num1,fh,num2,'=',num1/num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    elif fh == '**':
        print(num1,fh,num2,'=',num1**num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    elif fh == '%':
        print(num1,fh,num2,'=',num1%num2)
        x = input('\033[33m输入任意字符继续，为空退出\n')
        if x != '':
            k_math()
    else:
        print('')


