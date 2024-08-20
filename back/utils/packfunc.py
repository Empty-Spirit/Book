from uuid import uuid4

def getUUid():
    return str(uuid4())

def check_valid_guid(data, field):
  if (field in data) and data[field]:
    return data[field]
  else:
    return False