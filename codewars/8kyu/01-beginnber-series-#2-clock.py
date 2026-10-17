# DATE : 17 OCT 2026

"""Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds."""

def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)
