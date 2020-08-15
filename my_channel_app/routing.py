from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from custom_app import consumer
websocket_urlpattern =[
    path('ws/poll-data/',consumer.DashConsumer),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpattern))
})