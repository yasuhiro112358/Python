from modules.classes.post import Post
from modules.classes.sponsored_post import SponsoredPost
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
        Post("Hello"),
        Post("Hi"),
        SponsoredPost("Hey", "dotinstall")
    ]

    posts[0].like()
    posts[0].like()
    posts[2].like()

    for post in posts:
        post.show()

    # posts[0].set_likes(100)
    # print(posts[0].get_likes())

    posts[0].likes = 100
    print(posts[0].likes)

    Post.show_count()




def run():
    print("practice_class.py")

    # practice_02()
    practice_03()
    
if __name__ == "__main__":
    run()