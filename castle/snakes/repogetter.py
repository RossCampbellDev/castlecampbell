#!/usr/bin/python3
import json
import subprocess

subprocess.call('curl -H "Authorization: token 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" https://api.github.com/user/repos > repos.json', shell=True)

with open('repos.json') as f:
	repodata = json.load(f)

repos = []

for item in repodata:
	if not item['private']:
		data = {'title': item['name'], 'url': item['html_url'], 'desc': item['description']}
		repos.append(data)
	# print(item['full_name'] + ' ' + item['html_url'])

all_data = json.dumps(repos)

for repo in repos:
	line = "<div class=gitline><div class=gitlineinner><h3>{title}</h3><a href='{url}' target=_blank>github</a><p>{desc}</p></div></div>".format(title=repo['title'], url=repo['url'], desc=repo['desc'])
	print(line)
