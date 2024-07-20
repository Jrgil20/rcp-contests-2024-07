first_line = input().split(' ')

m = first_line[0]
n = first_line[1]
number_glyph_words = first_line[2]

grid = []

for i in range(m):
  row = input.split(' ')
  grid.append(row)


glyph_words = []
for i in range(number_glyph_words):
  word = input.split('')
  glyph_words.append(word)

# Returns the first tile where i should step on the first row
def stepOnFirstTile(glyph_words):
  for i in range(n):
    if (grid[0][i] == glyph_words[0][0]):
      return i

  return -1

def theresARoute(glyph_words):
  first_tile_number = stepOnFirstTile(glyph_words)
  if (first_tile_number == -1):
    print('impossible')
    return
  
  i_tile = 0
  j_tile = first_tile_number
  getRoute(i_tile, j_tile, glyph_words)

def getRoute(i_tile, j_tile, glyph_words):
  if(grid[i_tile][j_tile] != letter):
    return 'imposible'

  return getRoute()