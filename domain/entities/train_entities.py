class TrainEntity:
    def __init__(self, train_no: int, name: str, station: str):
        self.train_no = train_no
        self.name = name
        self.station = station

    def to_dict(self):
        return {
            "Train no": self.train_no,
            "Name": self.name,
            "Station": self.station

        }
