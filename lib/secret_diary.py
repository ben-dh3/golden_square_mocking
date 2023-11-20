# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary.content
        self.locked = True

    def read(self):
        if self.locked == True:
            return "Go away!"
        else:
            return self.diary
        

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False