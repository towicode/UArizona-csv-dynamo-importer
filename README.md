
# CSV to DynamoDB

provides a S3 Bucket and code to translate that to a DynamoDB 

## Deploy

In order to deploy the you endpoint simply run

```bash
serverless deploy
```

The expected result should be similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service ua-aws-handler-2020.zip file to S3 (2.7 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
........................
Serverless: Stack update finished...
Service Information
service: ua-aws-handler-2020
stage: dev
region: us-east-1
stack: ua-aws-handler-2020-dev
resources: 9
api keys:
  None
endpoints:
  None
functions:
  mys3trigger: ua-aws-handler-2020-dev-mys3trigger
layers:
  Nonee
```


## Scaling

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).
