"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass

from .stats import average_per_student,subjects_offered,top_scorer,passing_students

def format_report(records: list[dict]) -> str:
    total_records = len(records)
    subjects = sorted(list(subjects_offered(records)))
    averages = average_per_student(records)
    top_student, top_avg = top_scorer(records)
    passers = passing_students(records, threshold=60.0)

    lines = [
        f"Total records: {total_records}",
        f"Subjects offered: {', '.join(subjects)}",
        "Averages:"
    ]
    
    for name in sorted(averages.keys()):
        lines.append(f"  {name} : {averages[name]}")
        
    lines.append(f"Top scorer: {top_student} ({top_avg})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passers)}")
    
    return "\n".join(lines)
