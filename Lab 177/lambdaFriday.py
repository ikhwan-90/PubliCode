import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    if event:
        #Fetch and open object
        file_obj = event["Records"][0]
        
        #Filter for filename with spaces
        rawfilename = (str(file_obj['s3']['object']['key'])).split("+")     #Object key name is URL encoded. "file name.jpg" => file+name.jpg
        filename = " ".join(rawfilename)
        
        #Open file with decoded key
        obj = s3.get_object(Bucket='<bucket-name>', Key = filename)
        file_contents = obj["Body"].read().decode('utf-8')
        
        #Count words in file regardless of white spaces
        countWords = str(len(file_contents))
        
        #* Optional - Display for test event
        result = print('The word count in the file ' + str(filename) + ' is ' + str(countWords))
        
        # Send message to SNS
        SNS_ARN = '<topic-ARN>'
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn = SNS_ARN,
            Subject = 'Word Count Result',
            Message = 'The word count in the file ' + filename + ' is ' + countWords
        )
        
    return {
        
    }
