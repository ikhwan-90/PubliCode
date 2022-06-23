import json
import boto3
from urllib.parse import unquote_plus

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    if event:
        #Fetch object Key (Filename)
        file_obj = event["Records"][0]
        
        #Filter for filename with spaces
	#Object key name is URL encoded. For spaces, "file name.jpg" => file+name.jpg. Need to decode with unquote_plus
        rawfilename = str(file_obj['s3']['object']['key'])
        filename = unquote_plus(rawfilename)
                
        #Open object with decoded key
        try:
            obj = s3.get_object(Bucket='<S3-Bucket-Name>', Key = filename)
        except:
            print("The file with that name is not found in S3.")
        file_contents = obj["Body"].read().decode('utf-8')
        
        #Count words in file regardless of white spaces
        countWords = str(len(file_contents))
        
        #* Optional - Display for test event
        result = print('The word count in the file ' + '"' + filename + '"' + ' is ' + countWords)
        
        # Send message to SNS
        SNS_ARN = '<Topic-ARN>'
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn = SNS_ARN,
            Subject = 'Word Count Result',
            Message = 'The word count in the file ' + '"' + filename + '"' + ' is ' + countWords
        )
        
    return
