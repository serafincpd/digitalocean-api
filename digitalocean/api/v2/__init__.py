# coding: utf-8

from .actions import Actions
from .domains import Domains
from .droplets import Droplets
from .images import Images
from .keys import Keys
from .regions import Regions
from .sizes import Sizes


class ClientV2(object):

    def __init__(self, token=None):
        # Probably and example of bad design
        self.actions = Actions(token)
        self.domains = Domains(token)
        self.droplets = Droplets(token)
        self.images = Images(token)
        self.keys = Keys(token)
        self.regions = Regions(token)
        self.sizes = Sizes(token)
