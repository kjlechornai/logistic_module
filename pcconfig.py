import pynecone as pc

config = pc.Config(
    app_name="inventory_module",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
