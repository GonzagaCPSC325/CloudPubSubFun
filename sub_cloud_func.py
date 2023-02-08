import base64

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message[:100]) # I've found that when the
    # messages are really long they sometimes don't end up 
    # in the logs
    # TODO: insert pubsub_message as a big query row
    # the code to do this in CloudFunctionFun