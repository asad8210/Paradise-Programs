import math

def count_routes(grid_size):
    return math.factorial(2 * grid_size) // (math.factorial(grid_size) * math.factorial(grid_size))

def main():
    grid_size = int(input("Enter the grid size: "))
    result = count_routes(grid_size)
    print("Number of routes through a", grid_size, "x", grid_size, "grid:", result)

if __name__ == "__main__":
    main()
