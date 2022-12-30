from collections import deque


def breadthSearch(graph, start):
    search_queue = deque()
    search_queue += graph[start]
    checked = []

    while search_queue:
        person = search_queue.popleft()
        if not person in checked:
            if wantedPerson(person):
                print(person + " is wanted!")
                return True
            else:
                search_queue += graph[person]
                checked.append(person)
    return False


def wantedPerson(name):
    return name[-1] == "k"


if __name__ == "__main__":
    myGraph = {
        "you": ["bill", "jobs", "musk"],
        "bill": ["ballmer", "wozniak"],
        "jobs": ["wozniak"],
        "musk": ["bezos", "dorsey"],
        "ballmer": [],
        "wozniak": [],
        "bezos": [],
        "dorsey": []
    }

    print("Breadth search in our graph: " + str(breadthSearch(myGraph, "you")))
