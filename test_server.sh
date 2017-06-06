trap 'kill $(jobs -p)' EXIT

./venv/bin/python server_websockets.py &

./venv/bin/python server_aiohttp.py &

./venv/bin/python server_aiohttp_uvloop.py &

./venv/bin/python server_tornado.py &

docker run -it --rm \
    -v ${PWD}/config:/config \
    -v ${PWD}/reports:/reports \
    --net host \
    --name fuzzingserver \
    crossbario/autobahn-testsuite \
    wstest --mode fuzzingclient --spec /config/fuzzingclient.json
