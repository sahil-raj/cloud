import boto3
import botocore

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Corrected region name
    instance_id = "i-0cb771a7775f3909f"  # Replace with your EC2 Instance ID

    try:
        response = ec2.stop_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': f"Stopping instance {instance_id}. Response: {response}"
        }

    except botocore.exceptions.ClientError as e:
        return {
            'statusCode': 400,
            'body': f"Error stopping instance {instance_id}: {str(e)}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"An unexpected error occurred: {str(e)}"
        }
