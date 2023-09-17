"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements functions for retrieving 
    astronomical and astrological data from an ephemeris.
    
    It is as middle layer between the Swiss Ephemeris 
    and user software. Objects are treated as python 
    dicts and jd/lat/lon as float.
  
"""

from . import swe
from . import tools
from flatlib import angle
from flatlib import const


# === Objects === #

def getObject(ID, jd, lat, lon,hsys,flags):
    """ Returns an object for a specific date and 
    location.
    
    """
    if ID == const.SOUTH_NODE:
        obj = swe.sweObject(const.NORTH_NODE, jd,flags)
        obj.update({
            'id': const.SOUTH_NODE,
            'lon': angle.norm(obj['lon'] + 180)
        })

        # PARS_FORTUNA,
        # PARS_JINGSHEN,
        # PARS_AISHEN,
        # PARS_PINKUN,
        # PARS_YONGQI,
        # PARS_SHENGLI,
        # PARS_BAOYING
    elif ID == const.PARS_FORTUNA:
        # print(f"fortuna:{flags}")
        pflon = tools.pfLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': pflon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID==const.PARS_JINGSHEN:
        jslon=tools.jsLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID==const.PARS_AISHEN:
        jslon=tools.asLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID==const.PARS_PINKUN:
        jslon=tools.pkLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif ID==const.PARS_YONGQI:
        jslon=tools.yqLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif ID==const.PARS_SHENGLI:
        jslon=tools.slLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif ID==const.PARS_BAOYING:
        jslon=tools.byLon(jd, lat, lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jslon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    #Qizi,Zhangfu
    elif ID==const.PARS_QIZI:
        qzlon=tools.qzLon(jd,lat,lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': qzlon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID==const.PARS_ZHANGFU:
        zflon=tools.zfLon(jd,lat,lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': zflon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif ID==const.PARS_JIEHUNDIAN_MALE:
        jhlon=tools.jhMaleLon(jd,lat,lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jhlon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }
    elif ID==const.PARS_JIEHUNDIAN_FEMALE:
        jhlon=tools.jhFemaleLon(jd,lat,lon,hsys,flags)
        obj = {
            'id': ID,
            'lon': jhlon,
            'lat': 0,
            'lonspeed': 0,
            'latspeed': 0
        }

    elif ID == const.SYZYGY:
        szjd = tools.syzygyJD(jd)
        obj = swe.sweObject(const.MOON, szjd,flags)
        obj['id'] = const.SYZYGY
    else:
        obj = swe.sweObject(ID, jd,flags)
    
    _signInfo(obj)
    return obj


# === Houses === #

def getHouses(jd, lat, lon, hsys,flags):
    """ Returns lists of houses and angles. """
    houses, angles = swe.sweHouses(jd, lat, lon, hsys,flags)
    for house in houses:
        _signInfo(house)
    for angle in angles:
        _signInfo(angle)
    return (houses, angles)


# === Fixed stars === #

def getFixedStar(ID, jd,flags):
    """ Returns a fixed star. """
    star = swe.sweFixedStar(ID, jd,flags)
    _signInfo(star)
    return star


# === Solar returns === #

def nextSolarReturn(jd, lon):
    """ Return the JD of the next solar return. """
    return tools.solarReturnJD(jd, lon, True)

def prevSolarReturn(jd, lon):
    """ Returns the JD of the previous solar return. """
    return tools.solarReturnJD(jd, lon, False)


# === Sunrise and sunsets === #
    
def nextSunrise(jd, lat, lon):
    """ Returns the JD of the next sunrise. """
    return swe.sweNextTransit(const.SUN, jd, lat, lon, 'RISE')

def nextSunset(jd, lat, lon):
    """ Returns the JD of the next sunset. """
    return swe.sweNextTransit(const.SUN, jd, lat, lon, 'SET')

def lastSunrise(jd, lat, lon):
    """ Returns the JD of the last sunrise. """
    return nextSunrise(jd - 1.0, lat, lon)

def lastSunset(jd, lat, lon):
    """ Returns the JD of the last sunset. """
    return nextSunset(jd - 1.0, lat, lon)


# === Stations === #

def nextStation(ID, jd):
    """ Returns the aproximate jd of the next station. """
    return tools.nextStationJD(ID, jd)


# === Other functions === #

def _signInfo(obj):
    """ Appends the sign id and longitude to an object. """
    lon = obj['lon']
    obj.update({
        'sign': const.LIST_SIGNS[int(lon / 30)],
        'signlon': lon % 30
    })
