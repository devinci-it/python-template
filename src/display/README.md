### README.md

#### `src/display/` Directory Overview

This directory contains classes and constants for formatting and displaying text in a terminal using various styles.

#### Files:

- **`CONSTANTS.py`**: Defines constants such as terminal width and border styles used for text formatting.
  
- **`display.py`**: Contains the `Display` class that handles text formatting and display using the defined constants.
  
- **`__init__.py`**: Initializes the `Display` class with a predefined theme and border style.

#### Constants (`CONSTANTS.py`)

- **Constants**:
  - `OFFSET`: Represents the offset used in calculating default and maximum table widths.
  - `TERMINAL_WIDTH`: Retrieves the current terminal width using `os.get_terminal_size()`.
  - `DEFAULT_TABLE_WIDTH`: Calculates the default table width by subtracting `OFFSET` from `TERMINAL_WIDTH`.
  - `MAX_WIDTH`: Sets the maximum width for text display, initially set to `DEFAULT_TABLE_WIDTH`.

- **Border Styles (`BORDER_STYLES`)**:
  - Contains different predefined border styles (`thin`, `double`, `medium`, `thick`) with corresponding characters for top left, top right, bottom left, bottom right corners, horizontal lines, and vertical lines.

#### Methods (`display.py`)

- **`Display` Class**:
  - **Initialization (`__init__`)**:
    - Accepts a `theme` dictionary and `border_style` string (defaults to `'thick'`) to initialize the display settings.
    - Sets up constants like `table_width` and retrieves terminal width.

  - **Formatting Methods**:
    - **`format_with_border(message)`**: Formats the message with a border at the top and bottom using `theme['header']`.
    - **`_print_message(message, theme=None, justify='left', bold=False, max_width=None, indent=0)`**: Prints a formatted message with options for justification, bolding, and indentation.
  
  - **Text Display Methods**:
    - **`header(text, bold=False)`**: Prints the `text` centered with the `theme['header']`.
    - **`footer(text, bold=False)`**: Prints the `text` centered with the `theme['reset']`.
    - **`option(text, bold=False)`**: Prints `text` with the `theme['option']`.
    - **`body(text, bold=False)`**: Prints `text` with the `theme['body_text']`.
    - **`body_highlight(text, bold=False)`**: Prints `text` with the `theme['body_highlight']`.
    - **`underline(text, bold=False)`**: Prints `text` centered and resets formatting.
    - **`key_value_pair(key, value, bold_key=True, bold_value=False)`**: Prints `key` and `value` with specific formatting, optionally bolding them.

  - **Special Formatting Methods**:
    - **`header_and_sub(header, sub)`**: Combines a header and subheader with specified formatting.
    - **`banner(file_path)`**: Reads and displays a banner from a file using the `header` method.

#### Initialization (`__init__.py`)

- **`__init__.py`**:
  - Imports the `Display` class from `display.py`.
  - Initializes a `theme` dictionary with predefined ANSI escape sequences for different text styles and colors.
  - Creates a `DISPLAY` object using the `Display` class with the predefined `theme` and a `'thick'` border style.

#### Usage

To use the `Display` class in your Python scripts, follow these steps:

1. **Import the `DISPLAY` object** from `src/display/__init__.py`:

   ```python
   from src.display import DISPLAY
   ```

2. **Format and Display Text**:

   You can use the various methods provided by `DISPLAY` to format and display text in your terminal:

   ```python
   # Display a header
   DISPLAY.header("Welcome to My Application")

   # Display options
   DISPLAY.option("Select an option:")
   DISPLAY.body("1. Option A")
   DISPLAY.body("2. Option B")

   # Display a footer
   DISPLAY.footer("Please select an option above.")
   ```

   You can also format specific elements such as key-value pairs or banners:

   ```python
   # Display a key-value pair
   DISPLAY.key_value_pair("Key", "Value", bold_value=True)

   # Display a banner from a file
   DISPLAY.banner("path/to/banner.txt")
   ```

   Adjust paths (`src/display` in import statements) based on your project structure.

#### Notes:

- Ensure Python 3.6+ is installed on your system.
- Additional setup or installation instructions can be provided if necessary, such as dependencies or environment setup.
