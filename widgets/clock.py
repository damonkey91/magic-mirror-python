from datetime import datetime
from widgets.base_label import BaseLabel


class Clock(BaseLabel):
    def _update(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.config(text=current_time)
        self.after(1000, self._update)
