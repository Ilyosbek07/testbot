from backend.panel.tests.models import User
from asgiref.sync import sync_to_async


@sync_to_async
def new_user(user_id: int, name: str, username: str):
    return User(user_id=user_id, name=name, username=username).save()
