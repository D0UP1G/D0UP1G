from fuzzywuzzy import fuzz
from fuzzywuzzy import process

text = 'привет'

print(fuzz.ratio(text, 'привет'))
