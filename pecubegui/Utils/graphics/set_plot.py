#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is designed to plot output results in the interface. 

@author: maxime - maxime.bernard@uni-potsdam.de

"""

from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import matplotlib
import numpy as np


#-----------------------------------------------------------------------------
#-------------------------------- Functions ----------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def get_gradient_color(c1,c2,mix=0):
    """create a gradient color from color 1 to color 2. """
    c1 = np.array(matplotlib.colors.to_rgb(c1))
    c2 = np.array(matplotlib.colors.to_rgb(c2))
    return matplotlib.colors.to_hex((1-mix)*c1 + mix*c2)


def make_error_boxes(ax,xdata,ydata,xerror,yerror,facecolor='g',edgecolor='none',colorline='none',alpha=0.5,label='Portion extracted'):
    """ plot boxes for 4He/3He spectra (see oset_thermochronometers.py).
    The box integrates gas released over a finite
    heating range, rather than one exact release step point on the cumulative
    axis. The cumulative axis begins at zero and ends at one.
    Vertically, the center of each box is the measured Rstep/Rbulk, and its
    height represents the propagated uncertainty in that normalized ratio.

    xdata: observed released fraction of 3He
    ydata: observed 4He/3He ratios for each heating step
    xerror: error in the released fraction of 3He
    yerror: error in the 4He/3He ratios
    """

    # Get left and right boundaries of each box
    right_boundaries = xdata.values
    left_boundaries = np.zeros(np.size(xdata.values))
    left_boundaries[1:] = right_boundaries[:-1]
    left_boundaries[0] = 0.0
    
    # Build each box from the cumulative release boundaries.  The y error is
    # represented symmetrically around the measured ratio.
    errorboxes = [Rectangle((left, y - ye), right - left, 2 * ye)
                  for left, right, y, ye in zip(
                      left_boundaries, right_boundaries, ydata.values, yerror.values)]
    # Keep the fill translucent while drawing the box edges fully opaque.
    fill_color = matplotlib.colors.to_rgba(facecolor, alpha=0.5)
    border_color = matplotlib.colors.to_rgba(edgecolor, alpha=1.0)
    pc = PatchCollection(errorboxes, facecolor=fill_color,
                         edgecolor=border_color, label=label)
    
    # Add collection to axes
    ax.add_collection(pc)

    # Plot each measured ratio across the full width of its corresponding box.
    line_x = np.column_stack((left_boundaries, right_boundaries)).ravel()
    line_y = np.repeat(ydata.values, 2)
    ax.plot(line_x, line_y, color=colorline, alpha=1.0, label=label)
    ax.set_xlim(left_boundaries[0], right_boundaries[-1])