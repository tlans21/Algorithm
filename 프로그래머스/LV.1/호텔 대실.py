def solution(book_time):
    # 현재 방의 퇴실 시간을 기록합니다.
    answer = 0
    
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time.sort()
    
    
    
    
    
    store = []
    
    for book in book_time:
        if not store:
            store.append(book)
            continue
        for index, room in enumerate(store):
            if book[0] >= room[-1] + 10:
                store[index] = room + book
                break
        else:
            store.append(book)
                
    return len(store)