import sublime
import sublime_plugin
from datetime import datetime

def parse_time(s):
    return datetime.strptime(s, '%H:%M')

def format_diff(diff):
    s = str(diff)
    splits = (s.split(':'))
    return splits[0] + ':' + splits[1]

class AikaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Split lines
                lines = s.splitlines()
                # Parse start and end times
                start = parse_time(lines[0])
                end = parse_time(lines[-1])
                # Calculate difference
                diff = end - start
                diff_str = format_diff(diff)
                # Replace the selection with transformed text
                self.view.replace(edit, region, s + '\n\n' + diff_str)  
