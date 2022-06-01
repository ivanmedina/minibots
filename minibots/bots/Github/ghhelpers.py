from requests import Response
from tabulate import tabulate
from minibots import ghrepository
from minibots import ghuser

reposHeaders=[ 'id', 'name', 'description', 'url', 'size', 'clone_url' ]

def requestToGHUser (resp:Response)->ghuser:
    if resp.status_code == 200:
        _user = resp.json()
        return ghuser( _user['id'], _user['login'], _user['html_url'], _user['avatar_url'] )
    return ghuser( 0,'','','' )

def requestToRepos (resp:Response)->list[ghrepository]:
    if resp.status_code == 200:
        _repos = resp.json()
        return [ ghrepository( _r['id'], _r['name'], _r['description'], _r['url'], _r['size'], _r['clone_url']) for _r in _repos ]
    return []

def requestToArray ( key:str, resp:Response )->list[str]:
    if resp.status_code == 200:
        _follows = resp.json()
        return [ x[key]  for x  in _follows ]
    return []

def arrayReposToArrayDicts(repos:list[ghrepository])->list[dict]:
    return [ _r.__dict__ for _r in repos ]

def tableRepos(repos:list[dict])->str:
    for _r in range(len(repos)):
        for k, v in repos[_r].items():
            if not str(v).isnumeric() and isinstance(v, str) and v is not None and k == 'description':
                repos[_r][k]=v[:30]
    return tabulate(repos,headers='keys',tablefmt="grid")