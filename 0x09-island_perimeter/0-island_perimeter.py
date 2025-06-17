#!/usr/bin/python3
"""
Module for calculating island perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid: A list of list of integers where:
              - 0 represents water
              - 1 represents land
              
    Returns:
        Integer representing the perimeter of the island
        
    The function calculates perimeter by checking each land cell
    and counting how many of its sides are exposed to water or
    grid boundaries.
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(rows):
        for j in range(cols):
            # If current cell is land
            if grid[i][j] == 1:
                # Check all 4 adjacent cells
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    # If adjacent cell is outside grid or is water,
                    # it contributes to perimeter
                    if (ni < 0 or ni >= rows or 
                        nj < 0 or nj >= cols or 
                        grid[ni][nj] == 0):
                        perimeter += 1
    
    return perimeter


# Alternative more concise approach
def island_perimeter_alt(grid):
    """
    Alternative implementation using a more direct counting approach.
    
    For each land cell, start with 4 sides and subtract 1 for each
    adjacent land cell (since shared edges don't contribute to perimeter).
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                sides = 4
                
                # Subtract 1 for each adjacent land cell
                # Check up
                if i > 0 and grid[i-1][j] == 1:
                    sides -= 1
                # Check down  
                if i < rows - 1 and grid[i+1][j] == 1:
                    sides -= 1
                # Check left
                if j > 0 and grid[i][j-1] == 1:
                    sides -= 1
                # Check right
                if j < cols - 1 and grid[i][j+1] == 1:
                    sides -= 1
                    
                perimeter += sides
    
    return perimeter
