import json

import socketio
import toml
from aiohttp import web

from .channels import Channels


class Engage:
  def __init__(self):
    # Webserver
    self.app = web.Application()
    self.sio = socketio.AsyncServer(async_mode="aiohttp")
    self.sio.attach(self.app)

    # Config
    self.settings = {}

  def config(self, o):
    if isinstance(o, dict):
      self.settings = {**self.settings, **o}
    elif isinstance(o, str):
      if o.endswith(".toml"):
        with open(o, "rt") as f:
          self.settings = {**self.settings, **toml.load(f)}
      elif o.endswith(".json"):
        with open(o, "rt") as f:
          self.settings = {**self.settings, **json.load(f)}

  def run(self):
    self.channels = Channels(self.app, self.sio, self.settings)

    self.app.add_routes([
      web.get("/", self.channels.home),
      web.get("/forums", self.channels.forums)
    ])

    web.run_app(self.app)