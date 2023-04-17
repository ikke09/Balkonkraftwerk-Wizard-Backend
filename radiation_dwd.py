import numpy as np

from models import Coords

import pyproj


def wgs84_to_gk(lon, lat):
    # WGS84 Koordinatenreferenzsystem
    wgs84 = pyproj.Proj('EPSG:4326')
    # GK Koordinatenreferenzsystem
    gk = pyproj.Proj('EPSG:31467')
    # Umrechnung von WGS84 nach GK
    easting, northing = pyproj.transform(wgs84, gk, lon, lat)
    return easting, northing


def get_globalstrahlung(coordinates: Coords) -> float | None:

    # Pfad zur ASC-Datei
    asc_file = 'grids_germany_annual_radiation_global_2022.asc'
    data = None
    # Einlesen der ASC-Datei
    with open(asc_file, 'r') as f:
        # Lesen der Header-Informationen
        ncols = int(f.readline().split()[1])
        nrows = int(f.readline().split()[1])
        xllcorner = float(f.readline().split()[1])
        yllcorner = float(f.readline().split()[1])
        cellsize = float(f.readline().split()[1])
        nodata_value = float(f.readline().split()[1])

        # Einlesen der Rasterdaten
        data = np.loadtxt(f, dtype=np.float32, delimiter=' ')

        # Umformen der Daten in eine 2D-Array-Form
        data = data.reshape((nrows, ncols))

        # Setzen der NoData-Werte auf NaN
        data[data == nodata_value] = np.nan

        # Invertieren des Arrays, um die Ausrichtung zu korrigieren
        data = np.flipud(data)

    if data is None:
        return None

    east, north = wgs84_to_gk(coordinates.longitude, coordinates.latitude)
    col_index = int((xllcorner - east) / cellsize)
    row_index = int((north - yllcorner) / cellsize)
    value = data[row_index, col_index]
    # Ausgabe der Dimensionen des Arrays
    return value


if __name__ == "__main__":
    get_globalstrahlung(Coords(latitude=49.176, longitude=9.507))
