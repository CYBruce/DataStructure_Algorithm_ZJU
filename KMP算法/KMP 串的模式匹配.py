String = input()
check_time = int(input())
for i in range(check_time):
    pattern = input()
    try:
        index = String.index(pattern)
    except ValueError:
        print('Not Found')
    else:
        print(String[index:])
