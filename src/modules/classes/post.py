class Post:
    _count = 0 # クラス変数

    def __init__(self, text): # コンストラクタ
        # _をつけることで外部からアクセスしてほしくない変数であることを示す
        self._text = text # インスタンス変数
        self._likes = 0 
        Post._count += 1

    @classmethod
    def show_count(cls):
        print(f"{cls._count} instances created") # クラス変数にアクセスするためにclsを使う

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

    # def get_likes(self): # getter
    #     return self._likes

    # def set_likes(self, num): # setter
    #     self._likes = num

    @property
    def likes(self):
        return self._likes
    
    @likes.setter
    def likes(self, num):
        self._likes = num