def check_duplicate(packet: str) -> bool:
    counter = 0
    for check1 in packet:
        for check2 in packet:
            if check1 == check2:
                counter += 1
    if counter > 4:
        return False
    else:
        return True


def find_start_packet(subroutine):
    for i in range(len(subroutine)-4):
        if check_duplicate(subroutine[i:i+4]):
            return i+4


f = open("day6.txt")
print(find_start_packet(f.readline()))
f.close()
