def measure(bucket_one, bucket_two, goal, start_bucket):
    actions = {"one": 0, "two": 0}

    buckets = [start_bucket, "one" if start_bucket == "two" else "two"]

    maxs = {"one": bucket_one, "two": bucket_two}
    state = {"one": 0, "two": 0}

    def print_status(action=None):
        nonlocal state, maxs, actions, buckets
        print(
            (f"{action}\n" if action else "")
            + f"Max Capacity:  {maxs}    \n"
            + f"Current State: {state}   \n"
            + f"Actions:       {actions} \n"
            + f"Buckets:       {buckets} \n"
        )

    def switch():
        nonlocal buckets
        buckets[0], buckets[1] = buckets[1], buckets[0]
        print_status("Switch")

    def pour():
        nonlocal state, maxs, actions, buckets
        volume = 0
        available = maxs[buckets[1]] - state[buckets[1]]
        if available:
            actions[buckets[0]] += 1
        volume = min(state[buckets[0]], available)
        state[buckets[0]] -= volume
        state[buckets[1]] += volume
        print_status("Pour")

    def empty():
        nonlocal state, actions, buckets
        if state[buckets[0]]:
            actions[buckets[0]] += 1
        state[buckets[0]] = 0
        print_status("Empty")

    def fill():
        nonlocal state, maxs, actions, buckets
        if maxs[buckets[0]] - state[buckets[0]]:
            actions[buckets[0]] += 1
        state[buckets[0]] = maxs[buckets[0]]
        print_status("Fill")

    def impossible():
        nonlocal maxs, goal
        current = max(maxs.values())

        while current < maxs[buckets[0]] * maxs[buckets[1]]:
            if (
                current % maxs[buckets[0]] == 0
                and current % maxs[buckets[1]] in [goal, maxs[buckets[1]] - goal]
                or current % maxs[buckets[1]] == 0
                and current % maxs[buckets[0]] in [goal, maxs[buckets[0]] - goal]
            ):
                return False
            current += 1
        return True

    if goal > max(bucket_one, bucket_two):
        raise ValueError("Impossible, goal too high")

    if maxs[buckets[0]] == goal:
        fill()
    elif maxs[buckets[1]] == goal:
        fill()
        switch()
        fill()
    else:
        if impossible():
            raise ValueError("Impossible, cannot achieve with these buckets")

        while state[buckets[0]] != goal and state[buckets[1]] != goal:
            if state[buckets[1]] == maxs[buckets[1]]:
                switch()
                empty()
                switch()
            else:
                if state[buckets[0]] == 0:
                    fill()
                pour()
        if state[buckets[1]] == goal:
            switch()

    return sum(actions.values()), buckets[0], state[buckets[1]]
