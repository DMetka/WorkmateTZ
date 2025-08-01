from .average_report import AverageReport


def get_report_class(name):
    if name == "average":
        return AverageReport
    raise ValueError(f"Unknown report: {name}")
