import sys
from githubbot import GithubBot
from githubrepository import GithubRepository
from minibots import requestsGithub
from ghhelpers import *

resource="https://api.github.com"
auth={}
repositorio=GithubRepository()
req = requestsGithub( repositorio, resource )
bot=GithubBot( resource, auth, req )

def printOptions(_program_name):
    print(f'Usage: {_program_name} <action> [ <attribute1> <attribute2>... ]  ')
    print(f'Actions: ')
    print(f'[1] Get User -> attribute1 = username ')
    print(f'[2] Get Followers -> attribute1 = username ')
    print(f'[3] Get Follows -> attribute1 = username ')
    print(f'[4] Get Repositories -> attribute1 = username ')

def printExamples(_program_name):
    print(f'Examples: ')
    print(f'[1] Get User ->  {_program_name} 1 <username>' )
    print(f'[2] Get Followers -> {_program_name} 2 <username>' )
    print(f'[3] Get Follows -> {_program_name} 3 <username> ')
    print(f'[4] Get Repositories -> {_program_name} 4 <username> ')

def printHelp(_program_name):
    printOptions(_program_name)
    printExamples(_program_name)

def option1(bot, username):
    user = bot.getUser(username)
    print(user)

def option2(bot, username):
    followers = bot.getFollowersByUserName(username)
    followers = ''.join( _f+'\n' for _f in followers)
    print(followers)

def option3(bot, username):
    follows = bot.getFollowsByUserName(username)
    follows = ''.join( _f+'\n' for _f in follows)
    print(follows)

def option4(bot, username):
    repos = bot.getUserRepos(username)
    repos = tableRepos(arrayReposToArrayDicts(repos))
    print(repos)

def __main__():
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    count = len(arguments)
    
    options = {
        1 : option1,
        2 : option2,
        3 : option3,
        4 : option4
    }

    try:
        options[int(arguments[0])](bot,arguments[1])
    except:
        printHelp(program_name)

if __main__:
    __main__()