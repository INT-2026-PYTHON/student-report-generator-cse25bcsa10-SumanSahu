"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass


from collections import defaultdict

def average_per_student(records: list[dict]) -> dict[str, float]:
    student_scores = defaultdict(list)
    for record in records:
        student_scores[record["name"]].append(record["score"])
        
    return {
        name: round(sum(scores) / len(scores), 2)
        for name, scores in student_scores.items()
    }

def subjects_offered(records: list[dict]) -> set[str]:
    return {record["subject"] for record in records}

def top_scorer(records: list[dict])->tuple[str,float]:
    averages = average_per_student(records)
    if not averages:
        return ("", 0.0)
    return max(averages.items(), key=lambda item: item[1])

def passing_students(records:list[dict],threshold:float=60.0)->list[str]:
    averages = average_per_student(records)
    passing = [name for name, avg in averages.items() if avg>=threshold]
    return sorted(passing)
