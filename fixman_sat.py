# -*- coding: utf-8 -*-
import os

from LibTools.filesystem import Carpeta
from slaves import Fixman

import settings

if __name__ == '__main__':

    abspath = os.path.join(settings.folder_sat, "procesadas")

    carpeta = Carpeta(abspath)
    Fixman.reload_Files_v3(carpeta)
