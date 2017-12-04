from k_py import k_r
from k_py import k_m
print('\033[36m',end='')
print(r'''
        /^\   /^/  
        | |  / /    [^]  \^  /''\  /^\
        | | / /           | |      | |  /^/
        | |/\~\     |^|   | |      | | / /
        | |  \ \    | |   | |      | |/\~\
        | |   \ \   | |   | |      | |  \ \
        |_|    \_\  |_|   |_|      |_|   \_\
        ''')
print('\033[0m',end='')
def main():
       commed = input('\033[4;32mkerr\033[0m \033[36m>\033[0m')
       if commed == '生成随机字符串' or commed == '01':
           k_r.k_random()
       elif commed == '' or commed == '02':
           k_m.k_math()
       else:
           print('\033[33m再见！')

main()
