## Code created by Martha Margarita López Gutiérrez ##

import aplpy
import numpy
import matplotlib
from matplotlib import pyplot as plt
from astropy import wcs

# Create a figure and a set of subplot
fig = plt.figure(figsize=(7,6.5))
plt.subplots_adjust(left=0.15, bottom=0.08, right=0.98, top=0.98, wspace=0.1, hspace=0.1)

# Coordinate base image
gc = aplpy.FITSFigure('Files/2MASX_J004136-085933_DesiLegacy-g2.fits',figure=fig)

# Produce a 'rgu color image' from three bands of astronomical images 
rgu = ['Files/2MASX_J004136-085933_DesiLegacy-z2.fits','Files/2MASX_J004136-085933_DesiLegacy-r2.fits', 'Files/2MASX_J004136-085933_DesiLegacy-g2.fits']
aplpy.make_rgb_image(rgu,'Files/2MASX_J004136-085933_DesiLegacy_2_color.png', vmin_b=0., vmax_b=0.06, vmin_g=0., vmax_g=0.1, vmin_r=0., vmax_r=0.2)

# Show the previous 'rgu color image' created
gc.show_rgb('Files/2MASX_J004136-085933_DesiLegacy_2_color.png')

# Tick label parameters
gc.tick_labels.set_font(size='medium')
plt.tick_params(direction='in', fontsize=11)
gc.ticks.set_color('white')                         

# Scalebar parameters
#gc.add_scalebar(30/3600.) #The length of the scalebar in degrees. Example: here is 30 arcsec
#gc.scalebar.set_label('330 parsec')# scalebar name. Example: 30"=332 pc 
gc.scalebar.set_color('white') 
gc.scalebar.set_font_size(14)

# Label parameters
gc.axis_labels.set_xtext('R.A.(2000.0)')
gc.axis_labels.set_ytext('Dec. (2000.0)')  
gc.axis_labels.set_font(size='11')  
gc.add_label(0.8, 0.95, '2MASX J00413620-085933', relative=True, color='white', fontsize=14) 
      
plt.rcParams.update({'font.size': 14})
plt.show()
# Save the plot
#plt.savefig('Files/2MASX_J00413620-085933_DesiLegacy-zrg_2.png')
