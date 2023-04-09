import weaviate

client = weaviate.Client(
    url="https://some-endpoint.weaviate.network",  # Replace with your endpoint
)

schema = client.schema.get()
