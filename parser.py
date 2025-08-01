import json
from datetime import datetime


def parse_log_file(path, date_filter=None):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        log = json.loads(line)
        if date_filter:
            log_date = log['@timestamp'].split('T')[0]
            if log_date != date_filter:
                continue
        result.append(log)
    return result
