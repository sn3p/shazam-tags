# List saved tags from Shazam macOS app

import os
import sqlite3

db_path = os.path.expanduser('~/Library/Containers/com.shazam.mac.Shazam/Data/Documents/ShazamDataModel.sqlite')

connection = sqlite3.connect(db_path)
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
    print '{0} - {1}'.format(result[0], result[1])

connection.close()
