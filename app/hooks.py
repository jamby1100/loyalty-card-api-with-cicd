import boto3

def pre(event, context):
    print("PRE HOOK")
    print(event)

    lifecycleEventHookExecutionId = event['LifecycleEventHookExecutionId']
    deploymentId = event['DeploymentId']
    deployment_status = 'Succeeded'

    client = boto3.client('codedeploy')

    response = client.put_lifecycle_event_hook_execution_status(
        deploymentId=deploymentId,
        lifecycleEventHookExecutionId=lifecycleEventHookExecutionId,
        status=deployment_status
    )


def post(event, context):
    print("POST HOOK")
    print(event)

    lifecycleEventHookExecutionId = event['LifecycleEventHookExecutionId']
    deploymentId = event['DeploymentId']
    deployment_status = 'Succeeded'

    client = boto3.client('codedeploy')

    response = client.put_lifecycle_event_hook_execution_status(
        deploymentId=deploymentId,
        lifecycleEventHookExecutionId=lifecycleEventHookExecutionId,
        status=deployment_status
    )