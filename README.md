# s3-monitor

Code repo responsible for doing the below when a file/files are uploaded to S3 bucket.


* Validate the file extension to be pdf only
* Rename the file by appending a timestamp to the name
* Move this file to a different folder in the same bucket

The code base is written in serverless + lambda + python.

## File Details
#### env.dev.json
This file carries the environment variables for lambda based on environment in json format. For adding another environment. Just add another file with the name of the format env-<environment>.json and update the stage field in serverless.yaml file to the corresponding environment name.

#### handler.py
Simple python code to validate the file based on extension and delete it if not having the extension .pdf and copy it to the folder /updated if matches the criteria with timestamp appended to the filename and then delete the actual file.

#### serverless.yml
Key file to build the infrastructure which have Lambda function, IAM role for lambda, Cloudwatch log group, S3 bucket to store the artifactory.

## How to run the code
Use serverless command to run the projects.

```serverless deploy -v```

Bucketname to be monitored, AWS region name and Environment name based on the env json file needs to be updated before running the command.

```serverless remove -v```

Above command to delete the infrastructure if not needed.
