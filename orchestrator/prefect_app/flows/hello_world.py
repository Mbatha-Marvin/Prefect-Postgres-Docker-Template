from prefect import flow
from prefect_app.tasks.hello import (
    hello_world_start,
    hello_world_get_date,
    hello_world_log_data_and_greeting,
    hello_world_goodbye,
)


@flow(
    name="hello_world_flow",
    description="A Demo flow to show prefect and docker compose setup",
    version="0.1.0",
    retries=2,
    log_prints=True,
)
def hello_world_flow(user_name: str):
    greeting = hello_world_start(user_name=user_name)
    date_today = hello_world_get_date()
    log_data_success = hello_world_log_data_and_greeting(
        date=date_today, greeting=greeting
    )
    hello_world_goodbye(success_logging_data=log_data_success)
