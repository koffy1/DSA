# Breadth first search implementation

from collections import deque

graph = {}
graph["kofo"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["tom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["tom"] = []
graph["jonny"] = []

def isMangoSeller(name):
    if name[-1] == "m":
        return True
        
def searchGraph(graph):
    searchQueue = deque()
    searchQueue += graph["kofo"]
    searched = {}
    while searchQueue:
        name = searchQueue.popleft()
        if searched.get(name):
            continue
        if isMangoSeller(name):
            return name
        searched[name] = True
        searchQueue += graph[name]
    return False
    
print(searchGraph(graph))
    