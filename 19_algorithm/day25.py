def flatten(input):
    result = []

    for i in input:
        if isinstance(i, list) == True:
            result.extend(flatten(i))
        else:
            result.append(i)

    return result


print(flatten([1, 2, 3]))
print(flatten([1, [2, 3], 4]))
print(flatten([1, [2, [3, 4]], 5]))
print(flatten([[1, 2], [3, [4, 5]]]))


## 리스트 매서드 주의사항 : "원본을 바꾸는 메서드는 None을 반환한다"
# 리스트를 "바꾸는" 메서드 (append, extend, sort...):
#   → 리스트 자체를 직접 수정하고, return은 None
#   → 그래서 result.append(i) 는 result를 바꿀 뿐, 값으로 쓰면 None

# 새 걸 "돌려주는" 함수 (sorted, len...):
#   → 원본 안 바꾸고 결과를 return

## 결론 : 바꾸는 메서드(sort/append/extend/reverse) → None 반환 
#         새로 만드는 함수(sorted/len) → 결과 반환