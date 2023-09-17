import swisseph
import flatlib
from ephem import swe
from flatlib.datetime import Datetime
from ephem import tools
from flatlib.geopos import GeoPos
import const
# Set default swefile path
swe.setPath(flatlib.PATH_RES + 'swefiles')

swisseph.set_ephe_path()
date = Datetime(f'{2022}/{11}/{1}', f'{5}:{12}', 10)
pos = GeoPos('35s12','150e33')

# print(date.jd)
# flags=swisseph.FLG_TROPICAL
# print(tools.syzygyJD(111111,0))
# print(tools.syzygyJD(date.jd,0))
# print(tools.syzygyJD(date.jd,swisseph.FLG_SWIEPH))
# print(tools.syzygyJD(date.jd,swisseph.FLG_SIDEREAL))
# print(tools.isDiurnal(date.jd,pos.lat,pos.lon,0))
# print(tools.isDiurnal(date.jd,pos.lat,pos.lon,swisseph.FLG_SWIEPH))
# print(tools.isDiurnal(date.jd,pos.lat,pos.lon,swisseph.FLG_SIDEREAL|swisseph.FLG_SWIEPH))
# print(tools.isDiurnal(date.jd,pos.lat,pos.lon,swisseph.FLG_NONUT|swisseph.FLG_SWIEPH))

# star = swe.sweFixedStar("Aldebaran", date.jd,0)
# print(star)