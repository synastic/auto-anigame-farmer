###edit the following
server_id=''#copy ur channelid here (use developer mode and leftclick on channel and click copy)
channelid=''#copy ur channelid here (use developer mode and leftclick on channel and click copy)
token= ""#paste ur token here u can search on how to get it on youtube it comes with " so remove them and makse sure ur token doesnt end up like ""token"" it should be like "token"
###dont touch anything below here
from commands import *
async def start ():
  if token == '':
    print('please paste a token or read readme.md ')
  if channelid == '':
    print('please paste a channel id or read readme.md ')
  if server_id == '':
    print('please paste a server or read readme.md ')
  else :
    method = input('what would u like to do today: \n raid \n bt all \n lottery \n hourly \n ')
    try:
      code = lib[method]
    except:
      print('please enter a valid input devoid of excess spaces etc.')
    try:
      await run(code,token,channelid)
    except:
      print('an error occured while running your code')
        
loop = asyncio.get_event_loop()
loop.run_until_complete(start())
loop.close()
