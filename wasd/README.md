# Space Shooter

A simple space shooter game made with Python and Pygame.

## How to run

```
pip install pygame
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| W A S D | Move |
| SPACE | Shoot |
| ESC | Quit |
| R | Restart (on end screen) |

## Objective

Destroy **20 enemies** before losing all 3 HP.

- Enemies that reach the bottom of the screen deal damage
- Enemy bullets also deal damage
- Enemies with 2 HP show a health bar above them

## Project structure

```
space_shooter
├── main.py       # entry point
├── settings.py   # constants and colors
├── game.py       # main game loop
├── player.py     # Player class
├── enemy.py      # Enemy class
├── bullet.py     # PlayerBullet and EnemyBullet classes
└── menu.py       # title screen and end screen
```
