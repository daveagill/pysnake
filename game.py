import pyglet
import gamestate
import renderer
import snake

if __name__ == '__main__':          
    GROWTH = 3
    FREQUENCY = 1/10.0
    
    game = gamestate.GameState() 
    gfx = renderer.Renderer(game.width, game.height, 20)
    window = gfx.createWindow('pySnake - Dave::Soft')
         
    keyBindings = {pyglet.window.key.W     : snake.UP,
                   pyglet.window.key.UP    : snake.UP,
                   pyglet.window.key.S     : snake.DOWN,
                   pyglet.window.key.DOWN  : snake.DOWN,
                   pyglet.window.key.A     : snake.LEFT,
                   pyglet.window.key.LEFT  : snake.LEFT,
                   pyglet.window.key.D     : snake.RIGHT,
                   pyglet.window.key.RIGHT : snake.RIGHT}
        
    @window.event
    def on_key_press(symbol, modifiers):
        if keyBindings.has_key(symbol):
            game.snake.turn(keyBindings[symbol])
        elif not game.alive and \
             (symbol == pyglet.window.key.SPACE or \
              symbol == pyglet.window.key.ENTER):
            game.reset()
            
    @window.event
    def on_draw():
        gfx.draw(game)
        
    def update(dt):
        if not game.alive:
            return
        
        game.snake.move()
        
        if game.foodCollision():
            game.snake.grow(GROWTH)
            game.randomiseFood()
        
        if game.bodyCollision() or game.wallCollision():
            #pass
            game.alive = False
    
    pyglet.clock.schedule_interval(update, FREQUENCY)
    pyglet.app.run()
