import math

def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    s = sum([math.exp(i - m) for i in scores])

    return [math.exp(i - m)/s for i in scores]