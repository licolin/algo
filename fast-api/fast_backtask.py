# -*- encoding: utf-8 -*-
# Author: li_colin

from typing import Union

from fastapi import BackgroundTasks, Depends, FastAPI
import time

app = FastAPI()


def write_log(message: str):
    while True:
        time.sleep(2)
        print("msg!")


def get_query(background_tasks: BackgroundTasks, q: Union[str, None] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
        email: str, background_tasks: BackgroundTasks, q: str = Depends(get_query)):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
