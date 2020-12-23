# List saved tags from Shazam macOS app

import os
import sqlite3


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
    SELECT artist.ZNAME, tag.ZTRACKNAME
    FROM ZSHARTISTMO artist, ZSHTAGRESULTMO tag
    WHERE artist.ZTAGRESULT = tag.Z_PK
    ORDER BY tag.ZDATE
    '''
)

for result in results:
    print b'{0} - {1}'.format(result[0], result[1])

connection.close()
