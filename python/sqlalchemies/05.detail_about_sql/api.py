import functools
from random import choice, randint, sample
from string import ascii_letters

from models import Like, Tweet, User
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, lazyload, selectinload, subqueryload
from sqlalchemy.sql import select


def random_string(min_=5, max_=20) -> str:
    return "".join(sample(ascii_letters, randint(min_, max_)))


def title(msg: str):
    def wrapper(f):
        @functools.wraps(f)
        async def inner(*args, **kwargs):
            print("-----" * 5)
            print(f"--- {msg}")
            print("-----" * 5)
            await f(*args, **kwargs)
            print()

        return inner

    return wrapper


async def random_user(db: AsyncSession) -> User:
    """
    get random user with no tweets and likes
    """
    stmt = select(User).order_by(func.random())
    return (await db.execute(stmt)).scalar()


async def random_user_with_relations(db: AsyncSession) -> User | None:
    """
    get random user with all tweets and likes relations
    """
    stmt = (
        select(User)
        .order_by(func.random())
        .options(selectinload(User.tweets))
        .options(selectinload(User.likes))
    )
    return (await db.execute(stmt)).scalar()


async def random_tweet(db: AsyncSession) -> Tweet | None:
    stmt = select(Tweet).order_by(func.random())
    return (await db.execute(stmt)).scalar()


@title("Create User")
async def create_user(db: AsyncSession):
    user = User(name=random_string())
    db.add(user)
    await db.commit()
    await db.refresh(user)


@title("SELECT USER")
async def select_user(db: AsyncSession):
    """
    get All User model with all tweets and likes relations

    super heavy performance
    """
    stmt = (
        select(User)
        .join(User.tweets)
        .options(
            subqueryload(User.tweets).selectinload(Tweet.user),
            subqueryload(User.likes).selectinload(Like.user),
        )
    )
    results = await db.execute(stmt)
    for user in results.scalars():
        print(user.id, user.name, user.tweets, user.likes)


@title("Create Tweet")
async def create_tweet(db: AsyncSession):
    user = await random_user(db)
    if not user:
        return
    tweet = Tweet(message=random_string(), user_id=user.id)

    db.add(tweet)
    await db.commit()
    await db.refresh(tweet)


@title("Select Tweet")
async def select_tweet(db: AsyncSession):
    stmt = select(User, Tweet).join(Tweet, User.id == Tweet.user_id).limit(2)
    tweets = await db.execute(stmt)
    for t in tweets.all():
        print("type(t[0])", type(t[0]))
        print("type(t[1])", type(t[1]))


@title("Create Like")
async def create_like(db: AsyncSession):
    for _ in range(3):
        user: User = await random_user(db)
        if not user:
            return

        tweet: Tweet = await random_tweet(db)
        if not tweet:
            return

        like: Like = Like(user_id=user.id, tweet_id=tweet.id)

        db.add(like)
        await db.commit()
        await db.refresh(like)


@title("Super Test")
async def test(db: AsyncSession):
    """
    ある Tweet に Like している User を全取得
    GET `/tweets/:tweet_id/likes/users`
    """
    tweet = await random_tweet(db)
    if not tweet:
        return

    print("\n>>> Tweet : ", tweet.id)
    print()

    stmt = (
        select(User)
        .join(User.likes)
        .join(Like.tweet)
        .filter(Tweet.id == tweet.id)
        .options(selectinload(User.tweets), selectinload(User.likes))
    )
    result = await db.execute(stmt)
    users = result.scalars().all()

    for user in users:
        print(user.id, user.name, user.likes)
