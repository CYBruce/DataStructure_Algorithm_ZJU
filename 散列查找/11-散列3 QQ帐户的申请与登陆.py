#11-散列3 QQ帐户的申请与登陆 （25 分)
N = int(input())
qq = {}
for i in range(N):
    flag,number,passcode = input().split()
    if flag == 'N':
        if number not in qq.keys():
            qq[number]=passcode
            print('New: OK')
        else:
            print('ERROR: Exist')
    elif flag == 'L':
        if number not in qq.keys():
            print('ERROR: Not Exist')
        elif passcode == qq[number]:
            print('Login: OK')
        else:
            print('ERROR: Wrong PW')
