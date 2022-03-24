from domain.entities.train_entities import TrainEntity


class TrainFactory:

    @staticmethod
    def train(train_no, name=None, station=None):
        return TrainEntity(train_no, name, station)
