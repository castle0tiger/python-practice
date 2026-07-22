toolbox = []

def tool(func):
    toolbox.append(func)
    return func

@tool
def hello():
    print("인사말 올립니다.")

@tool
def information():
    print("@데코를 실습중입니다.")

@tool
def calculation():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for n in number:
        total += n
    return total

print(len(toolbox))

for t in toolbox:
    t()

print("\n")

for t in toolbox:
    result = t()
    print("리턴값:", result)