import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print(f"value1 {event['key1']}")
    print(f"value2 {event['key2']}")
    print(f"value3 {event['key3']}")
    return f"{event['key1']} {event['key2']} {event['key3']}"   # Echo back the first key value
    #raise Exception('Something went wrong')
