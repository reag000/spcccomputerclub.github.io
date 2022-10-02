import csv
import sys
from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding `person_id`s
names = {}

# Maps `person_id`s to a dictionary of: `name`, `birth`, `movies`
people = {}

# Maps `movie_id`s to a dictionary of: `title`, `year`, `stars`
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    # degrees.py is in the same directory where [directory] is placed
    # [directory]: 'large' | 'small'
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    # Initialises data structures: names, peoples, movies
    load_data(directory)
    print("Data loaded.")

    # Find shortest path between source and target which are `person_id`s
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    # Solve
    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    class Network:
        def __init__(self, source, target):
            self._source = source
            self._target = target
            self._start = Node(self._source, None, None)
            self._frontier = QueueFrontier()
            self._frontier.add(self._start)
            self._explored = set()
            self._solution = []

        def solve(self):
            while True:
                if self._frontier.empty():
                    return None
                node = self._frontier.remove()
                
                if node in self._explored:
                    continue
                
                if node.state == self._target:
                    while node.parent is not None:
                        self._solution.append((node.action, node.state))
                        node = node.parent
                    self._solution.reverse()
                    break

                self._explored.add(node)
                neighbors = neighbors_for_person(node.state)
                for movie_id, person_id in neighbors:
                    if person_id == node.state:
                        continue
                    sussecor_node = Node(person_id, node, movie_id)
                    if self._frontier.contains_state(person_id) or sussecor_node in self._explored:
                        continue
                    self._frontier.add(sussecor_node)
            return self._solution

    n = Network(source, target)
    return n.solve()

def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
