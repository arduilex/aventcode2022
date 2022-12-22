def check_duplicate(packet: str)->bool:
    counter = 0
    for check1 in packet:
        for check2 in packet:
            if check1==check2:
                counter += 1
    if counter>len(packet):
        return False
    else:
        return True

def find_start_packet(subroutine, size: int)->int:
    for i in range(len(subroutine)-size):
        if check_duplicate(subroutine[i:i+size]):
            return i+size

f = open("day6.txt")
message = f.readline()
print(find_start_packet(message, 14))
f.close()