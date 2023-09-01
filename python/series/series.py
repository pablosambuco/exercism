def slices(series, length):
    if not length: # if the slice length is zero.
        raise ValueError("slice length cannot be zero")
    if length < 0: # if the slice length is negative.
        raise ValueError("slice length cannot be negative")
    if not series: # if the series provided is empty.
        raise ValueError("series cannot be empty")
    if length > len(series): # if the slice length is longer than the series.
        raise ValueError("slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(len(series)-length+1)]
