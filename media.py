import json
import os
import re

class Movie():
  """This class provides a way to store movie related information"""

  VALID_RATINGS = ["G", "PG", "PG-13", "R"]

  def __init__(self, **kwargs):
    keys = ["movie_title", "movie_storyline", "poster_image", "trailer_youtube"]
    for key in keys:
      setattr(self, key, kwargs.get(key, ""))

  def get_youtube_id(self):
    """Extract the youtube ID from the url"""
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', self.trailer_youtube)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', self.trailer_youtube)
    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                          else None)
    return trailer_youtube_id

class MovieCollection():
  """A collection of movie records"""
  def __init__(self, movies):
    self.movies = movies

  @classmethod
  def init_with_file(cls, file):
    """Initialize MovieCollection from the json file"""
    collection = []

    assert os.path.exists(file), '%s File does not exist' % file

    movie_data_file = open(file, 'r')
    movie_data = json.load(movie_data_file)

    for record in movie_data:
      movie = Movie(
        movie_title = record['title'],
        movie_storyline = record['storyline'],
        poster_image = record['poster_image_url'],
        trailer_youtube = record['trailer_youtube_url'],
      )
      collection.append(movie)

    movie_data_file.close()

    return cls(collection)
