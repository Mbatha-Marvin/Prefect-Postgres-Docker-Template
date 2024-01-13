from prefect_app.flows.hello_world import hello_world_flow


hello_wold_deployment = hello_world_flow.to_deployment(
    name="hello_world_deployment",
    interval=60,
    tags=["hello_world", "docker"],
    parameters={"user_name": "Mbatha Marvin"},
)
