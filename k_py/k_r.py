import random
def k_random():
    str_dxsz = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_num = input('\033[33m请输入位数\n\033[4;32mkerr\033[0m \033[36m>\033[0m')
    str_num = input('\033[33m请输入个数\n\033[4;32mkerr\033[0m \033[36m>\033[0m')
    str_list = []
    for l in range(int(str_num)):
        for i in range(int(random_num)):
            str_list.append(random.choice(str_dxsz))
        strl = ''.join(str_list)
        print(strl)
        str_list = []

