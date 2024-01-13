from prefect import task
from prefect_app.utils.date import get_current_date


@task(
    name="hello_world_start",
    description="Logs the Hello World Flow has started",
    version="0.1.0",
    tags=["hello_world", "docker"],
    log_prints=True,
    timeout_seconds=5,
)
def hello_world_start(user_name: str) -> str:
    return f"Hello {user_name}"


@task(
    name="hello_world_get_date",
    description="Returns the date",
    version="0.1.0",
    tags=["hello_world", "docker"],
    log_prints=True,
    timeout_seconds=5,
)
def hello_world_get_date() -> str:
    return get_current_date()


@task(
    name="hello_world_log_date",
    description="Logs the date it recieves",
    version="0.1.0",
    tags=["hello_world", "docker"],
    log_prints=True,
    timeout_seconds=5,
)
def hello_world_log_data_and_greeting(date: str, greeting: str) -> bool:
    if date and greeting:
        print(f"{greeting}. Today is {date}")
        return True
    else:
        return False


@task(
    name="hello_world_goodbye",
    description="Logs good bye",
    version="0.1.0",
    tags=["hello_world", "docker"],
    log_prints=True,
    timeout_seconds=5,
)
def hello_world_goodbye(success_logging_data: bool) -> bool:
    if success_logging_data:
        print("GoodBye. I Hope to see you soon")
    else:
        raise RuntimeError("Did not log data")
