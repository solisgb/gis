# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:44:18 2021

@author: solis
"""
import pyproj as proj
import numpy as np


def geographics2proyected(crsg, crsp, lat_lon):
    """
    Transforms a list of geographic coordinates xyg from geographic
    coordinate reference system crsg to a proyected crsp one
    Parameters
    ----------
    crsg : int
        geographic coordinate reference system
    crsp : int
        proyected coordinate reference system
    lat_lon : List of lists of str (latitude, longitude)
        latitude is a str with the format DDMMSSC
        longitude is a str with the format DDMMSSC
        where DD degres, MM minutes, SS seconds and C is a cardinal direction:
        N, S, E, W
    Returns
    -------
    xyp List of list of [x, y] in the projected crsp
    """

    if proj.crs.CRS(crsg).is_projected:
        raise ValueError(f'crs {crsg:d} is not geographic')
    if proj.crs.CRS(crsp).is_geographic:
        raise ValueError(f'crs {crsp:d} is not projected')
    transformer = proj.Transformer.from_crs(crsg, crsp)
    xyp = np.empty((len(lat_lon), 2), np.float32)
    for i, lat_lon1 in enumerate(lat_lon):
        for j, item in enumerate(lat_lon1):
            dg = float(item[0:2])
            mn = float(item[2:4])
            sc = float(item[4:6])
            d = item[6:7]
            if j == 0:
                if d not in 'NS':
                    raise ValueError (f'{item} is not a longiude')
                lat_deg = dg + (mn/60) + (sc/3600)
                if d == 'S':
                    lat_deg = -1. * lat_deg
            else:
                if d not in 'WE':
                    raise ValueError (f'{item} is not a latitude')
                lon_deg = dg + mn/60 + sc/3600
                if d == 'W':
                    lon_deg = -1. * lon_deg
                xp1, yp1 = transformer.transform(lat_deg, lon_deg)
                xyp[i,:] = [xp1, yp1]
    return xyp.tolist()


