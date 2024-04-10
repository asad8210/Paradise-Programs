def read_input():
    n = int(input())
    customers = []
    for _ in range(n):
        a, b = map(int, input().split())
        customers.append((a, b))
    return customers

def allocate_rooms(customers):
    customers.sort()
    rooms = []
    room_assignment = {}
    room_number = 1
    for customer in customers:
        assigned = False
        for room in rooms:
            if room[-1][1] < customer[0]:
                room.append(customer)
                room_assignment[customer] = room_number
                assigned = True
                break
        if not assigned:
            rooms.append([customer])
            room_assignment[customer] = room_number
            room_number += 1
    return len(rooms), room_assignment

def main():
    customers = read_input()
    min_rooms, room_assignment = allocate_rooms(customers)
    print(min_rooms)
    for customer in customers:
        print(room_assignment[customer], end=' ')

if __name__ == "__main__":
    main()
