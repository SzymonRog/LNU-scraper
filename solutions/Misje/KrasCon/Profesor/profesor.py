def check_connection(przystanek_a, przystanek_b, polaczenia):
    visited = set()
    stack = [przystanek_a]

    while stack:
        current = stack.pop()
        if current == przystanek_b:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in polaczenia.get(current, []):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return False
