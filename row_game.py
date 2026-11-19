def solution(board, k):
    n = len(board)
    prefix = [0]
    best = []
    lowest = 0

    for value in board:
        prefix.append(prefix[-1] + value)
        best.append(prefix[-1] - lowest)
        lowest = min(lowest, prefix[-1])

    # Earliest arrival with the next direction pointing left.
    times = [k + 1] * n
    scores = [0] * n

    for r in range(n):
        if prefix[r + 1] >= 0:
            times[r] = 1
            scores[r] = prefix[r + 1]

    answer = 0

    for r in range(n):
        if times[r] > k:
            continue

        gain = best[r]
        answer = max(
            answer,
            scores[r] + (k - times[r]) * max(0, gain)
        )

        if gain <= 0:
            continue

        for j in range(r + 1, n):
            base = scores[r] + prefix[j + 1] - prefix[r + 1]

            # Each pair of trips earns 2 * gain in two moves.
            pairs = max(1, (-base + 2 * gain - 1) // (2 * gain))
            arrival = times[r] + 2 * pairs
            total = base + 2 * pairs * gain

            if arrival < times[j] or (
                arrival == times[j] and total > scores[j]
            ):
                times[j] = arrival
                scores[j] = total

    return answer
