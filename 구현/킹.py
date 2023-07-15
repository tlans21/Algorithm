move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}


king, stone, cnt = input().split()
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
k = list(map(int, [ord(king[0]) - 64, king[1]]))

for i in range(int(cnt)):
    rotation = input()
    
    nx = move[rotation][0] + k[0]
    ny = move[rotation][1] + k[1]

    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == s[0] and ny == s[1]:
            stone_nx = move[rotation][0] + s[0]
            stone_ny = move[rotation][1] + s[1]
            if 0 < stone_nx <= 8 and 0 < stone_ny <= 8:
                s = [stone_nx, stone_ny]
                k = [nx, ny] 

        else:
            k = [nx, ny]
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')





