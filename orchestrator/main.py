from prefect import serve
# from time import sleep
from prefect_app.app.pipelines.hello_world.deployment import hello_wold_deployment

if __name__ == "__main__":
    # sleep(5)
    serve(hello_wold_deployment)