from widgets.base_label import BaseLabel
from http_requests.dad_jokes import get_dad_jokes
from helpers.constants import *
from helpers.widget_kwargs_functions import extract_refresh_rate


class DadJokes(BaseLabel):
    def __init__(self, *args, **kwargs):
        self.refresh_rate = extract_refresh_rate(kwargs, TWENTY_FOUR_HOURS)
        super().__init__(*args, **kwargs)

    def _update(self):
        joke = get_dad_jokes()
        self.config(text=joke)
        self.after(self.refresh_rate, self._update)
