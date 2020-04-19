# Shazam tags

This Python script lists your saved tags from the Shazam macOS app.
Shazam for macOS doesn't have an option to save your tags, but stores its data in a SQLite database
located in one of these places:
```
~/Library/Containers/com.shazam.mac.Shazam/Data/Documents/ShazamDataModel.sqlite
~/Library/Group Containers/*.group.com.shazam/com.shazam.mac.Shazam/ShazamDataModel.sqlite
```

### Usage

To list the tags run:
```
$ python shazam-tags.py

Nova Nova - Prisoner Song (Extended Origina Mix)
Amadou & Mariam - Ce N'est Pas Bon (Ajd Twitch Edit)
Wu Tang Clan - Bring Me Da Ruckus
Eazy-E - Real Muthaphuckkin' G's
```

Or store the output to a file:
```
$ python shazam-tags.py > playlist.txt
```
