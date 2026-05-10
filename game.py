import pyxel
from enum import IntEnum

class Direction(IntEnum):
    North = 0
    West = 1
    South = 2
    East = 3

class WallType(IntEnum):
    TYPE_NONE = 0
    TYPE_WALL = 1
    TYPE_DOOR = 2

FIELD_WIDTH = FIELD_HEIGHT = 10

WALLS = [[[WallType.TYPE_WALL] * len(Direction) for _ in range(FIELD_WIDTH)] for _ in range(FIELD_HEIGHT)]

def open_wall(x, y, direction):

    WALLS[y][x][direction] = WallType.TYPE_NONE

    if direction == Direction.North:
        ny = (y - 1) % FIELD_HEIGHT
        WALLS[ny][x][Direction.South] = WallType.TYPE_NONE

    elif direction == Direction.South:
        ny = (y + 1) % FIELD_HEIGHT
        WALLS[ny][x][Direction.North] = WallType.TYPE_NONE

    elif direction == Direction.West:
        nx = (x - 1) % FIELD_WIDTH
        WALLS[y][nx][Direction.East] = WallType.TYPE_NONE

    elif direction == Direction.East:
        nx = (x + 1) % FIELD_WIDTH
        WALLS[y][nx][Direction.West] = WallType.TYPE_NONE

open_wall(0,0,Direction.South);open_wall(0,0,Direction.East)
open_wall(0,1,Direction.North);open_wall(0,1,Direction.South)
open_wall(0,2,Direction.North);open_wall(0,2,Direction.South)
open_wall(0,3,Direction.North);open_wall(0,3,Direction.South)
open_wall(0,4,Direction.North);open_wall(0,4,Direction.South)
open_wall(0,5,Direction.North);open_wall(0,5,Direction.South)
open_wall(0,6,Direction.North);open_wall(0,6,Direction.South)
open_wall(0,7,Direction.North);open_wall(0,7,Direction.South)
open_wall(0,8,Direction.North);open_wall(0,8,Direction.South)
open_wall(0,9,Direction.East);open_wall(0,9,Direction.North)

open_wall(1,0,Direction.East);open_wall(1,0,Direction.West)
open_wall(1,1,Direction.South);open_wall(1,1,Direction.East)
open_wall(1,2,Direction.North);open_wall(1,2,Direction.South);open_wall(1,2,Direction.East)
open_wall(1,3,Direction.North);open_wall(1,3,Direction.East);open_wall(1,3,Direction.South)
open_wall(1,4,Direction.North);open_wall(1,4,Direction.South);open_wall(1,4,Direction.East)
open_wall(1,5,Direction.North);open_wall(1,5,Direction.South)
open_wall(1,6,Direction.North);open_wall(1,6,Direction.South)
open_wall(1,7,Direction.North);open_wall(1,7,Direction.South)
open_wall(1,8,Direction.East);open_wall(1,8,Direction.North)
open_wall(1,9,Direction.East);open_wall(1,9,Direction.West)

open_wall(2,0,Direction.East);open_wall(2,0,Direction.West)
open_wall(2,1,Direction.West);open_wall(2,1,Direction.South)
open_wall(2,2,Direction.North);open_wall(2,2,Direction.South);open_wall(2,2,Direction.West)
open_wall(2,3,Direction.North);open_wall(2,3,Direction.South);open_wall(2,3,Direction.West)
open_wall(2,4,Direction.North);open_wall(2,4,Direction.West)
open_wall(2,5,Direction.South);open_wall(2,5,Direction.East)
open_wall(2,6,Direction.North);open_wall(2,6,Direction.East);open_wall(2,6,Direction.South)
open_wall(2,7,Direction.North);open_wall(2,7,Direction.East)
open_wall(2,8,Direction.West);open_wall(2,8,Direction.East)
open_wall(2,9,Direction.East);open_wall(2,9,Direction.West)

open_wall(3,0,Direction.East);open_wall(3,0,Direction.West);open_wall(3,0,Direction.South)
open_wall(3,1,Direction.North);open_wall(3,1,Direction.South)
open_wall(3,2,Direction.North);open_wall(3,2,Direction.South)
open_wall(3,3,Direction.North);open_wall(3,3,Direction.South)
open_wall(3,4,Direction.North);open_wall(3,4,Direction.South)
open_wall(3,5,Direction.North);open_wall(3,5,Direction.South);open_wall(3,5,Direction.East);open_wall(3,5,Direction.West)
open_wall(3,6,Direction.North);open_wall(3,6,Direction.South);open_wall(3,6,Direction.East);open_wall(3,6,Direction.West)
open_wall(3,7,Direction.North);open_wall(3,7,Direction.East);open_wall(3,7,Direction.West)
open_wall(3,8,Direction.East);open_wall(3,8,Direction.West)
open_wall(3,9,Direction.East);open_wall(3,9,Direction.West)

open_wall(4,0,Direction.East);open_wall(4,0,Direction.West)
open_wall(4,1,Direction.South);open_wall(4,1,Direction.East)
open_wall(4,2,Direction.North);open_wall(4,2,Direction.South)
open_wall(4,3,Direction.North);open_wall(4,3,Direction.South)
open_wall(4,4,Direction.North);open_wall(4,4,Direction.East)
open_wall(4,5,Direction.South);open_wall(4,5,Direction.West)
open_wall(4,6,Direction.North);open_wall(4,6,Direction.South);open_wall(4,6,Direction.West)
open_wall(4,7,Direction.North);open_wall(4,7,Direction.West)
open_wall(4,8,Direction.East);open_wall(4,8,Direction.West)
open_wall(4,9,Direction.East);open_wall(4,9,Direction.West)

open_wall(5,0,Direction.East);open_wall(5,0,Direction.West)
open_wall(5,1,Direction.West)
open_wall(5,2,Direction.South);open_wall(5,2,Direction.East)
open_wall(5,3,Direction.North);open_wall(5,3,Direction.East)
open_wall(5,4,Direction.South);open_wall(5,4,Direction.West);open_wall(5,4,Direction.East)
open_wall(5,5,Direction.North);open_wall(5,5,Direction.East)
open_wall(5,6,Direction.North);open_wall(5,6,Direction.South)
open_wall(5,7,Direction.North);open_wall(5,7,Direction.South)
open_wall(5,8,Direction.West);open_wall(5,8,Direction.North)
open_wall(5,9,Direction.East);open_wall(5,9,Direction.West)

open_wall(6,0,Direction.East);open_wall(6,0,Direction.West);open_wall(6,1,Direction.South)
open_wall(6,1,Direction.South);open_wall(6,1,Direction.North)
open_wall(6,2,Direction.North);open_wall(6,2,Direction.South);open_wall(6,2,Direction.East);open_wall(6,2,Direction.West)
open_wall(6,3,Direction.North);open_wall(6,3,Direction.East);open_wall(6,3,Direction.West)
open_wall(6,4,Direction.South);open_wall(6,4,Direction.East);open_wall(6,4,Direction.West)
open_wall(6,5,Direction.West);open_wall(6,5,Direction.North)
open_wall(6,6,Direction.South);open_wall(6,6,Direction.East)
open_wall(6,7,Direction.East);open_wall(6,7,Direction.South);open_wall(6,7,Direction.North)
open_wall(6,8,Direction.North);open_wall(6,8,Direction.East)
open_wall(6,9,Direction.East);open_wall(6,9,Direction.West)

open_wall(7,0,Direction.East);open_wall(7,0,Direction.West)
open_wall(7,1,Direction.East)
open_wall(7,2,Direction.East);open_wall(7,2,Direction.South);open_wall(7,2,Direction.West)
open_wall(7,3,Direction.North);open_wall(7,3,Direction.West);open_wall(7,3,Direction.East);open_wall(7,3,Direction.South)
open_wall(7,4,Direction.South);open_wall(7,4,Direction.East);open_wall(7,4,Direction.West);open_wall(7,4,Direction.North)
open_wall(7,5,Direction.West);open_wall(7,5,Direction.East);open_wall(7,5,Direction.North)
open_wall(7,6,Direction.South);open_wall(7,6,Direction.West);open_wall(7,6,Direction.East)
open_wall(7,7,Direction.South);open_wall(7,7,Direction.West);open_wall(7,7,Direction.East);open_wall(7,7,Direction.North)
open_wall(7,8,Direction.East);open_wall(7,8,Direction.North);open_wall(7,8,Direction.West)
open_wall(7,9,Direction.East);open_wall(7,9,Direction.West)

open_wall(8,0,Direction.East);open_wall(8,0,Direction.West)
open_wall(8,1,Direction.East);open_wall(8,1,Direction.West)
open_wall(8,2,Direction.West);open_wall(8,2,Direction.South)
open_wall(8,3,Direction.North);open_wall(8,3,Direction.West)
open_wall(8,4,Direction.South);open_wall(8,4,Direction.East);open_wall(8,4,Direction.West)
open_wall(8,5,Direction.West);open_wall(8,5,Direction.North);open_wall(8,5,Direction.East)
open_wall(8,6,Direction.East);open_wall(8,6,Direction.South);open_wall(8,6,Direction.West)
open_wall(8,7,Direction.South);open_wall(8,7,Direction.North);open_wall(8,7,Direction.East);open_wall(8,7,Direction.West)
open_wall(8,8,Direction.East);open_wall(8,8,Direction.West);open_wall(8,8,Direction.South);open_wall(8,8,Direction.North)
open_wall(8,9,Direction.East);open_wall(8,9,Direction.West);open_wall(8,9,Direction.North)

open_wall(9,0,Direction.West)
open_wall(9,1,Direction.South);open_wall(9,1,Direction.West)
open_wall(9,2,Direction.North);open_wall(9,2,Direction.South)
open_wall(9,3,Direction.North);open_wall(9,3,Direction.South)
open_wall(9,4,Direction.South);open_wall(9,4,Direction.North);open_wall(9,4,Direction.West)
open_wall(9,5,Direction.West);open_wall(9,5,Direction.North)
open_wall(9,6,Direction.West);open_wall(9,6,Direction.South)
open_wall(9,7,Direction.South);open_wall(9,7,Direction.North);open_wall(9,7,Direction.West)
open_wall(9,8,Direction.North);open_wall(9,8,Direction.West)
open_wall(9,9,Direction.West)

playervector = {
    Direction.North: (0, -1),
    Direction.West: (-1, 0),
    Direction.South: (0, 1),
    Direction.East: (1, 0),
}

class Game:
    def __init__(self):
        pyxel.init(256, 224, "DRPG")

        self.img = pyxel.Image(256, 224)

        self.location = [[[0] * 2 for _ in range(15)] for _ in range(len(Direction))]

        self.images = {}

        for i in reversed(range(15)):
            for j in range(4):
                try:
                    img = pyxel.Image(256, 224)
                    img.load(0, 0, f"assets/{i}_{j}.png")
                    self.images[(i, j)] = img
                except Exception as e:
                    pass

        self.location = [
            [
                [-1, -4],[1, -4],[0, -4],
                [-1, -3],[1, -3],[0, -3],
                [-1, -2],[1, -2],[0, -2],
                [-1, -1],[1, -1],[0, -1],
                [-1,  0],[1,  0],[0,  0],
            ],
            [
                [-4,  1],[-4, -1],[-4, 0],
                [-3,  1],[-3, -1],[-3, 0],
                [-2,  1],[-2, -1],[-2, 0],
                [-1,  1],[-1, -1],[-1, 0],
                [ 0,  1],[ 0, -1],[ 0, 0],
            ],
            [
                [ 1,  4],[-1, 4],[ 0, 4],
                [ 1,  3],[-1, 3],[ 0, 3],
                [ 1,  2],[-1, 2],[ 0, 2],
                [ 1,  1],[-1, 1],[ 0, 1],
                [ 1,  0],[-1, 0],[ 0, 0],
            ],
            [
                [ 4, -1],[ 4, 1],[ 4, 0],
                [ 3, -1],[ 3, 1],[ 3, 0],
                [ 2, -1],[ 2, 1],[ 2, 0],
                [ 1, -1],[ 1, 1],[ 1, 0],
                [ 0, -1],[ 0, 1],[ 0, 0],
            ]
        ]
        self.player_x = 0
        self.player_y = 9
        self.player_dir = Direction.North

        pyxel.run(self.update, self.draw)
    def update(self):

        if pyxel.btnp(pyxel.KEY_UP):
            if WALLS[self.player_y][self.player_x][self.player_dir] == WallType.TYPE_NONE:
                dx, dy = playervector[self.player_dir]
                self.player_x = (self.player_x + dx) % FIELD_WIDTH
                self.player_y = (self.player_y + dy) % FIELD_HEIGHT

        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.player_dir = (self.player_dir-1) % len(Direction)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.player_dir = (self.player_dir+1) % len(Direction)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.player_dir = (self.player_dir+2) % len(Direction)

    def draw(self):
        pyxel.cls(0)

        for i in range(15):
            depth = i-i%3

            x = self.player_x + self.location[self.player_dir][i][0]
            y = self.player_y + self.location[self.player_dir][i][1]
            x %= FIELD_WIDTH
            y %= FIELD_HEIGHT

            for j in [1, 3, 2, 0]:
                direction = (self.player_dir + j) % len(Direction)
                if WALLS[y][x][direction]:
                    print(i, j)
                    if (i, j) in self.images:
                        pyxel.dither(0.8*depth/12+0.1)
                        pyxel.blt(0,0,self.images[i, j], 0,0,256,224,7)

        pyxel.dither(1.0)
        pyxel.text(30,10, f"x:{self.player_x}, y:{self.player_y}, dir:{Direction(self.player_dir).name}",7)