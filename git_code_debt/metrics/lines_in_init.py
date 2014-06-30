
from git_code_debt.metrics.base import SimpleLineCounterBase


class Python__init__LineCount(SimpleLineCounterBase):
    def should_include_file(self, file_diff_stat):
        return file_diff_stat.filename == '__init__.py'

    def line_matches_metric(self, line, file_diff_stat):
        # All lines in __init__.py match
        return True
