# README

```sql
CREATE TABLE users (
        id INTEGER NOT NULL,
        name VARCHAR NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE posts (
        id INTEGER NOT NULL,
        title VARCHAR,
        content VARCHAR,
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(user_id) REFERENCES users (id)
)
```
