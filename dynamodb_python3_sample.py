import boto3
from boto3.session import Session

# DynamoDBを利用するための準備
session = Session()                         #セッションの作成
dynamodb = session.resource('dynamodb')     #リソースにDynamoDBを選択
table = dynamodb.Table('todos')             #テーブルにtodosを指定

# DynamoDBからtodosの一覧を取得
def dynamodb_scan():
    try:
        results = table.scan()  #todosの一覧を取得
    except:
        raise
    return results

# メイン関数
def main():
    results = dynamodb_scan()   #dynamodb_scan()関数を実行
    print(results)              #取得した結果を表示

if __name__ == '__main__':
    main()                      #メイン関数を実行