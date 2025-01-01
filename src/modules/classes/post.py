class Post:
    def __init__(self, text, likes): # コンストラクタ
        self.text = text
        self.likes = likes

    def show(self):
        print(f"{self.text} - {self.likes}")

