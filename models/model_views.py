import datetime

class View:
    def __init__(self, **kwargs):
        self.id = kwargs["url_id"] if kwargs["url_id"] else None
        self.time = kwargs["hour_time"] if kwargs.get("hour_time") else datetime.now()
        self.count = kwargs["count"] if kwargs.get("count") else None