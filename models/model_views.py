class View:
    def __init__(self, **kwargs):
        self.id = kwargs["view_id"] if kwargs["view_id"] else None
        self.time = kwargs["time"] if kwargs.get("time") else None
        self.link_id = kwargs["link_id"] if kwargs.get("link_id") else None