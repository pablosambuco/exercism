def convert(number):
    string = ""
    nums = {3: "Pling", 5: "Plang", 7: "Plong"}
    for k, v in nums.items():
        if number % k == 0:
            string += v
    if not string:
        string = str(number)
    return string
