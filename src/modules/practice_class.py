from pprint import pprint

def practice_02():
    print("practice_02")

    def show(post):
        print(f"Title: {post['title']} | Content: {post['content']} | {post['likes']} like(s)")
        print()

    posts = [
        {"title": "First post", "content": "Hello World!", "likes": 9},
        {"title": "Introduce", "content": "My name is Taro.", "likes": 10},
        {"title": "Final post", "content": "Goodbye!", "likes": 7},
    ]

    pprint(posts)
    
    show(posts[0])
    show(posts[1])
    show(posts[2])




def run():
    print("practice_class.py")

    practice_02()
    
if __name__ == "__main__":
    run()