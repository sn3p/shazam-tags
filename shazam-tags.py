# List saved tags from Shazam macOS app

import os
import sqlite3


# Field Delimiter
delimiter = ' - '   # Default
db_path = os.path.expanduser(
    '~/Library/Containers/com.shazam.mac.Shazam/Data/Documents/ShazamDataModel.sqlite'
)
if not os.path.exists(db_path):
    db_prefix = os.path.expanduser('~/Library/Group Containers/')
    for child in os.listdir((db_prefix)):
        if not child.endswith('.group.com.shazam'):
            continue
        db_path_ = os.path.join(db_prefix, child, 'com.shazam.mac.Shazam/ShazamDataModel.sqlite')
        if os.path.exists(db_path_):
            db_path = db_path_
            break

if not db_path:
    raise UserWarning("Could not find Shazam Database")

connection = sqlite3.connect(db_path)
connection.text_factory = lambda x: x
cursor = connection.cursor()
results = cursor.execute(
    '''
    SELECT tag.Z_PK as Id, strftime('%Y-%m-%d', datetime(tag.ZDATE + 946684800 + 31536000, 'unixepoch')) as TagTime, tag.ZTRACKNAME as Title, artist.ZNAME as Artist, tag.ZSHAZAMSERVERTRACKURL as URL, tag.ZPRIVATETRACKKEY as TrackKey
    FROM ZSHARTISTMO artist, ZSHTAGRESULTMO tag
    WHERE artist.ZTAGRESULT = tag.Z_PK
    ORDER BY tag.ZDATE
    '''
)

names = [description[0] for description in cursor.description]
print delimiter.join(names)

for row in results:
    print delimiter.join(str(field) for field in row)

connection.close()
