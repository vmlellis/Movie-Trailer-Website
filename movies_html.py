import os
import webbrowser

def create_movie_tiles_content(movies):
  """Generates the HTML content for this section of the page"""
  file = open('templates/movie_tile.tpl', 'r')
  movie_tile_content = file.read()
  file.close()

  content = ''

  for movie in movies:
    trailer_youtube_id = movie.get_youtube_id()

    # Append the tile for the movie with its content filled in
    content += movie_tile_content.format(
      movie_title = movie.movie_title,
      poster_image_url = movie.poster_image,
      trailer_youtube_id = trailer_youtube_id
    )

  return content

def head_content():
  '''Generates the head HTML content'''
  file = open('templates/head.tpl', 'r')
  content = file.read()
  file.close()
  return content

def body_content(movies):
  '''Generates the body HTML content'''
  file = open('templates/body.tpl', 'r')
  content = file.read()
  file.close()
  return content.format(movie_tiles = create_movie_tiles_content(movies))

def create_page_content(movies):
  '''Generates the HTML content'''
  content = '<!DOCTYPE html><html lang="en">{head}{body}</html>'
  return content.format(head = head_content(), body = body_content(movies))

def open_page(movies, output):
  """Create and open output page from movies list"""

  # Output the file
  output_file = open(output, 'w')
  output_file.write(create_page_content(movies))
  output_file.close()

  # open the output file in the browser (in a new tab, if possible)
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new = 2)
