# SCREEN CONST
SCREEN_WIDTH = 1336
SCREEN_HEIGHT = 768

# COLORS 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
RED = (180, 0, 0)
GREEN = (0, 170, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)

# Dont change (gravity doesnt work well with lower fps)
FPS = 120

# GENERAL CONSTS
LEFT = 1
RIGHT = 0
GRAVITY = 0.25
GROUND = SCREEN_HEIGHT - 150

# UI CONSTS
# BARS
BAR_HEIGHT = 10
# SLOTS
SLOT_WIDTH = 50
SLOT_HEIGHT = 80
# ICONS
ICON_WIDTH = 80
ICON_HEIGHT = 80

# PLAYER CONST
# Geometry
PLAYER_HEIGHT = 70
PLAYER_WIDTH = 50
# Stats
PLAYER_MAX_HP = 500
PLAYER_MAX_MANA = 50
PLAYER_MAX_STAMINA = 800
PLAYER_SPEED = int(3*(120/FPS))
JUMP_SPEED = int(10*(120/FPS))
# Consumption
DASH_S_COST = 100
DASH_DIST = 100
JMP_S_COST = 100
ATK_S_COST = 100
CTR_S_COST = 30

# ENEMY CONST
# Geometry
ENEMY_HEIGHT = 70
ENEMY_WIDTH = 50
# Stats
ENEMY_MAX_HP = 900
ENEMY_SPEED = int(1*(120/FPS))

# WEAPON CONST
# Geometry
WEAPON_LENGTH = 130
WEAPON_WIDTH = 20
# Stats
WEAPON_DAMAGE = 50
WEAPON_WEIGHT = 50
# States
IDLE = 0
CHASE = 1
ATTACK = 2
