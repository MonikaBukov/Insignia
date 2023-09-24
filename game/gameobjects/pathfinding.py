import pyasge
from game.gamedata import GameData
import math


import heapq


def heuristic(node, goal):
    dx = node[0] - goal[0]
    dy = node[1] - goal[1]
    return math.sqrt(dx * dx + dy * dy)


def distance_in_tiles(start, goal, data: GameData):
    start_tile = data.game_map.tile(start)
    goal_tile = data.game_map.tile(goal)
    dx = abs(start_tile[0] - goal_tile[0])
    dy = abs(start_tile[1] - goal_tile[1])
    distance = dx + dy
    return distance


def resolve(end_pos, data: GameData, start_pos):
    start_tile = data.game_map.tile(pyasge.Point2D(start_pos.sprite.x, start_pos.sprite.y))
    goal_tile = data.game_map.tile(end_pos)

    # use these to make sure you don't go out of bounds when checking neighbours
    map_width = data.game_map.width
    map_height = data.game_map.height
    start_cost = data.game_map.costs[start_tile[1]][start_tile[0]]

    goal_cost = data.game_map.costs[goal_tile[1]][goal_tile[0]]

    if not (0 <= start_tile[0] < map_width and 0 <= start_tile[1] < map_height):
        return []

    # if either the start or goal position is not walkable, return an empty path
    if start_cost > 1 or goal_cost > 1:
        return []

    frontier = []
    heapq.heappush(frontier, (0, start_tile))
    visited = set()
    previous_tile = {start_tile: None}
    cost_so_far = {start_tile: 0}

    while frontier:
        current_cost, current_tile = heapq.heappop(frontier)
        if current_tile == goal_tile:
            break

        visited.add(current_tile)
        neighbours = [(current_tile[0] - 1, current_tile[1]), (current_tile[0] + 1, current_tile[1]),
                      (current_tile[0], current_tile[1] - 1), (current_tile[0], current_tile[1] + 1)]

        for neighbour in neighbours:
            if neighbour not in visited:
                if 0 <= neighbour[0] < map_width and 0 <= neighbour[1] < map_height:
                    neighbor_cost = data.game_map.costs[neighbour[1]][neighbour[0]]
                    if neighbor_cost <= 1:
                        new_cost = cost_so_far[current_tile] + neighbor_cost
                        if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                            new_cost = cost_so_far[current_tile] + neighbor_cost
                            priority = new_cost + heuristic(goal_tile, neighbour)
                            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                                cost_so_far[neighbour] = new_cost
                                heapq.heappush(frontier, (priority, neighbour))
                                previous_tile[neighbour] = current_tile

    path = []
    current_tile = goal_tile
    while current_tile != start_tile:
        path.insert(0, data.game_map.world(current_tile))
        current_tile = previous_tile[current_tile]

    return path

