"""
Fox Dono views
"""

import aiohttp
from quart import jsonify
from foxdono import app

MEETUP_ROOT = 'https://api.meetup.com/'

@app.route('/')
async def index():
    """
    Home page response
    """
    return "Hello from Fox Dono, a very special fox"

@app.route('/event/next')
async def next_event():
    """
    Returns details about the next event
    """
    async with aiohttp.ClientSession() as sess:
        url = MEETUP_ROOT + app.config['MEETUP_TAG'] + '/events'
        async with sess.get(url) as resp:
            data = await resp.json()
    return jsonify(data[0] if data else [])

@app.route('/rollcall', methods=['POST'])
async def rollcall():
    return 'Hi there'
