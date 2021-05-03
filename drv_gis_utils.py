# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:08:40 2020

@author: solis
"""

from time import time
import traceback
import littleLogging as logging
import gis_utils as gis


if __name__ == "__main__":

    try:
        startTime = time()

        # something to do
        lat_lon = [['373604N', '005916W'],['374642N', '004821W']]
        xysp = gis.geographics2proyected(4258, 25830, lat_lon)
        print(xysp)


    except ValueError:
        msg = traceback.format_exc()
        logging.append(msg)
    except Exception:
        msg = traceback.format_exc()
        logging.append(msg)
    finally:
        logging.dump()
        xtime = time() - startTime
        print(f'El script tardó {xtime:0.1f} s')
