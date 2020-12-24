'''
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#id11

Calling a task returns an AsyncResult instance. This can be used to check the state of the task, wait for the task to finish, or get its return value (or if the task failed, to get the exception and traceback).

Results are not enabled by default. In order to do remote procedure calls or keep track of task results in a database, you will need to configure Celery to use a result backend. This is described in the next section.

這裡是送出任務的地方

tasks定義了任務怎麼運作

當前的運算結果是不會回傳的
'''
from tasks import add
import time

async_result = add.delay(4, 4)

method_for_user = [m for m in dir(async_result) if not m.startswith('_')]
method_for_dev = [m for m in dir(async_result) if m not in method_for_user]
print(type(async_result))
print(method_for_user)
print(method_for_dev)
