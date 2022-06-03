import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    if event:
        print("Event : ", event)
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        
        
        obj = s3.get_object(Bucket='lab177060322', Key = filename)
        file_contents = obj["Body"].read().decode('utf-8')
        countWords = str(len(file_contents))
        result = print('The word count in the file ' + str(filename) + ' is ' + str(countWords))
        
        # Send message to SNS
        SNS_ARN = 'arn:aws:sns:us-west-2:137906345418:lab177topic'
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn = SNS_ARN,
            Subject = 'Lab 177 Challenge',
            Message = 'The word count in the file ' + filename + ' is ' + countWords
        )
        
    return {
        
    }