from modules.classes.post import Post
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


def practice_03():
    print("practice_03")

    posts = [
        Post("Hello", 3),
        Post("Hi", 5),
    ]

    print(posts[0].text)
    print(posts[0].likes)
    print(posts[1].text)
    print(posts[1].likes)

    posts[0].show()
    posts[1].show()


def run():
    print("practice_class.py")

    # practice_02()
    practice_03()
    
if __name__ == "__main__":
    run()