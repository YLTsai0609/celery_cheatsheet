# Info

[doc](https://docs.celeryproject.org/en/stable/)

[github](https://github.com/celery/celery)

1. pure python
2. Keywords:task, queue, job, async, rabbitmq, amqp, redis, python, distributed, actors
3. distributed(cross machine, process)
4. open source(BSD)
5. communications protocol : AMQP(Advanced Message Queuing Protocol, an application protocol)
6. design pattern : pub-sub 

# Getting start

use dummy job to simulated 

1. one machine / multiple process
2. multiple machine

## Key concept

1. message broker

message broker (訊息中繼站/訊息經紀人) - Which collects the reponse and manages them in a queue. Also makes worker gets their task and tracks the job is done or not. We need a brain to do that. It's Message Broker.

1. RabbitMQ
2. Redis

Here we pick RabbitMQ

2. task assign system - celery

``` Python
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

Celery object

`$1` : name of the current module
`$2` : broker keyword argument(the url of the message broker)

pyamqp://localhost with RabbitMQ

redis://localhost with Redis

define task using `@app.task` with python function

## Installation

1. `rabbitmq-server` or `redis`

   1. Ubuntu/Debian - sudo apt-get install rabbitmq-server
   2. Docker - docker run -d -p 5672:5672 rabbitmq

check your port is open by 

 `netstat -anvp tcp | awk 'NR<3 || /LISTEN/'`

2. `celery`

`pip install celery` - celery only
`pip install "celery[redis]"` - bundle

# Reference

精通Python 第11章 - 並行與網路

[How can I list my open network ports with netstat?](https://apple.stackexchange.com/questions/117644/how-can-i-list-my-open-network-ports-with-netstat)
