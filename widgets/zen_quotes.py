from widgets.base_label import BaseLabel
from http_requests.zen_quotes import get_zen_quote, joke_type_enum
from helpers.constants import *
from helpers.widget_kwargs_functions import extract_refresh_rate


class ZenQuotes(BaseLabel):
    def __init__(self, *args, **kwargs):
        self.joke_type = joke_type_enum.RANDOM
        self.refresh_rate = extract_refresh_rate(kwargs, TWENTY_FOUR_HOURS)
        super().__init__(*args, **kwargs)

    def set_joke_type(self, type: joke_type_enum):
        self.joke_type = type

    def _update(self):
        joke = get_zen_quote(self.joke_type)
        self.config(text=joke)
        self.after(self.refresh_rate, self._update)
