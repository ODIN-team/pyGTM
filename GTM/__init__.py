#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This program implements the generalized 4x4 transfer matrix (GTM) method poposed in 
Passler, N. C. and Paarmann, A., JOSA B 34, 2128 (2017) doi.org/10.1364/JOSAB.34.002128
and corrected in <DOI to be inserted>, with inputs from D. Dietze's FSRStools code
https://github.com/ddietze/FSRStools

Please cite the associated publications if you use this code. 

author: Mathieu Jeannin <math.jeannin@free.fr> (permanent)
affiliation: Laboratoire de Physique de l'Ecole Normale Superieure (2019)

..
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    Copyright (C) Mathieu Jeannin 2019 <math.jeannin@free.fr>.
    
"""