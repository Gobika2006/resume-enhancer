import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "Resume analyzed successfully",
            "score": 85,
            "suggestions": [
                "Add more technical skills",
                "Improve summary section",
                "Include projects with AWS"
            ]
        })
    }
