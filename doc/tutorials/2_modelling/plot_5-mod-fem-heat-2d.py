#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Heat equation in 2D
-------------------

This tutorial simulates the stationary heat equation in 2D. The example is
taken from the pyGIMLi paper (https://cg17.pygimli.org).
"""

import pygimli as pg
import pygimli.meshtools as mt

###############################################################################
# Create geometry definition for the modelling domain.
world = mt.createWorld(start=[-20, 0], end=[20, -16], layers=[-2, -8],
                       worldMarker=False)
# Create a heterogeneous block
block = mt.createRectangle(start=[-6, -3.5], end=[6, -6.0],
                           marker=4,  boundaryMarker=10, area=0.1)
# Merge geometrical entities
geom = world + block
pg.show(geom, boundaryMarker=True)

###############################################################################
# Create a mesh from based on the geometry definition.
mesh = mt.createMesh(geom, quality=33, area=0.2, smooth=[1, 10])
pg.show(mesh)

###############################################################################
# Call :py:func:`pygimli.solver.solveFiniteElements` to solve the heat
# diffusion equation :math:`\nabla\cdot(a\nabla T)=0` with :math:`T(bottom)=1`
# and :math:`T(top)=0`, where :math:`a` is the thermal diffusivity and :math:`T`
# is the temperature distribution.
T = pg.solver.solveFiniteElements(mesh,
                                  a={1: 1.0, 2: 2.0, 3: 3.0, 4:0.1},
                                  bc={'Dirichlet': {8: 1.0, 4: 0.0}}, verbose=True)

ax, _ = pg.show(mesh, data=T, label='Temperature $T$', cMap="hot_r")
pg.show(geom, ax=ax, fillRegion=False)

# just hold figure windows open if run outside from spyder, ipython or similar
pg.wait()
