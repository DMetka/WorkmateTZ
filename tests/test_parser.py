from parser import parse_log_file


def test_parse_log_file(tmp_path):
    content = '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."}\n'
    file = tmp_path / "test.log"
    file.write_text(content)

    parsed = parse_log_file(str(file))
    assert len(parsed) == 1
    assert parsed[0]['url'] == "/api/context/..."


def test_parse_log_with_date_filter(tmp_path):
    content = '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."}\n'
    file = tmp_path / "test.log"
    file.write_text(content)

    parsed = parse_log_file(str(file), date_filter="2025-06-22")
    assert len(parsed) == 1

    parsed_empty = parse_log_file(str(file), date_filter="2025-06-23")
    assert len(parsed_empty) == 0