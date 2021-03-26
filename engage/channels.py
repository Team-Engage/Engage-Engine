from aiohttp import web
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
  loader = PackageLoader("engage", "data"),
  autoescape = select_autoescape(["html", "xml"])
)

class Channels:
  def __init__(self, app, sio, settings):
    self.app = app
    self.sio = sio
    self.settings = settings

  async def home(self, request):
    return web.Response(text="<a href='/forums'>Forums</a>", content_type="text/html")

  async def forums(self, request):
    template = env.get_template("forums.html")
    return web.Response(text=template.render(site=self.settings["site"]), content_type="text/html")
