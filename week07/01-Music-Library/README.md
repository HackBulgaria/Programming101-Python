# A Music Library

We are going to implement a music library + crawler for the music on our computer.

## Songs

First, we are going to need a `Song` class which we want to initialize like that:

```python
s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
```

**Length can have hours!:**

Those are all valid lengths:

* `"3:44"`
* `"1:30:44"`


The methods we want for our `Song` are:

* `__str__` - should be able to turn the song into the following string: `"{artist} - {title} from {album} - {length}"`
* Our `Song` should be hashabe! Implement `__eq__` and `__hash__`
* `length(seconds=True)` should return the length in seconds.
* `length(minutes=True)` should return the length in minutes (omit the seconds)
* `length(hours=True)` should return the length in hours (omit minutes and seconds that does not add up to a full hour)
* `length()` should return the string representation of the length

## Playlist class

We are going to implement a collection for our songs.

The playlist should be initialized with a name:

```python
code_songs = Playlist(name="Code", repeat=True, shuffle=True)
```

* `repeat` should be defaulted to `False`
* `shuffle` should be defaulted to `False`

The `Playlist` should behave like that:

* `add_song(song)` and `remove_song(song)` are self explanatory.
* `add_songs(songs)` should add a list of `songs`.
* `total_length()` should return a string representation of tha total length of all songs in the playlist
* `artists()` - returns a histogram of all artists in the playlist. For each artist, we must have the count of songs in the playlist.
* `next_song()` should return a `Song` instance from the order of the playlist. If `repeat=True`, when our playlist reaches the end, it should loop back again at the beginning. If `shuffle=True`, everytime we call `next_song()`, we should get a different song. **Make it randomize so it wont repeat a played song unless every song from the playlist has been played!**
* `pprint_playlist()` should print the playlist to the console in a table-like view. Here is an example:

```
| Artist  | Song             | Length |
| --------|------------------|--------|
| Manowar | Odin             | 3:44   |
| Manowar | The Sons of Odin | 6:26   |
```

## Saving and Loading the playlist

We should be able to save and load a playlist to a JSON file.

* `save()` should be a instance method, that saves the playlist to a JSON filed, which has the name of the playlist. If the name has whitespaces in it, replace them with `"-"` - the so-called dasherize.
* `load(path)` should be a `@staticmethod` that returns a new `Playlist` instance.

Example usage:

```python
code = Playlist("For Code")
# ... adding songs ...

# Saves to For-Code.json
code.save()
```

Later on:

```python
code = Playlist.load("For-Code.json")
code.name == "For Code" # True
```

Save the `*.json` files in a specified folder, for instance, called `playlist-data`. Make the `load` function look there too.

## MusicCrawler

Create a `MusicCrawler` class that creates playlists and songs objects from real files on your file system. Most of .mp3 and .ogg files have tags that describe them. Tags hold information about the title, artist, album etc. Our task is to crawl a directory full of .mp3 or .ogg files and create a new playlist by reading the files' tags.

__We recommend you [mutagen](http://mutagen.readthedocs.org/en/latest/#) to read audio metadata__

Example:

```python
>>> crawler = MusicCrawler("/home/ivaylo/Music/")
>>> playlist = crawler.generate_playlist()
```

As you see, the constructor takes only one argument - the `path` of the directory from which you should read all the audio files.

`generate_playlist()` method craws all the files and returns a new playlist full of songs.

## MusicPlayer *

**This is a hard problem. Solve only if you want to.**

If you want to make this program usable you should implement a console interface for it. __You don't have to test this class!__ Implement this in the way you like it. Make it as user friendly as a console can be. 

This class should only parse user commands and call methods from the above classes.

In order to play music from the console, you can use whatever you want to use on the internet!
