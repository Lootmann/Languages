# Basic Relationship Patterns

[SQLAlchemy 2.0 - Basic Relationship Pattenrs](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)


A quick walkthrough of the basic relational patterns,
which in this section are illustrated
using Declarative style mappings based on the use of the Mapped annotation type.

> 基本的な Relationship のパターンを駆け足でさらいましょう
> Mapped anotation type というものを利用して
> Declarative スタイルでマッピングをします

The setup for each of the following sections is as follows:

> 必要なセットアップはこいつら

```
from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass
```


## Declarative vs. Imperative Forms

As SQLAlchemy has evolved, different ORM configurational styles have emerged.
For examples in this section and others that use annotated Declarative mappings with Mapped,
the corresponding non-annotated form should use the desired class, or string class name,
as the first argument passed to relationship().

> SQLAlchemyの発展に伴い, 様々はORMの宣言スタイルを吸収してきました
> このセクションの例では `Mapped` を利用して Declarative mapping を利用してます
> non-annotated form に対応する `desired class`, `string class name`, を利用すべきです
> relationship に引数を渡すという形で

The example below illustrates the form used in this document,
which is a fully Declarative example using PEP 484 annotations,
where the relationship() construct is also deriving the target class
and collection type from the Mapped annotation,
which is the most modern form of SQLAlchemy Declarative mapping:

> 下の例では 完全な `Declarative` な例が乗っています
> relationship() は target lcass と collection type を得ることが出来ます
> Mapped annotation というものを利用して
> この例は今一番ホットな SQLAlchemy の宣言的 mapping です


```
class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")
```

In contrast, using a Declarative mapping without annotations is the more “classic” form of mapping,
where relationship() requires all parameters passed to it directly, as in the example below:

> 対象的に annotations を利用しない `Declarative` mapping を使って 旧型のMappingを
> かましたのがこちらです `relationship()` はすべてのパラメータを直接指定する必要があります

```
class Parent(Base):
    __tablename__ = "parent_table"

    id = mapped_column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"

    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(ForeignKey("parent_table.id"))
    parent = relationship("Parent", back_populates="children")
```

Finally, using Imperative Mapping,
which is SQLAlchemy’s original mapping form before Declarative was made
(which nonetheless remains preferred by a vocal minority of users),
the above configuration looks like:

> 終わりに `Declarative` 以前の  Imperative Mappingを利用したMapping をお見せします
>  (マイノリティのユーザのためだけに残しているクソ機能です)
> こんな感じです

```
registry.map_imperatively(
    Parent,
    parent_table,
    properties={"children": relationship("Child", back_populates="parent")},
)

registry.map_imperatively(
    Child,
    child_table,
    properties={"parent": relationship("Parent", back_populates="children")},
)
```


Additionally, the default collection style for non-annotated mappings is list.
To use a set or other collection without annotations,
indicate it using the relationship.collection_class parameter:

```
class Parent(Base):
    __tablename__ = "parent_table"

    id = mapped_column(Integer, primary_key=True)
    children = relationship("Child", collection_class=set, ...)
```

Detail on collection configuration for relationship() is at Customizing Collection Access.

Additional differences between annotated
and non-annotated / imperative styles will be noted as needed.
