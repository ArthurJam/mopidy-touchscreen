import pykka
from mopidy import backend
import logging

logger = logging.getLogger(__name__)

class TouchScreenBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(TouchScreenBackend, self).__init__()
        self.audio = audio
        logger.error("backend funciona")

    def on_receive(self, message):
        action = message['action']
        if action == 'volume':
            self.audio.set_volume(message['value'])
        elif action == "mute":
            self.audio.set_mute(message['value'])
        elif action == "random":
            self.audio.set_random(message['value'])