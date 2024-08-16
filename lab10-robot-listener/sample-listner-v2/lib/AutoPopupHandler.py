from robot.libraries.BuiltIn import BuiltIn
import os
import re

b = BuiltIn()

class AutoPopupHandler:
    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    PULSE_RESOURCE_PATTERN = "/case/pulse/*"
    
    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
    
    @staticmethod
    def is_pulse_resource(path_string, pattern):
        # Normalize the path string and pattern to use forward slashes
        path_string = path_string.replace(os.sep, '/')
        pattern = pattern.replace(os.sep, '/')

        # Escape special characters in the pattern, except for * and ?
        pattern = re.escape(pattern).replace(r'\*', '.*').replace(r'\?', '.')

        # Ensure the pattern matches from the '/case/' part onwards
        if not pattern.startswith('/case/'):
            pattern = r'.*' + pattern

        # Anchor the pattern to the end of the string
        pattern += '$'

        # Compile the regular expression
        regex = re.compile(pattern, re.IGNORECASE)

        # Perform the match
        return bool(regex.search(path_string))
        
    def start_keyword(self, name, attrs):
        b.log_to_console("keyword: " + name)
        b.log_to_console("attributes: " + attrs['source'])
        if self.is_pulse_resource(attrs['source'], self.PULSE_RESOURCE_PATTERN):
            b.log_to_console("========= Start your popup handler here!!!!!============")
            b.log_to_console("========= IF POPUP EXIST THEN ??? ============")
        
