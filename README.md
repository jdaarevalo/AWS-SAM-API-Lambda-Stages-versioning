# api_gateway_lambda_versioning


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