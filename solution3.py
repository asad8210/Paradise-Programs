def count_profitable_segments(profits, segment_size):
    num_segments = len(profits) - segment_size + 1
    profitable_segments = 0
    for i in range(num_segments):
        segment_profit = sum(profits[i:i+segment_size])
        if segment_profit > 0:
            profitable_segments += 1
    return profitable_segments

def min_max_profitable_segments(n, l, h, profits):
    min_profitable_segments = float('inf')
    max_profitable_segments = float('-inf')
    
    for segment_size in range(l, h+1):
        profitable_segments = count_profitable_segments(profits, segment_size)
        min_profitable_segments = min(min_profitable_segments, profitable_segments)
        max_profitable_segments = max(max_profitable_segments, profitable_segments)
    
    return min_profitable_segments, max_profitable_segments

def main():
    n, l, h = map(int, input().split())
    profits = [int(input()) for _ in range(n)]
    min_segments, max_segments = min_max_profitable_segments(n, l, h, profits)
    print(f"{min_segments} {max_segments}")

if __name__ == "__main__":
    n = int(input("Enter the number of days in the books: "))
    l = int(input("Enter the minimum possible choice of segment size: "))
    h = int(input("Enter the maximum possible choice of segment size: "))
    profits = [int(input(f"Enter the profit for day {i+1}: ")) for i in range(n)]
    
    min_segments, max_segments = min_max_profitable_segments(n, l, h, profits)
    print(f"Minimum number of profitable segments: {min_segments}")
    print(f"Maximum number of profitable segments: {max_segments}")
