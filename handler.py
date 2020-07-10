import json
import datetime
import boto3
import csv

TABLE_NAME = "ua-dynamodb-storage-2020"

def endpoint(event, context):

    region='us-east-1'
    recList=[]

    s3 = boto3.client('s3')   
    dyndb = boto3.client('dynamodb', region_name=region)

    for record in event['Records']:
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']
        bucket = record['s3']['bucket']['name']
        if size > 0:
            # do your stuff here
            confile = s3.get_object(Bucket=bucket, Key=key)
            recList = confile['Body'].read().split('\n')
            firstrecord=True
            csv_reader = csv.reader(recList, delimiter=',', quotechar='"')
            for row in csv_reader:
                if (firstrecord):
                    firstrecord=False
                    continue
                sample_id = row[0]
                net_id = row[1].replace(',','') if row[1] else '-'
                test_date = row[2].replace(',','') if row[2] else '-'
                test_type = row[3].replace(',','') if row[3] else '-'
                test_results = row[4].replace(',','') if row[4] else '-'
                sample_status = row[5].replace(',','') if row[5] else '-'
                notification_message = row[6].replace(',','') if row[6] else '-'

                response = dyndb.put_item(
                    TableName=TABLE_NAME,
                    Item={
                    'sample_id' : {'S':sample_id},
                    'net_id': {'S':net_id},
                    'test_date': {'S':test_date},
                    'test_type': {'S':test_type},
                    'test_results': {'S':test_results},
                    'sample_status': {'S':sample_status},
                    'notification_message': {'S':notification_message},
                    }
                )
            print('Put succeeded:')


    body = {
        "message": "OK"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
