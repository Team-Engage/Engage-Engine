from aiohttp import web as _web


class Channels:
  def __init__(self, app, sio):
    self.app = app
    self.sio = sio

  async def home(self, request):
    return _web.Response(text="<a href='/forums'>Chat</a>", content_type="text/html")

  async def forums(self, request):
    return _web.Response(text="Hello, world!")
