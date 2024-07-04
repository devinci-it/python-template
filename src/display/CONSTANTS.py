import os

OFFSET = 8
TERMINAL_WIDTH = os.get_terminal_size().columns
DEFAULT_TABLE_WIDTH = TERMINAL_WIDTH - OFFSET  # Default table width
MAX_WIDTH = DEFAULT_TABLE_WIDTH  # Maximum width for text

# Border styles
BORDER_STYLES = {
    'thin': {
        'TOP_LEFT': '┌', 'TOP_RIGHT': '┐',
        'BOTTOM_LEFT': '└', 'BOTTOM_RIGHT': '┘',
        'HORIZONTAL': '─', 'VERTICAL': '│'
    },
    'double': {
        'TOP_LEFT': '╔', 'TOP_RIGHT': '╗',
        'BOTTOM_LEFT': '╚', 'BOTTOM_RIGHT': '╝',
        'HORIZONTAL': '═', 'VERTICAL': '║'
    },
    'medium': {
        'TOP_LEFT': '╓', 'TOP_RIGHT': '╖',
        'BOTTOM_LEFT': '╙', 'BOTTOM_RIGHT': '╜',
        'HORIZONTAL': '─', 'VERTICAL': '│'
    },
    'thick': {
        'TOP_LEFT': '┏', 'TOP_RIGHT': '┓',
        'BOTTOM_LEFT': '┗', 'BOTTOM_RIGHT': '┛',
        'HORIZONTAL': '━', 'VERTICAL': '┃'
    }
}
