from base import *
from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'liantang',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1', 
        'PORT': '5432', 
    },
}

#GDAL_LIBRARY_PATH = r'C:\Program Files\GDAL\gdal202'
#GDAL_LIBRARY_PATH = r'C:\Program Files (x86)\GDAL\gdal202'
#GDAL_LIBRARY_PATH =r'D:\tools\release-1900-x64-gdal-2-2-3-mapserver-7-0-7\bin\gdal202'
#GDAL_DRIVER_PATH=r'D:\tools\release-1900-x64-gdal-2-2-3-mapserver-7-0-7\bin\gdal'
#GDAL_LIBRARY_PATH = 'D:\tools\release-1900-x64-gdal-2-2-3-mapserver-7-0-7\bin\gdal'