import media
import movies_html

from optparse import OptionParser

def compile():
  """Compile movie trailer website"""

  parser = OptionParser()

  parser.add_option("-d", "--data", dest="file",
    help="import data from json FILE", default="data.json")
  parser.add_option("-o", "--output", dest="output",
    help="write html to FILE", default="output.html")

  (options, args) = parser.parse_args()

  movies = media.MovieCollection.init_with_file(options.file).movies
  movies_html.open_page(movies, options.output)

compile()
