# Завдання 2
# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.
# Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створимо граф, що моделює транспортну мережу Києва
# Вершини представляють певні райони, а ребра - транспортні зв'язки між ними
G = nx.Graph()

# Додаємо вершини (райони Києва)
G.add_nodes_from(["Печерський", "Шевченківський", "Оболонський", "Дарницький", "Дніпровський", "Голосіївський", "Подільський"])

# Додаємо ребра (зв'язки між районами)
G.add_edges_from([
    ("Печерський", "Шевченківський"),
    ("Печерський", "Оболонський"),
    ("Печерський", "Дарницький"),
    ("Печерський", "Дніпровський"),
    ("Шевченківський", "Подільський"),
    ("Оболонський", "Подільський"),
    ("Дарницький", "Дніпровський"),
    ("Голосіївський", "Дарницький"),
    ("Голосіївський", "Подільський")
])

# Візуалізуємо граф
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Алгоритм розташування вузлів для гарної візуалізації
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа Києва")
plt.text(0, -1.1, "Цей граф представляє модель транспортних зв'язків між районами Києва.\nВершини графу - це райони, а ребра - транспортні маршрути між ними.", fontsize=12, ha='center')

# Додаємо підсумки на графік
plt.text(-1.5, -1.3, f"Кількість вершин (районів): {G.number_of_nodes()}\nКількість ребер (зв'язків): {G.number_of_edges()}", fontsize=12, ha='left')

plt.show()

# Аналіз основних характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин (районів): {num_nodes}")
print(f"Кількість ребер (зв'язків): {num_edges}")
print("Ступінь кожної вершини (кількість зв'язків для кожного району):")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")

# Алгоритм DFS для знаходження шляху у графі
def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return path

# Алгоритм BFS для знаходження шляху у графі
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return path

# Застосуємо алгоритми до нашого графу
start_node = "Печерський"
dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("\nРезультати виконання алгоритму DFS:")
print(" -> ".join(dfs_path))

print("\nРезультати виконання алгоритму BFS:")
print(" -> ".join(bfs_path))

# Порівняння результатів
print("\nПорівняння шляхів, знайдених алгоритмами DFS і BFS:")
print(f"DFS шлях: {' -> '.join(dfs_path)}")
print(f"BFS шлях: {' -> '.join(bfs_path)}")

print("\nРізниця між алгоритмами полягає в підході до пошуку: DFS використовує глибину (рухається глибше, доки можливо), тоді як BFS використовує ширину (перевіряє всі сусідні вузли на кожному рівні перед переходом далі). Через це DFS може знайти шлях, що проходить через довші гілки, тоді як BFS знаходить найкоротший шлях у термінах кількості ребер.")