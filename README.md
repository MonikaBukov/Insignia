# Insignia

Insignia: A top-down view strategy game where you have to defeat all enemies.

## How to Play

- Use the mouse to move and attack
- Defeat all enemies to win.


## Screenshots
<div style="display: flex; justify-content: center;">
  <img src="https://github.com/MonikaBukov/Insignia/assets/135535997/51c5c074-c481-4626-a667-fdfe8650d0d4" width="400" alt="Image 1">
  <img src="https://github.com/MonikaBukov/Insignia/assets/135535997/50c68a55-1436-40ff-82cd-b7206f336ce0" width="400" alt="Image 2">
</div>

## Demo
[![YouTube Video](https://github.com/MonikaBukov/Insignia/blob/main/data/insigniap.png?raw=true)](https://www.youtube.com/watch?v=qAmLrJ74Jh0)

## More About the Project

This was a group project I was responsible for adding some sounds but mainly for the pathfinding.

https://github.com/MonikaBukov/Insignia/blob/main/game/gameobjects/pathfinding.py

This Python code uses the A* algorithm to find the shortest path between two points on a grid-based map. It efficiently explores neighbouring tiles, maintains cost records, and reconstructs the optimal path from start to finish.

Initialize data structures:

frontier: A priority queue (implemented as a heap) to store tiles to be explored.
visited: A set to keep track of visited tiles.
previous_tile: A dictionary to store the previous tile for each tile in the path.
cost_so_far: A dictionary to store the cost of reaching each tile from the start.
Start with the start_tile, add it to frontier with a cost of 0, and initialize other data structures.

Enter a loop that continues until frontier is empty or the goal is reached:

a. Pop the tile with the lowest cost (current_cost) from frontier.

b. Check if current_tile is the goal; if yes, break out of the loop.

c. Add current_tile to visited to mark it as explored.

d. Generate neighboring tiles (up, down, left, right) of current_tile.

e. For each valid neighbor:

Calculate the cost to reach it (new_cost) via the current tile.
If the neighbor is not in cost_so_far or new_cost is lower than the recorded cost:
Update cost_so_far with the new cost.
Calculate the priority of the neighbor based on new_cost and a heuristic to the goal.
Add the neighbor and its priority to frontier.
Record current_tile as the previous tile for the neighbor.
Once the loop completes, reconstruct the path from goal_tile to start_tile using the previous_tile dictionary.

Return the path as a list of coordinates.

## Technologies Used

- Python
- Pyasge

## License

This project was created solely for a school assignment and is not intended for public release or distribution. All rights to the game and its code belong to the project creators.
