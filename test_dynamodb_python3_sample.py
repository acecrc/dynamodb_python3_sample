import dynamodb_python3_sample

import unittest
from unittest import mock
from decimal import Decimal

# テスト用クラス
class TestDynamodbPython3Sample(unittest.TestCase):
 
    # 正常系試験
    @mock.patch('dynamodb_python3_sample.table')
    def test_ok_dynamodb_scan(self, table):
        items = [
            {'id': Decimal(1),'done': False,'task': 'タスク'}
        ]
        # DynamoDBから出力されるデータ
        table.scan.return_value = {
            'Items': items
        }
        
        # 期待される結果
        expected = {
            'Items': items
        }
        
        # 試験実施
        actual = dynamodb_python3_sample.dynamodb_scan()
        self.assertEqual(expected, actual)
    
    # 異常系試験
    @mock.patch('dynamodb_python3_sample.table')
    def test_err_dynamodb_scan(self, table):
        # 試験実施
        table.scan.side_effect = Exception('DB Error')
        with self.assertRaises(Exception):
            dynamodb_python3_sample.dynamodb_scan()

if __name__ == '__main__':
    unittest.main()