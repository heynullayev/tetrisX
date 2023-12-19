class Colors:
    """
    Предоставляет все цвета используемы в игре.

    - `dark_grey`: RGB tuple representing dark grey color.
    - `green`: RGB tuple representing green color.
    - `red`: RGB tuple representing red color.
    - `orange`: RGB tuple representing orange color.
    - `yellow`: RGB tuple representing yellow color.
    - `purple`: RGB tuple representing purple color.
    - `cyan`: RGB tuple representing cyan color.
    - `blue`: RGB tuple representing blue color.
    - `white`: RGB tuple representing white color.
    - `dark_blue`: RGB tuple representing dark blue color.
    - `light_blue`: RGB tuple representing light blue color.

    :returns: List of RGB tuples representing various cell colors.
    :rtype: list
    """
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        """
        Получение списка предоставленных цветов для ячеек.

        :returns: List of RGB tuples representing various cell colors.
        :rtype: list
        """
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
