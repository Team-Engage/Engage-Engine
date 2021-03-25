import json as _json

import socketio as _socketio
import toml as _toml
from aiohttp import web as _web

from .channels import Channels


class Engage:
  def __init__(self):
    # Webserver
    self.app = _web.Application()
    self.sio = _socketio.AsyncServer(async_mode="aiohttp")
    self.sio.attach(self.app)
    self.channels = Channels(self.app, self.sio)

    # Config
    self.settings = {}

  def config(
    self,
    dictionary = None,
    toml = None,
    json = None
  ):
    if isinstance(dictionary, dict):
      self.settings = {**self.settings, **dictionary}
    elif isinstance(toml, str) and toml.endswith(".toml"):
      with open(toml, "rt") as f:
        self.settings = {**self.settings, **_toml.load(f)}
    elif isinstance(json, str) and json.endswith(".json"):
      with open(json, "rt") as f:
        self.settings = {**self.settings, **_json.load(f)}

  def run(self):
    self.app.add_routes([
      _web.get("/", self.channels.home),
      _web.get("/forums", self.channels.forums)
    ])

    _web.run_app(self.app)