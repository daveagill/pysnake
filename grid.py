class Grid(object):
    def __init__(self, pitch, data):
        self._data = data
        self.width = pitch
        self.height = len(data) / pitch
    
    def get(self, x, y):
        return self._data[y * self.width + x]
    
    def set(self, x, y, value):
        self._data[y * self.width + x] = value
    
    # Apply f(x, y, value) to all elements
    def process(self, f):
        for i in range(len(self._data)):
            f(i % self.width,
              i // self.width,
              self._data[i])