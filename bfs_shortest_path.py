from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city not in visited:
            neighbors = graph.get(city, [])

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(city)

    return None

# --- Real-world application graph (Cities and Roads) ---
city_map = {
    "Lahore": ["Faisalabad", "Multan"],
    "Faisalabad": ["Lahore", "Islamabad"],
    "Multan": ["Lahore", "Karachi"],
    "Islamabad": ["Faisalabad", "Peshawar"],
    "Karachi": ["Multan", "Hyderabad"],
    "Hyderabad": ["Karachi"],
    "Peshawar": ["Islamabad"]
}

# --- Input from user ---
print("🗺️  Welcome to City Route Finder (Using BFS)")
start_city = input("Enter starting city: ").title()
end_city = input("Enter destination city: ").title()

if start_city in city_map and end_city in city_map:
    path = bfs_shortest_path(city_map, start_city, end_city)
    if path:
        print(f"\n✅ Shortest path from {start_city} to {end_city}:")
        print(" ➡️  ".join(path))
        print(f"\n📍 Total Stops: {len(path)-1}")
    else:
        print("\n❌ No path found between the cities!")
else:
    print("\n⚠️ Invalid city names. Please enter from the given map.")
