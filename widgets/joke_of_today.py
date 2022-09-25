from widgets.base_label import BaseLabel
from http_requests.joke_of_today import get_joke_of_today
from helpers.constants import TWELVE_HOURS


class JokeOfToday(BaseLabel):
    def _update(self):
        joke = get_joke_of_today()
        self.config(text=joke)
        self.after(TWELVE_HOURS, self._update)
