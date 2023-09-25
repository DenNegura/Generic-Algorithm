import datetime

class JsonWriter:

    def __init__(self, file_prefix):
        self._file = None
        self._file_prefix = file_prefix
        self._file_extension = '.json'
        self.open_file(self.get_file_name())

    def get_file_name(self):
        return self._file_prefix + datetime.datetime.now().isoformat().replace(':', '.') + self._file_extension

    def open_file(self, file_name):
        self._file = open(file_name, 'w')

    def write(self, *args):
        line = ''
        for arg in args:
            line += str(arg) + ' '
        self._file.write(line + '\n')

    def close(self):
        if self._file:
            self._file.close()
            self._file = None
