
"""
* Input: touple (x, y)
* Returns: key for mapTiles in GameBoard. Returns None, if outside.
"""
def coordinates_to_key(pos):
    x = pos[0]
    y = pos[1]
    key = ""
    if 270 <= x < 360:
        key += "a"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
    if 360 <= x < 450:
        key += "b"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
        
    if 450 <= x < 540:
        key += "c"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"
        
    if 540 <= x < 630:
        key += "d"
        if 270 <= y < 360:
            key += "4"
        if 360 <= y < 450:
            key += "3"
        if 450 <= y < 540:
            key += "2"
        if 540 <= y < 630:
            key += "1"

    if len(key) == 2:
        return key
    return None


"""
* GameBoard for 900 * 900 board
"""
class GameBoard():
    def __init__(self):
        """
        [0] = Tower tile
        [1] = Position. Topleft Corner tuple (x,y)
        """
        self.mapTiles = {
            "a4":[None, (270,270)], "b4":[None, (360,270)], "c4":[None, (450, 270)], "d4": [None, (540, 270)],
            "a3":[None, (270, 360)], "b3":[None, (360, 360)], "c3":[None, (450, 360)], "d3":[None, (540, 360)],
            "a2":[None, (270, 450)], "b2":[None, (360, 450)], "c2":[None, (450, 450)], "d2":[None, (540, 450)],
            "a1":[None, (270, 540)], "b1":[None, (360, 540)], "c1":[None, (450, 540)], "d1":[None,540, 540]
        }

    def click_tile(self, mousePosClick):
        tile = coordinates_to_key(mousePosClick)
        print("tile clicked = ", tile)
        if self.mapTiles[tile][0] != None:
            self.mapTiles[tile].clicked()
            return
        print("Tile is empty")


        
    
        
        



