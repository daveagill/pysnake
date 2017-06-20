import pyglet
import snake

# Returns the path to an image
def imagePath(name):
    return 'images/' + name

# Loads an image
def loadImage(name):
    return pyglet.image.load(imagePath(name))

# Renders the game of snake
class Renderer(object):    
    _backgroundImage = loadImage('background.jpg')
    _wallImage       = loadImage('wall.png')
    _foodImage       = loadImage('food.png')
    
    _segmentImages = {snake.Segment.HORIZONTAL: loadImage('bodyH.png'),
                      snake.Segment.VERTICAL:   loadImage('bodyV.png'),
                      snake.Segment.TLCORNER:   loadImage('bodyTL.png'),
                      snake.Segment.BLCORNER:   loadImage('bodyBL.png'),
                      snake.Segment.TRCORNER:   loadImage('bodyTR.png'),
                      snake.Segment.BRCORNER:   loadImage('bodyBR.png')}
    
    _headImages = {snake.UP:    loadImage('headUp.png'),
                   snake.DOWN:  loadImage('headDown.png'),
                   snake.LEFT:  loadImage('headLeft.png'),
                   snake.RIGHT: loadImage('headRight.png')}
    
    _tailImages = {snake.UP:    loadImage('tailUp.png'),
                   snake.DOWN:  loadImage('tailDown.png'),
                   snake.LEFT:  loadImage('tailLeft.png'),
                   snake.RIGHT: loadImage('tailRight.png')}
    
    def __init__(self, width, height, cellSize):
        self.width = width * cellSize
        self.height = height * cellSize
        self.cellSize = cellSize
        self._batch = pyglet.graphics.Batch()
    
    # Creates a window of the correct size with blending enabled
    def createWindow(self, caption):
        window = pyglet.window.Window(self.width, self.height, caption)
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND) 
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        return window
    
    def draw(self, gameState):
        Renderer._backgroundImage.blit(0, 0)
        self._drawArena(gameState.arena)
        self._drawFood(gameState.foodPosition)
        self._drawSnake(gameState.snake)

    def _drawArena(self, arena):
        def _drawCell(x, y, value):
            screenTop = self.height - self.cellSize
            if value == 1:
                Renderer._wallImage.blit(x * self.cellSize,
                                         screenTop - y * self.cellSize)
        arena.process(_drawCell)

    def _drawSnake(self, snake): # SWITCH TO AN EVENT MODEL LIKE THE REAL MVC PATTERN
        position  = snake.head.position * self.cellSize
        snake.head.sprite = pyglet.sprite.Sprite(Renderer._headImages[snake.head.direction],
                                                 position.x, position.y,
                                                 batch = self._batch)       
        if snake.length > 1:
            snake.tail.sprite.image = Renderer._tailImages[snake.tail.direction]
        
        if (snake.body):
            segment = snake.body[0]
            segment.sprite.image = Renderer._segmentImages[segment.type]
            
        self._batch.draw()
        

    def _drawFood(self, position):
        position = position * self.cellSize
        Renderer._foodImage.blit(position.x, position.y)