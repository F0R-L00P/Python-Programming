from collections import namedtuple
from github import Github, InputFileContent

# build github object
gh = Github()
# check object
print(gh)

# check rate limits of calls per hour without author
# default is 60 calls per 60 minutes
print(gh.rate_limiting)

# setup user
loop = gh.get_user('stepthom')
print(loop)

# HELP
# can use help to obtain all class information and urls
help(loop)

# use dir to obtain all methods
# use methods on object
dir(loop)
print(loop.location)
print(loop.followers)
print(loop.html_url)
print(loop.repos_url)
print(loop.followers_url)

# you can also call help on a method
help(loop.get_repos)

# api response = PaginatedList
loop.get_repos()

# build namedtuple
Repo = namedtuple('Repo', ['name', 'stars', 'forks'])

# write method to get repo stats
def get_repo_stats(user, n=5):

    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue
        
        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))
    
    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]

get_repo_stats(loop, n=10)

# =============================================================================
# Using TOKEN
# =============================================================================

TOKEN = 'YOUR_TOKEN'

# setup user with toke,
gh = Github(TOKEN)
print(gh)

# check rate limit, this should have increased to 5000 counts from 60
print(gh.rate_limiting)

# user is now a Authenticated user
loop = gh.get_user()
print(loop)

# lets use the helpfunction to identify gists POST
help(loop.create_gist)

