from datetime import datetime, timedelta, time
from widgets.base_label import BaseLabel


class DayCountDown(BaseLabel):
    def _update(self):
        time_left = self._time_until_end_of_day()
        self.config(text=time_left)
        self.after(1000, self._update)

    @staticmethod
    def _time_until_end_of_day(dt=None):
        if dt is None:
            dt = datetime.now()
        tomorrow = dt + timedelta(days=1)
        time_left = datetime.combine(tomorrow, time.min) - dt
        return str(time_left).split('.', 2)[0]
