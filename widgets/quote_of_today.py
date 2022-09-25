from widgets.base_label import BaseLabel
from http_requests.quote_of_today import get_quote_of_today
from helpers.constants import TWELVE_HOURS


class QuoteOfToday(BaseLabel):
    def _update(self):
        joke = get_quote_of_today()
        self.config(text=joke)
        self.after(TWELVE_HOURS, self._update)
