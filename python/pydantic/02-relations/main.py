import post as post_schema
import user as user_schema
from pydantic import ValidationError


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
        "age": 94,
        "name": "hoge",
        "posts": [],
    }

    user = user_schema.User(**user_data)
    print(user)

    try:
        user_data = {
            "id": "hoge",
            "age": -1200,
            "name": "hoge",
            "posts": [],
        }
        user_schema.User(**user_data)
    except ValidationError as e:
        print("\n>>> e.errors()")
        print(e.errors())

        print("\n>>> e.json()")
        print(e.json())

        print("\n>>> str(e)")
        print(str(e))


if __name__ == "__main__":
    main()
