from datetime import date


def mark_attendance(employee_id, status):
    """Mark attendance for an employee with today's date."""
    if status not in ("present", "absent", "late"):
        raise ValueError("status must be 'present', 'absent' or 'late'")
    return {
        "employee_id": employee_id,
        "status": status,
        "date": date.today().isoformat(),
    }
