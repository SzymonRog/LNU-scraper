def generate_report(points, threshold):
    if points >= threshold:
        return f"You passed the exam with {points} points."
    else:
        return f"You failed the exam with {points} points."