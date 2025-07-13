from fastapi import FastAPI


def add_router(app: FastAPI):
    """
    Function to add user-related routes to the FastAPI application.
    """

    from app.user_module import user_router
    app.include_router(user_router, prefix="/user", tags=["user"])

