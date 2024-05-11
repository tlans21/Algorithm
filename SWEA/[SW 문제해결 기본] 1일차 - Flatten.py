T = 10


for tc in range(1, T + 1):
    dump = int(input())
    blocks = list(map(int, input().split()))
    

    while dump:
        maxHeight = -123
        minHeight = 555555555
        maxidx = -1
        minidx = -1
        for idx, block in enumerate(blocks):
            if maxHeight < block:
                maxHeight = block
                maxidx = idx

            if minHeight > block:
                minHeight = block
                minidx = idx
        # 수정
        
        blocks[maxidx] = maxHeight - 1
        blocks[minidx] = minHeight + 1
        dump -= 1
    answer = max(blocks) - min(blocks)
    print("#{} {}".format(tc, answer))

for i in range(1,11):

    dump = int(input())

    box = list(map(int, input().split()))

 

    while dump:

        max_box = max(box)

        min_box = min(box)

        max_idx = box.index(max(box))

        min_idx = box.index(min(box))

 

        box[max_idx] -= 1

        box[min_idx] += 1

 

        dump -= 1

 

    print('#{} {}'.format(i,max(box)-min(box)))
    

              
        
