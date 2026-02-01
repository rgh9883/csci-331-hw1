import sys
from collections import deque


# alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def get_neighbors(word: str, word_list: list[str]):
    neighbors = []
    for node in word_list:
        total_diff = 0
        for i in range(len(word)):
            if node[i] != word[i]:
                total_diff += 1
        if total_diff == 1:
            neighbors.append(node)
    return neighbors

def bfs_traversal(start, end, word_list):
    queue = deque()
    parent = dict()
    visited = set()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node, word_list):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == end:
                    return parent
    return parent

def build_path(start, end, parent):
    path = [end]
    cur_word = end
    while cur_word != start:
        cur_word = parent[cur_word]
        path.insert(0, cur_word)
    return path

if __name__ == "__main__":
    words_file = sys.argv[1]
    start_str = sys.argv[2]
    target_str = sys.argv[3]
    pos_words = []
    with open(words_file, "r") as f:
        for line in f:
            word = line.strip()
            if len(word) == len(start_str):
                pos_words.append(word)
    parent = bfs_traversal(start_str, target_str, pos_words)
    if target_str not in parent:
        print("No solution")
        sys.exit()
    path = build_path(start_str, target_str, parent)
    for word in path:
        print(word)
            
