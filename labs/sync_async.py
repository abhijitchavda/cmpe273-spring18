import requests
import asyncio
import sys
from aiohttp import ClientSession

url=sys.argv[3]
no=sys.argv[2]
typ=sys.argv[1]

if typ=='sync':
	for y in range(1,int(no)+1):
		res=[
		requests.get(url,params={'request':y})
		for y in range(1,int(no)+1)
		]

	for response in res:
		print(str(response.content)+' response from '+str(response.url))




if typ=='async':
	counts=[]
	async def asynccall(url,y):
		async with ClientSession() as sess:
			async with sess.get(url) as res:
				res=await res.read()
				print(str(res)+'--->request'+str(y))

	for y in range(1,int(no)+1):
		count=asyncio.ensure_future(asynccall(url,y))
		counts.append(count)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait(counts))
