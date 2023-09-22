def encode(numbers):
    vlq = []
    for number in numbers:
        local_vlq = []
        while number:
            x = number % 2**7
            number //= 2**7
            local_vlq.insert(0, x)
        for i in range(len(local_vlq) - 1):
            local_vlq[i] += 2**7
        vlq.extend(local_vlq or [0])
    return vlq


def decode(bytes_):
    if bytes_[-1] // 2**7:
        raise ValueError("incomplete sequence")

    numbers = []
    number = 0
    for byte in bytes_:
        print(byte, byte // 2**8, byte // 2**7)
        number *= 2**7
        if byte // 2**7 == 1:
            number += byte - 2**7
        else:
            number += byte
            numbers.append(number)
            number = 0
    return numbers
