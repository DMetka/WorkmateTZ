from collections import defaultdict
from .base import BaseReport


class AverageReport(BaseReport):
    def generate(self):
        data = defaultdict(lambda: {"count": 0, "total_time": 0.0})

        for entry in self.entries:
            endpoint = entry.get('url')
            response_time = entry.get('response_time')
            if endpoint is None or response_time is None:
                continue
            data[endpoint]['count'] += 1
            data[endpoint]['total_time'] += response_time

        return [
            {
                "Endpoint": endpoint,
                "Requests": values["count"],
                "Avg Response Time": round(values["total_time"] / values["count"], 2)
            }
            for endpoint, values in sorted(data.items())
        ]
