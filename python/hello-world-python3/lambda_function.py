import json
import requests

print('Loading function')

# def lambda_handler(event, context):
#     print("Received event: " + json.dumps(event, indent=2))
#     print(f"value1 {event['key1']}")
#     print(f"value2 {event['key2']}")
#     print(f"value3 {event['key3']}")
#     return f"Key values => {event['key1']} {event['key2']} {event['key3']}"   # Echo back the first key value
#     #raise Exception('Something went wrong')


def lambda_handler(event, context):
    response = "Something went wrong... check the logs!"
    try:
        url = 'https://gorest.co.in/public/v1/posts'
        response = requests.get(url)
        print(f'response: {response.json()}')
    except Exception as e:
        print("ERROR: Unexpected error... {}".format(e))

    return response.json()