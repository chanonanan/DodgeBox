import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INSTRUCTIONS_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2
GAME_WIN = 3

MOVEMENT_SPEED = 7
LIFE_POINT = 100
MAX_COIN = 20

class Enemy(arcade.Sprite):

    def reset_pos(self):
        if random.randrange(200) == 5:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y -= MOVEMENT_SPEED
        if self.top < 0:
            self.reset_pos()

class Enemy2(arcade.Sprite):

    def reset_pos(self):
        if random.randrange(200) == 5:
            self.center_x = random.randrange(SCREEN_WIDTH + 20,
                                             SCREEN_WIDTH + 100)
            self.center_y = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.center_x -= MOVEMENT_SPEED
        if self.center_x < 0:
            self.reset_pos()

class Enemy3(arcade.Sprite):

    def reset_pos(self):
        if random.randrange(200) == 5:
            self.center_y = 0
            self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        self.center_y += MOVEMENT_SPEED
        if self.top > SCREEN_HEIGHT:
            self.reset_pos()

class Enemy4(arcade.Sprite):

    def reset_pos(self):
        if random.randrange(200) == 5:
            self.center_x = 0
            self.center_y = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.center_x += MOVEMENT_SPEED
        if self.center_x > SCREEN_WIDTH:
            self.reset_pos()

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x -= self.change_x
        self.center_y -= self.change_y

        if self.center_x < self.left_boundary:
            self.change_x *= -1

        if self.center_x > self.right_boundary:
            self.change_x *= -1

        if self.center_y < self.bottom_boundary:
            self.change_y *= -1

        if self.center_y > self.top_boundary:
            self.change_y *= -1


class MyAppWindow(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)
        self.current_state = INSTRUCTIONS_PAGE
        
        # Sprite lists
        self.all_sprites_list = None
        self.enemy_list = None
        self.enemy2_list = None
        self.enemy3_list = None
        self.enemy4_list = None
        self.coin_list = None

        # Set up the player
        self.life = 0
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):

        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.life = LIFE_POINT
        self.score = 0
        self.player_sprite = arcade.Sprite("images/box.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)
        for i in range(20):

            enemy = Enemy("images/ball.png", SPRITE_SCALING )
            enemy2 = Enemy2("images/ball.png", SPRITE_SCALING )
            enemy3 = Enemy3("images/ball.png", SPRITE_SCALING )
            enemy4 = Enemy4("images/ball.png", SPRITE_SCALING )
            
            
            if random.randrange(20) == 5:
                enemy.center_x = random.randrange(SCREEN_WIDTH)
                enemy.center_y = random.randrange(SCREEN_HEIGHT)
                enemy2.center_x = random.randrange(SCREEN_WIDTH)
                enemy2.center_y = random.randrange(SCREEN_HEIGHT)
                enemy3.center_x = random.randrange(SCREEN_WIDTH)
                enemy3.center_y = random.randrange(SCREEN_HEIGHT)
                enemy4.center_x = random.randrange(SCREEN_WIDTH)
                enemy4.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprites_list.append(enemy)
            self.enemy_list.append(enemy)
            self.all_sprites_list.append(enemy2)
            self.enemy_list.append(enemy2)
            self.all_sprites_list.append(enemy3)
            self.enemy_list.append(enemy3)
            self.all_sprites_list.append(enemy4)
            self.enemy_list.append(enemy4)
            
        for i in range(MAX_COIN):
            coin = Coin("images/coin.png", SPRITE_SCALING )

            coin.left_boundary = coin.width // 2
            coin.right_boundary = SCREEN_WIDTH - coin.width // 2
            coin.bottom_boundary = coin.height // 2
            coin.top_boundary = SCREEN_HEIGHT - coin.height // 2

            coin.center_x = random.randint(coin.left_boundary,
                                           coin.right_boundary)
            coin.center_y = random.randint(coin.bottom_boundary,
                                           coin.top_boundary)

            coin.change_x = random.randint(-3, 3)
            coin.change_y = random.randint(-3, 3)
            
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)


        self.set_mouse_visible(False)
            



    def draw_instructions_page(self):
        output = "Use Mouse to play"
        arcade.draw_text(output, 130, 400, arcade.color.WHITE, 54)

        output = "Dodge box, Collect ball"
        arcade.draw_text(output, 250, 320, arcade.color.WHITE, 24)

        output = "Click to start"
        arcade.draw_text(output, 310, 250, arcade.color.WHITE, 24)


    def draw_game(self):
        self.all_sprites_list.draw()
        
        output = "Life Point: {}".format(self.life)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 230, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 285, 300, arcade.color.WHITE, 24)

    def draw_game_win(self):
        output = "You Win"
        arcade.draw_text(output, 275, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 285, 300, arcade.color.WHITE, 24)


    def on_draw(self):
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE:
            self.draw_instructions_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == GAME_WIN:
            self.draw_game()
            self.draw_game_win()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):

        if self.current_state == INSTRUCTIONS_PAGE:
            self.start_new_game()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.start_new_game()
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        
        if self.score >= MAX_COIN *0.8:
            self.player_sprite.center_x = y
            self.player_sprite.center_y = x
        else:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def animate(self, delta_time):

        self.all_sprites_list.update()

        hit_list = \
            arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.enemy_list)
        point_list = \
            arcade.check_for_collision_with_list(self.player_sprite,
                                                 self.coin_list)


        if self.current_state == GAME_RUNNING:
            for enemy in hit_list:
                enemy.kill()
                self.life -= 1
            for coin in point_list:
                coin.kill()
                self.score += 1

        if self.score == MAX_COIN and self.life > 0:
            self.current_state = GAME_WIN
        if self.score < MAX_COIN and self.life == 0:
            self.current_state = GAME_OVER



def main():
    window = MyAppWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_background_color(arcade.color.BLACK)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()
