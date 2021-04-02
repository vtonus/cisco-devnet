from ncclient import manager

router = {"host": "10.0.20.55", "port": "830", "username": "VandersonKjdy7s3y", "password": "&SBJEwkwis98f7u&2"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
 for capability in m.server_capabilities:
  print('*' * 50)
  print(capability)
 m.close_session()



