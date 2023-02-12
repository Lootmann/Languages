import post as post_schema
import user as user_schema


def get_posts():
    return [
        post_schema.Post(id=1, title="hello", content="hoge"),
        post_schema.Post(id=2, title="hello", content="hoge"),
        post_schema.Post(id=3, title="hello", content="hoge"),
        post_schema.Post(id=4, title="hello", content="hoge"),
    ]


def main():
    user_data = {
        "id": 1,
        "name": "hoge",
        "posts": get_posts(),
    }
    user = user_schema.User(**user_data)
    print(user)


if __name__ == "__main__":
    main()
