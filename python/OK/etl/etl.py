def transform(legacy_data):
    new_data = {}
    for key, value  in legacy_data.items():
        for uniq in value:
            new_data[uniq.lower()] = key
    return(new_data)
