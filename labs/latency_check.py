from __future__ import print_function
from operator import itemgetter
import subprocess


host = [["us-east-1","23.23.255.255",0],["us-east-2","13.58.0.253",0],["us-west-1","13.52.0.2",0],["us-west-2","34.208.63.251",0],["us-gov-west-1","52.61.0.254",0],["ca-central-1","35.182.0.251",0],["sa-east-1","18.231.0.252",0],["eu-west-1","34.240.0.253",0],["eu-central-1","18.194.0.252",0],["eu-west-2","35.176.0.252",0],["eu-west-3","52.47.32.127",0],["ap-northeast-1","13.112.63.251",0],["ap-northeast-2","13.124.63.251",0],["ap-southeast-1","13.228.0.251",0],["ap-southeast-2","13.54.63.252",0],["ap-south-1","13.126.0.252",0],["cn-north-1","52.80.5.207",0],["cn-northwest-1","52.83.214.0",0]]

for i in range(len(host)):
	ping = subprocess.Popen(
        ["ping", "-c", "3", host[i][1]],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
	out, error = ping.communicate()
	count=0
	ans=""
	for index in range(len(out)):
		if count>4:
			break
		if out[index]=="/":
			count=count+1
			continue
		if count==4:
			ans=ans+out[index]


	host[i][2]=float(ans)

print(sorted(host, key=itemgetter(2)))
