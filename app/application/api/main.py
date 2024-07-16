from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Kafka chat',
        docs_url='/api/docs',
        description='kafka + ddd exaple'
    )
