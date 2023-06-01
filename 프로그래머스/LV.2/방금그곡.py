def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer = []
    index = 0
    for i in musicinfos:
        index += 1
        start, end, title, M = i.split(',')
       
        st1, st2 = start.split(':')
        start = (int(st1) * 60) + int(st2)
        st3, st4 = end.split(':')
        end = (int(st3) * 60) + int(st4)
       
        time = end - start
        #기억속 음의 길이 
        changed = change(M)
        a = len(changed)
        
        #음악 길이
        b = changed * (time // a) + changed[:time%a]
        k = change(m)
        
        #재생된 음악 길이
        
       
        
        if k in b:
            answer.append([time, index, title])
            
    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2] # 첫번째 제목을 리턴
        