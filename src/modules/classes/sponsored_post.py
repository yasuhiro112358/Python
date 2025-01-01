from modules.classes.post import Post

class SponsoredPost(Post): # Postクラスを継承
    pass
    def __init__(self, text, sponsor): # コンストラクタ
        super().__init__(text) # 親クラスのコンストラクタを呼び出す
        self._sponsor = sponsor
    
    def show(self):
        print(f"{self._text} - {self._likes} sponsored by {self._sponsor}")

