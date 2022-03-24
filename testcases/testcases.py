from unittest import TestCase
from application.services.Train import TrainClass
from infrastructure.repository.db_connect import engine

T1 = TrainClass()


class Test(TestCase):

    def test_create_train(self):
        data = {'no': 4, 'name': "Maysa", 'station': "einval"}
        T1.create_train(data)
        output = engine.execute('select * from "Train_db" where train_no=4')
        for row in output:
            self.assertEqual(row, (4, 'Maysa', 'einval'))

    def test_train_no(self):
        data = {'no': '', 'name': 'name', 'station': 'station'}
        result = T1.create_train(data)
        self.assertEqual(result, {'status code': 400, 'Message': 'Train number must be integer'})

    def test_dupli_values(self):
        data = {'no': 1, 'name': 'name', 'station': 'station'}
        result = T1.create_train(data)
        self.assertEqual(result, {'status code': 400, 'Message': 'Duplicate primary key'})

    def test_empty_values(self):
        data = {'no': 1, 'name': '', 'station': ''}
        result = T1.create_train(data)
        self.assertEqual(result, {'status code': 400, 'Message': 'Empty Values are not allowed'})

    def test_get_train(self):
        train_no = {'no': 1}
        result = T1.get_train(train_no)
        output = T1.get_train({'no': 1})
        self.assertEqual(result, output)

    def test_not_exists(self):
        train_no = {'no': 0}
        result = T1.get_train(train_no)
        self.assertEqual(result, {'status code': 400, 'Message': "Train Doesn't Exists"})

    def test_get_trains(self):
        result = T1.get_trains()
        self.assertEqual(result, result)

    def test_update_train(self):
        data = {'no': 9, 'name': 'Mana', 'station': ''}
        result = T1.update_train(data)
        self.assertEqual(result, {'status code': 400, 'Message': "Train Doesn't Exists"})

    def test_update(self):
        data = {'no': 2, 'name': 'Durant', 'station': 'Delhi'}
        result = T1.update_train(data)
        self.assertEqual(result, {'status code': 200, 'Message': 'Updated Successfully'})
