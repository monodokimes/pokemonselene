#tile dictionaries
import pygame, sys

pallet_town = {'battle_tiles':(416,417,418,419,440,441,442,443),'spawn_tile':199,'event_tiles':(173,182),'warp_tiles':(175, 184),
			'invalids':(12,15,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,46,50,71,74,95,98,102,103,104,105,106,
			111,112,113,114,115,119,122,126,130,135,139,143,146,150,154,159,163,167,170,174,176,177,178,183,
			185,186,187,191,194,215,218,239,242,254,255,256,257,258,259,260,263,266,270,271,272,273,278,284,
			287,290,302,308,311,314,326,327,328,330,331,332,335,338,359,362,383,386,398,399,400,402,403,407,
			410,431,434,455,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478),
			'V':24}

pokemon_centre_ground_floor = {'battle_tiles':(), 'spawn_tile':128, 'event_tiles':(18,19,53), 'warp_tiles': (91, 143), 'invalids': (35,41,50,
			51,52,54,55,56,102,103,117,118), 'V':15}
			
pokemon_centre_top_floor = {'battle_tiles':(), 'spawn_tile':92, 'event_tiles':(), 'warp_tiles':(91, 91), 'invalids': (76,77), 'V':15}

current_tile_map = pallet_town