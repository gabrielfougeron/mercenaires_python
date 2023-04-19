import numpy as np

class Mercenaires:

    def __init__(
            self,
            InitPurse = 50,
            DistMidToCity = 3,
            NameL = 'Left',
            NameR = 'Right'
        ):

        self.PurseL = InitPurse
        self.PurseR = InitPurse

        self.NameL = NameL
        self.NameR = NameR

        self.PosMerc = 0
        self.DistMidToCity = DistMidToCity

        self.ascii_castle = [
            '[][][] /\/\ [][][]',
            ' |##|__|##|__|##| ',
            ' |##############| ',
            ' |#####/||\#####| ',
            ' |#####||||#####| ',
        ]

        self.ascii_merc = [
            '  o  ',
            ' /|\ ',
            '_/ \_',
        ]

        self.ascii_grass = ['\\\\\\\\\\']

        self.ascii_blank = ['  ']

        self.CheckAsciiArtSquare()

    def MakeAsciiScene(self):

        scene = [self.ascii_castle]

        for i in range(-self.DistMidToCity,self.PosMerc):
            scene.append(self.ascii_blank)
            scene.append(self.ascii_grass)
        
        scene.append(self.ascii_blank)
        scene.append(self.ascii_merc)

        for i in range(self.PosMerc + 1 ,self.DistMidToCity):
            scene.append(self.ascii_blank)
            scene.append(self.ascii_grass)
        
        scene.append(self.ascii_blank)
        scene.append(self.ascii_castle)

        return scene


    def __str__(self):

        res = ''

        scene = self.MakeAsciiScene()

        max_height = 0
        for ascii_art in scene:
            max_height = max(max_height,len(ascii_art))

        scene = self.MakeAsciiScene()

        for height in range(max_height):
            for item in scene:
                depth = len(item) - max_height + height
                
                if depth >= 0:
                    res += item[depth]
                else:
                    for i in range(len(item[0])):
                        res += ' '
                
            res += '\n'

        # return str(max_height)
        return res




    def CheckAsciiArtSquare(self):

        for key in dir(self):
            if key.startswith('ascii'):
                assert ascii_is_square(getattr(self, key))

def ascii_is_square(ascii_art):

    min_len = len(ascii_art[0])
    max_len = min_len
    for the_line in ascii_art:
        the_len = len(the_line)
        min_len = min(min_len, the_len)
        max_len = max(min_len, the_len)

    return (min_len == max_len)