"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    
    
    This module implements functions specifically 
    for the ephem subpackage.
    
"""
import swisseph

from . import swe
from flatlib import angle
from flatlib import const
from flatlib import utils


# One arc-second error for iterative algorithms
MAX_ERROR = 0.0003


# === Object positions === #
#福点
def pfLon(jd, lat, lon,hsys,flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.
    
    """
    sun = swe.sweObjectLon(const.SUN, jd,flags)
    moon = swe.sweObjectLon(const.MOON, jd,flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys,flags)[1][0]
    
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc + moon - sun)
    else:
        return angle.norm(asc + sun - moon)
    
#精神点
def jsLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]

    if isDiurnal(jd, lat, lon):
        return angle.norm(asc - moon + sun)
    else:
        return angle.norm(asc - sun + moon)

#爱神点
def asLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    venus=swe.sweObjectLon(const.VENUS, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]

    if isDiurnal(jd, lat, lon):
        return angle.norm(asc+venus-(asc - moon + sun))
    else:
        return angle.norm(asc+(asc - sun + moon)-venus)


# 贫困点
def pkLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]
    mercury=swe.sweObjectLon(const.MERCURY, jd, flags)
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc+(asc + moon - sun)-mercury)
    else:
        return angle.norm(asc+mercury-(asc + sun - moon))

# 勇气点
def yqLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]
    mars=swe.sweObjectLon(const.MARS, jd, flags)
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc+(asc + moon - sun)-mars)
    else:
        return angle.norm(asc+mars-(asc + sun - moon))


#胜利点
def slLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    jupiter=swe.sweObjectLon(const.JUPITER, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]

    if isDiurnal(jd, lat, lon):
        return angle.norm(asc+jupiter-(asc - moon + sun))
    else:
        return angle.norm(asc+(asc - sun + moon)-jupiter)

# 报应点
def byLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.

    """
    sun = swe.sweObjectLon(const.SUN, jd, flags)
    moon = swe.sweObjectLon(const.MOON, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]
    saturn=swe.sweObjectLon(const.SATURN, jd, flags)
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc+(asc + moon - sun)-saturn)
    else:
        return angle.norm(asc+saturn-(asc + sun - moon))

#妻子点
def qzLon(jd, lat, lon, hsys, flags):
    """ Returns the ecliptic longitude of Pars Fortuna.
    It considers diurnal or nocturnal conditions.
    """
    saturn = swe.sweObjectLon(const.SATURN, jd, flags)
    venus = swe.sweObjectLon(const.VENUS, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]

    if isDiurnal(jd, lat, lon):
        return angle.norm(asc + venus - saturn)
    else:
        return angle.norm(asc + saturn - venus)
#丈夫点
def zfLon(jd, lat, lon, hsys, flags):
    venus=swe.sweObjectLon(const.VENUS, jd, flags)
    mars=swe.sweObjectLon(const.MARS, jd, flags)
    asc = swe.sweHousesLon(jd, lat, lon,
                           hsys, flags)[1][0]
    if isDiurnal(jd, lat, lon):
        return angle.norm(asc + venus-mars)
    else:
        return angle.norm(asc + mars-venus)

#正缘结婚点(male)
def jhMaleLon(jd, lat, lon, hsys, flags):
    sum_lon=0
    for planet in const.LIST_SEVEN_PLANETS:
        lon = swe.sweObjectLon(planet, jd, flags)
        sum_lon+=lon
    qiziLon=qzLon(jd, lat, lon, hsys, flags)
    return angle.norm(qiziLon+sum_lon)

#正缘结婚点(female)
def jhFemaleLon(jd, lat, lon, hsys, flags):
    sum_lon=0
    for planet in const.LIST_SEVEN_PLANETS:
        lon = swe.sweObjectLon(planet, jd, flags)
        sum_lon+=lon
    zhangfuLon=zfLon(jd, lat, lon, hsys, flags)
    return angle.norm(zhangfuLon+sum_lon)
# === Diurnal  === #
def isDiurnal_old(jd, lat, lon):
    """ Returns true if the sun is above the horizon
    of a given date and location.
    """
    # print('in isDiurnal')
    flags=swisseph.FLG_SWIEPH
    sun = swe.sweObject(const.SUN, jd,flags)
    mc = swe.sweHousesLon(jd, lat, lon,const.HOUSES_PLACIDUS,flags)[1][1]
    ra, decl = utils.eqCoords(sun['lon'], sun['lat'])
    mcRA, _ = utils.eqCoords(mc, 0.0)
    return utils.isAboveHorizon(ra, decl, mcRA, lat)

def isDiurnal(jd, lat, lon):
    flags = swisseph.FLG_SIDEREAL
    sun = swe.sweObject(const.SUN, jd, flags)
    _, ascmc = swisseph.houses_ex(jd, lat, lon, b'W',flags)
    # asc_lon = swe.sweHousesLon(jd, lat, lon, const.HOUSES_WHOLE_SIGN, flags)[1][0]
    asc_lon=ascmc[0]
    sun_lon=sun['lon']
    return angle.closestdistance(asc_lon,sun_lon)<0
# === Iterative algorithms === #

def syzygyJD(jd):
    """ Finds the latest new or full moon and
    returns the julian date of that event. 
    
    """
    # print("in syzygyJD")
    flags=0
    sun = swe.sweObjectLon(const.SUN, jd,flags)
    moon = swe.sweObjectLon(const.MOON, jd,flags)
    dist = angle.distance(sun, moon)
    
    # Offset represents the Syzygy type. 
    # Zero is conjunction and 180 is opposition.
    offset = 180 if (dist >= 180) else 0
    while abs(dist) > MAX_ERROR:
        jd = jd - dist / 13.1833  # Moon mean daily motion
        sun = swe.sweObjectLon(const.SUN, jd,flags)
        moon = swe.sweObjectLon(const.MOON, jd,flags)
        dist = angle.closestdistance(sun - offset, moon)
    return jd

def solarReturnJD(jd, lon, forward=True):
    """ Finds the julian date before or after 
    'jd' when the sun is at longitude 'lon'. 
    It searches forward by default.
    
    """
    sun = swe.sweObjectLon(const.SUN, jd,0)
    if forward:
        dist = angle.distance(sun, lon)
    else:
        dist = -angle.distance(lon, sun)
        
    while abs(dist) > MAX_ERROR:
        jd = jd + dist / 0.9833  # Sun mean motion
        sun = swe.sweObjectLon(const.SUN, jd,0)
        dist = angle.closestdistance(sun, lon)
    return jd


# === Other algorithms === #

def nextStationJD(ID, jd):
    """ Finds the aproximate julian date of the
    next station of a planet.

    """
    speed = swe.sweObject(ID, jd,0)['lonspeed']
    for i in range(2000):
        nextjd = jd + i / 2
        nextspeed = swe.sweObject(ID, nextjd,0)['lonspeed']
        if speed * nextspeed <= 0:
            return nextjd
    return None
