# Завдання 3
# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from heapq import heappop, heappush
from tabulate import tabulate

# Створимо граф, що моделює транспортну мережу Києва з вагами на ребрах
G = nx.Graph()

# Додаємо вершини (райони Києва)
G.add_nodes_from(["Печерський", "Шевченківський", "Оболонський", "Дарницький", "Дніпровський", "Голосіївський", "Подільський", "Деснянський"])

# Додаємо ребра (зв'язки між районами), з вагами (умовними відстанями)
G.add_weighted_edges_from([
    ("Печерський", "Шевченківський", 3),
    ("Печерський", "Оболонський", 5),
    ("Печерський", "Дарницький", 2),
    ("Печерський", "Дніпровський", 4),
    ("Шевченківський", "Подільський", 6),
    ("Оболонський", "Подільський", 4),
    ("Дарницький", "Дніпровський", 1),
    ("Голосіївський", "Дарницький", 7),
    ("Голосіївський", "Подільський", 3),
    ("Деснянський", "Дніпровський", 3),
    ("Деснянський", "Дарницький", 5)
])

# Візуалізуємо граф з вагами
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Алгоритм розташування вузлів для гарної візуалізації
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
plt.title("Транспортна мережа Києва з вагами на ребрах")


# Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів
def dijkstra(graph, start):
    queue = []
    heappush(queue, (0, start))
    shortest_paths = {node: (float('inf'), None) for node in graph}
    shortest_paths[start] = (0, None)

    while queue:
        current_distance, current_node = heappop(queue)

        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, current_node)
                heappush(queue, (distance, neighbor))

    return shortest_paths

# Застосування алгоритму Дейкстри до нашого графа
start_node = "Печерський"
shortest_paths = dijkstra(G, start_node)

# Підготовка результатів для виводу у таблицю
results = []
for node, (distance, predecessor) in shortest_paths.items():
    if node != start_node:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = shortest_paths[current][1]
        path = path[::-1]
        results.append([node, distance, ' -> '.join(path)])

# Створення таблиці з результатами та вивід у консолі
headers = ["Вершина", "Відстань", "Шлях"]
print(tabulate(results, headers=headers, tablefmt="grid", stralign="center"))

plt.show()