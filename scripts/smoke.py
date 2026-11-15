#!/usr/bin/env python3
"""Create community/post only once at boot; strictly verify after upgrade/redeploy."""
import hashlib,json,os,pathlib,secrets,urllib.request,urllib.error,urllib.parse
b=os.environ['BASE_URL'].rstrip('/');phase=os.environ['SMOKE_PHASE']
assert phase in ('boot','upgrade','redeploy'),'unknown phase'
p=pathlib.Path(__file__).with_name('state-'+hashlib.sha256(b.encode()).hexdigest()[:20]+'.json')
def api(path,body=None,jwt=None,expected=(200,)):
 headers={'Content-Type':'application/json','Accept':'application/json'}
 if jwt:headers['Authorization']='Bearer '+jwt
 req=urllib.request.Request(b+'/api/v3/'+path,data=None if body is None else json.dumps(body).encode(),headers=headers)
 try:r=urllib.request.urlopen(req,timeout=60)
 except urllib.error.HTTPError as e:r=e
 with r:
  assert r.code in expected,f'API {path} status {r.code}'
  return json.loads(r.read())
assert 'site_view' in api('site'),'site API shape'
creds={'username_or_email':os.environ['ADMIN_USERNAME'],'password':os.environ['ADMIN_PASSWORD']}
jwt=api('user/login',creds)['jwt']
api('user/login',{**creds,'password':'wrong-'+creds['password']},expected=(400,401,403))
if not p.exists():
 assert phase=='boot','missing boot state; refusing to recreate durable data'
 marker='rtv'+secrets.token_hex(6)
 community=api('community',{'name':marker,'title':marker,'description':'Isolated validation community'},jwt)['community_view']['community']['id']
 post=api('post',{'community_id':community,'name':marker,'body':'Durable validation record '+marker},jwt)['post_view']['post']['id']
 tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps({'marker':marker,'community':community,'post':post}));tmp.chmod(0o600);tmp.replace(p)
s=json.loads(p.read_text())
post=api('post?'+urllib.parse.urlencode({'id':s['post']}),jwt=jwt)['post_view']['post']
assert post['name']==s['marker'],'post title changed';assert post['body']=='Durable validation record '+s['marker'],'post body changed';assert post['community_id']==s['community'],'post association changed'
community=api('community?'+urllib.parse.urlencode({'id':s['community']}),jwt=jwt)['community_view']['community']
assert community['name']==s['marker'] and community['title']==s['marker'],'community missing or changed'
print(json.dumps({'phase':phase,'check':'stored-community-and-post','ok':True}))
