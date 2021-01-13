import json
import subprocess

def lambda_handler(event, context):
    command(['ls','-la', '/opt/extensions'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }

def command(cmd):
    out = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(out.stdout.decode())