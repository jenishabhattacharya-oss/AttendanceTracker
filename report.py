import csv


def export_report(records, path):
    """Export attendance records to a CSV file and return the path."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["employee_id", "status", "date"])
        for r in records:
            writer.writerow([r["employee_id"], r["status"], r["date"]])
    return path
