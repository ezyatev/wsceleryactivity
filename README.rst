=========
WS Celery Activity
=========

Real time celery active tasks monitoring using websockets. A particular case of `wscelery <https://github.com/johan-sports/wscelery/>`__.

************
Requirements 
************

* Python >= 3.4

************
Installation
************

Development version: ::

    $ pip install https://github.com/ezyatev/wsceleryactivity/zipball/master

*****
Usage
*****

Launch the websocket listener on port 8001: ::

    $ wsceleryactivity --port=8001

Or launch from celery: ::

    $ celery wsceleryactivity -A proj --address=127.0.0.1 --port=8001

Broker URL and other configuration options can be passed through standard Celery options: ::

    $ celery wsceleryactivity -A proj --broker=amqp://guest:guest@localhost:5672//

To see all command options use: ::

    $ wsceleryactivity --help

