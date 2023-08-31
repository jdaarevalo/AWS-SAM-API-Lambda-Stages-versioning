# AWS-SAM-API-Lambda-Stages-Versioning

## Overview

This repository provides a robust solution for managing multiple environments and versions in AWS Lambda functions and API Gateway, utilizing the AWS Serverless Application Model (SAM). It's designed to meet the needs of Data Engineers who require flexible, scalable, and maintainable data serving layers.

## Features

- Automates the deployment and management of multiple API Gateway stages and Lambda aliases.
- Provides a pattern for iterative development.
- Allows seamless rollback or progression of API and Lambda function versions.

## Prerequisites

- AWS Account
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/YourUsername/AWS-SAM-API-Lambda-Stages-versioning.git
```

2. Navigate to the project directory:

```bash
cd AWS-SAM-API-Lambda-Stages-versioning
```

3. Deploy using SAM:

```bash
sam deploy --guided
```

## Test locally

One of the big benefits of using SAM is the framework provided for locally testing your applications. Gone are the bad old days of creating test events manually in the AWS Lambda Console!

### Create the virtual environment

```bash
conda create --name py3-10 python=3.10
conda activate py3-10
```

## sam local invoke

```bash
sam build
sam local invoke -e tests/events/event.json
```

## Usage

Once deployed, you can call the API Gateway URL to invoke different versions of the Lambda function based on the stage you specify.

For detailed instructions, please refer to the [blog post](https://aws.plainenglish.io/scalable-data-processing-with-aws-serverless-scatter-gather-pattern-implementation-63d25d6f6d23).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


---

![License](https://img.shields.io/badge/License-MIT-green)