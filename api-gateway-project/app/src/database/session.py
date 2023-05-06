from typing import Callable, Any, TypeVar, cast, Iterator
from functools import wraps
from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.core import get_setting


engine: Engine = create_engine(url=get_setting().DATABASE_URL)
Function = TypeVar(name="Function", bound=Callable[..., Any])


@contextmanager
def _create_session() -> Iterator[Session]:
    session: Session = Session(bind=engine)
    try:
        yield session
        session.commit()

    except SQLAlchemyError as error:
        session.rollback()
        raise Exception(f"Database Error: {str(error)}")

    finally:
        session.close()


def get_db(function: Function) -> Function:
    @wraps(wrapped=function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with _create_session() as session:
            return function(*args, **kwargs, session=session)

    return cast(Function, wrapper)
