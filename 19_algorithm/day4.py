def most_frequent(text):

    counts = {}

    for t in text:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1

    frequent = text[0]
    
    for key in counts:
        if counts[frequent] < counts[key]:
            frequent = key

    return frequent, counts[frequent] 
# return return A, B처럼 쉼표로 여러 개를 돌려줄 수 있음

print(f"hello 최다: {most_frequent('hello')}")
print(f"banana 최다: {most_frequent('banana')}")


## 키와 값을 변수 frequent에 저장한 경우 (중복 저장이어서 실무에선 지양하는 방법)
def most_frequent_v2(text):

    counts = {}

    for t in text:
        if t in counts:
            counts[t] += 1
        else:
            counts[t] = 1

    frequent = [text[0], counts[text[0]]]
    # [글자, 개수] 리스트 형식으로 저장
    
    for key in counts:
        if frequent[1] < counts[key]: # frequent[1] = 저장된 개수(리스트 2번째 요소)
            frequent = [key, counts[key]] # 글자와 개수를 쌍으로 교체

    return frequent
## 앞선 것보다 코드 쓰기 읽기 모두 복잡해짐

print(most_frequent_v2("hello"))
print(most_frequent_v2("banana"))
