# Movie Trailer Website
This is a collection movies website that displays box art imagery and movie trailers. The python code generate a static web page.

## Pre-requisites
- Python 2.7

## Getting started
Execute the command:
```
python entertainment_center.py
```

### Aditional options
* -d, --data FILENAME (default: data.json)

The file content is a JSON array. An example of this file content is:
``` json
[
  {
    "title": "movie title",
    "storyline": "movie storyline",
    "poster_image_url": "poster image URL",
    "trailer_youtube_url": "trailer URL"
  }
]
```

* -o, --output FILENAME (default: output.html)

## License
It is free software, and may be redistributed under the terms specified in the [LICENSE](/LICENSE) file.
