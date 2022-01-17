from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_patterns


application = ProtocolTypeRouter({
    'websockt': AuthMiddlewareStack(
        URLRouter(
            websocket_patterns
            )
    ),
})