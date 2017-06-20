from sml import vector

# Movement directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# A segment of the snake 
class Segment(object):
    # Segment Types: Horizontal, Vertical, TopLeftCorner, etc
    HORIZONTAL  = 0; VERTICAL = 1
    TLCORNER = 2; BLCORNER = 3; TRCORNER = 4; BRCORNER = 5
    
    # (initialDirection, finalDirection) -> Segment Type
    _segmentType = {(UP,    UP)    : VERTICAL,
                    (DOWN,  DOWN)  : VERTICAL,
                    (LEFT,  LEFT)  : HORIZONTAL,
                    (RIGHT, RIGHT) : HORIZONTAL,
                    (UP,    LEFT)  : TRCORNER,
                    (UP,    RIGHT) : TLCORNER,
                    (DOWN,  LEFT)  : BRCORNER,
                    (DOWN,  RIGHT) : BLCORNER,
                    (LEFT,  UP)    : BLCORNER,
                    (LEFT,  DOWN)  : TLCORNER,
                    (RIGHT, UP)    : BRCORNER,
                    (RIGHT, DOWN)  : TRCORNER}
                
    def __init__(self, position, initialDirection):
        self._position = position
        self._direction = initialDirection
        self._type = None
    
    # Sets the final direction and type of the segment
    def setFinalDirection(self, direction):
        self._type = self._segmentType[(self._direction, direction)]
        self._direction = direction
        
    def _getPosition(self):
        return self._position
    position = property(_getPosition)
        
    def _getDirection(self):
        return self._direction
    direction = property(_getDirection)
    
    # Type can only be known if the segment has a final direction
    def _getType(self):
        return self._type
    type = property(_getType)

# The snake itself
class Snake(object):
    _displacements = {UP:    vector.Vector2(0, 1),
                      DOWN:  vector.Vector2(0, -1),
                      LEFT:  vector.Vector2(-1, 0),
                      RIGHT: vector.Vector2(1, 0)}

    def __init__(self, x, y, growth, direction):
        self._segments = [Segment(vector.Vector2(x, y), direction)]
        self._directions = [direction]
        self._growth = growth
    
    def _length(self):
        return len(self._segments)
    length = property(_length)    
    
    def _head(self):
        return self._segments[0]
    head = property(_head)

    def _tail(self):
        return self._segments[-1]
    tail = property(_tail)
    
    # All segments excluding head and tail
    def _body(self):
        return self._segments[1:-1]
    body = property(_body)
    
    # Direction of the head
    def _heading(self):
        return self._directions[0]
    heading = property(_heading)
    
    def __iter__(self):
        return self._segments.__iter__()
    
    # Queue a growth of the snake
    def grow(self, growth = 1):
        self._growth += growth
    
    # Queue a direction for the snake to turn,
    # may be called multiple times before move()
    def turn(self, direction):
        # ensure the direction won't turn the backwards snake onto itself
        if direction >= 2 and self._directions[-1] <= 1 or \
           direction <= 1 and self._directions[-1] >= 2:
            self._directions.append(direction)
    
    # Moves the snake in the direction of the first queued direction
    def move(self):    
        if len(self._directions) > 1: # remove old direction to get new direction
            self._directions.pop(0)
        
        # the final direction of the old head segment is now known
        self.head.setFinalDirection(self.heading)

        # add a new head
        position = self.head.position + self._displacements[self.heading]
        self._segments.insert(0, Segment(position, self.heading))
        
        if self._growth > 0:     # grow snake
            self._growth -= 1
        else:
            self._segments.pop()
    
    def selfCollision(self):
        for i in range(self.length-1):
            if self.head.position == self._segments[i+1].position:
                return True
        return False