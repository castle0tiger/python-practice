## 과제 5-C: ChatMemory 클래스 — groq_memory의 승격

class ChatMemory:
    def __init__(self):
        self.cards = []

    def add(self, role, content):
        self.cards.append({"role": role, "content": content})

    def make_script(self, system_text):
        return [{"role": "system", "content": system_text}] + self.cards

    def count(self):
        return len(self.cards)


aichat = ChatMemory()
aichat.add("user", "파이썬이 뭐야?")
aichat.add("assistant", "Grok 답변내용")

print(aichat.make_script("한국어로 5문장이내로 답장해"))
print(aichat.count())