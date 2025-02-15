import asyncio

from typing import Any, Callable

from di import Container
from di.executors import AsyncExecutor
from di.dependent import Dependent


# Framework code
class Request:
    def __init__(self, value: int) -> None:
        print(value)
        self.value = value


class App:
    def __init__(self, _controller: Callable[..., Any]) -> None:
        self.container = Container()
        self.solved = self.container.solve(
            Dependent(_controller, scope="request"),
            scopes=["request"],
        )
        self.executor = AsyncExecutor()

    async def run(self, request: Request) -> int:
        with self.container.enter_scope("request") as state:
            return await self.solved.execute_async(
                executor=self.executor,
                values={Request: request},
                state=state,
            )


# User code
class MyClass:
    def __init__(self, request: Request) -> None:
        self.value = request.value

    def add(self, value: int) -> int:
        return self.value + value


def controller(obj: MyClass) -> int:
    return obj.add(1)


async def main() -> None:
    app = App(controller)
    resp = await app.run(Request(1))
    assert resp == 2
    resp = await app.run(Request(2))
    assert resp == 3


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
