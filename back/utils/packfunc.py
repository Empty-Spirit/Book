from uuid import uuid4

def getUUid():
    return str(uuid4())

def check_valid_guid(data):
  if ('guid' in data) and data['guid']:
    return data['guid']
  else:
    return False