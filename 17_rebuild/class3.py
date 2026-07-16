class StudyLog:
    def __init__ (self):
        self.logs = []

    def add(self, subject, hours):
        self.logs.append({"과목": subject, "시간": hours})
    
    def total_hours(self):
        total_h = 0
        
        for log in self.logs:
            total_h += log["시간"]
        
        return total_h

    def best_subject(self):
        best_log = self.logs[0]

        for log in self.logs:
            if best_log["시간"] < log["시간"]:
                best_log = log
        return best_log["과목"]
    

study = StudyLog()
study.add("영어", 1)
study.add("파이썬", 3)
study.add("통계", 2)

print(study.total_hours())
print(study.best_subject())

