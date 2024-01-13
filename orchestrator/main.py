from prefect import serve
from prefect_app.deployments.hello_world import hello_wold_deployment

if __name__ == "__main__":
    serve(hello_wold_deployment)
