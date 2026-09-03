## 재귀로 평탄화 -> 다른 함수로 결과 만들기
def flatten(input):
    result = []

    for i in input:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


def nested_stats(input):
    result = {}

    result["개수"] = len(flatten(input))
    result["합"] = sum(flatten(input))
    result["최대"] = max(flatten(input))

    return result


print(nested_stats([1, [2, [3, 4]], 5]))
print(nested_stats([10, [20], 30]))
print(nested_stats([[7]]))
print("")


## 피드백 : 한번만 flatten 하고 값을 저장시키기
def nested_stats_v2(input):
    flat = flatten(input)   # 딱 한 번!
    return {"개수": len(flat), "합": sum(flat), "최대": max(flat)}

print(nested_stats_v2([1, [2, [3, 4]], 5]))
print(nested_stats_v2([10, [20], 30]))
print(nested_stats_v2([[7]]))
print("")


# 재귀 하나가 개수·합·최대를 동시에 들고 다니며 합치기
def nested_stats_v3(input):
    result = {}
    count = 0
    total = 0
    biggest = None  # "아직 아무것도 못 봤다"는 뜻

    for i in input:
        if isinstance(i, list):
            sub = nested_stats_v3(i)  # sub = {"개수": n, "합": s, "최대": m}
            count += sub["개수"]
            total += sub["합"]
            if biggest is None or sub["최대"] > biggest:
                biggest = sub["최대"]
        
        else:
            count += 1
            total += i
            if biggest is None or i > biggest:
                biggest = i

    result["개수"] = count
    result["합"] = total
    result["최대"] = biggest

    return result


print(nested_stats_v3([1, [2, [3, 4]], 5]))
print(nested_stats_v3([10, [20], 30]))
print(nested_stats_v3([[7]]))


## 복잡한 재귀 함수 문제 접근법
# 1단계: 숫자를 만났을 때 처리 + 최종 결과(딕셔너리) 만드는 부분을 먼저 완성
# 2단계: 그 다음에 리스트 만났을 때(재귀) 부분을 채운다


## 실무자들이 접근하는 방식 (일반화)
# 1단계 : base case(멈추는 조건) + "제일 단순한 경우"를 먼저 확정
# -> 1. 가장 단순한 경우(else branch)와 결과 포장(return)부터 완성

# 2단계 : 그 확정된 "약속"을 믿고, 복잡한 경우(재귀 부분)를 나중에 채움
# -> 2. 재귀 호출 부분은 그 다음에, "방금 쓴 return을 그대로 믿고" 채우기
