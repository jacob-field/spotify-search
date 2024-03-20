# <img src="https://www.pngall.com/wp-content/uploads/9/Spotify-Logo-PNG-Picture.png" alt="Image of spotify logo" width="25" height="25"> Spotify Search
_by Jacob Field_

## Description
- Uses the [Spotify Web API](https://developer.spotify.com/documentation/web-api) to search Spotify and return the top 5 results
- Takes a string as input and returns each song's title, artist, and release date

_Note: results will differ based on each Spotify account_

## How To Use
1. Create a **Spotify Developer** project with the **Spotify Web API** using [this setup guide](https://developer.spotify.com/documentation/web-api)

2. In Python, install `spotipy` using pip:
```python
pip install spotipy
```
or alternatively,
```python
pip install requirements.txt
```

3. In `main.py`, change the following variables `API_KEY` to your developer project's keys:
```python
CLIENT_ID = 'your client ID here'
CLIENT_SECRET = 'your client secret here'
REDIRECT_URI = 'your redirect URI here'
```
_Tip: your developer project will be located on the [developer dashboard](https://developer.spotify.com/dashboard)_

## Example Output
```
What song would you like to search for? Happy

Searching Spotify for Happy...

Result #1: NF - HAPPY                                                                  	Released on 2023-04-07
Result #2: The Weeknd - House Of Balloons / Glass Table Girls                          	Released on 2011-03-21
Result #3: Tyler, The Creator - See You Again (feat. Kali Uchis)                       	Released on 2017-07-21
Result #4: Pharrell Williams - Happy - From "Despicable Me 2"                          	Released on 2014-03-03
Result #5: elijah woods - almost happy                                                 	Released on 2022-11-18
```
