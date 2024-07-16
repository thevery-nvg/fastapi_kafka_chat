from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title='Kafka chat',
        docs_url='/api/docs',
        description='kafka + ddd example',
        debug=True
    )
    return app
