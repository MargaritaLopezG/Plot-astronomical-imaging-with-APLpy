## Code created by Martha Margarita López Gutiérrez ##

import numpy 
import aplpy
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib_scalebar.scalebar import ScaleBar
from astropy.wcs import WCS
from astropy.io import fits
from skimage.transform import resize


# Create a figure and a set of subplot
rgu = ['Files/A2670_G38_iPanS_2.fits','Files/A2670_G38_rPanS_2.fits', 'Files/A2670_G38_gPanS_2.fits']
aplpy.make_rgb_image(rgu,'Files/output/A2670_G38_color.png', vmin_b=0., vmax_b=18., vmin_g=0., vmax_g=50., vmin_r=0., vmax_r=88.)

## Coordinate base image (HI moment 0)
filename = 'Files/output/A2670_G38_mom0_b2.fits'
hdu = fits.open(filename)[0]
wcs = WCS(hdu.header)
image_data = hdu.data
#hdu.header # see header

fig = plt.figure(figsize=(8.2,8))
ax = plt.subplot(projection=wcs,  slices=('x', 'y', 1),aspect = 'equal')
plt.subplots_adjust(left=0.15, bottom=0.12, right=1.1, top=0.98, wspace=0.1, hspace=0.1)

##### Poner la imagen de fondo ####


img = plt.imread('A2670_rgu/A2670_32_color.png')
img_flip = numpy.flipud(img)#la funcion numpy.flipud voltea la imagen
ax.imshow(img_flip) 

#### Poner los contornos #######

ax.contour(image_data[0,:,:],levels=[14.2, 71, 127.8,  184.6 ], colors='white', alpha=0.8)

ax.coords[0].set_axislabel('R.A. (2000.0)', fontsize=22)
ax.coords[1].set_axislabel('Dec. (2000.0)', fontsize=22)
ax.tick_params(direction='in', color='white', fontsize=22, which='both')
ax.text(0.4, 0.95,r'PGC 141225', fontsize=24, color='white', horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)


#BEAM (optional)
#e = mpl.patches.Ellipse((0.12, 0.15), 0.13, 0.2, color='w', fill=False, transform=ax.transAxes) #BEAM (24' x 17') 
#ax.add_patch(e)
#r = mpl.patches.Rectangle((0.035, 0.03), 0.17,0.25, color='w', fill=False, transform=ax.transAxes)
#ax.add_patch(r)


plt.rcParams.update(res,{'font.size': 22})
plt.show()
# Save the plot
#plt.savefig('Files/output/SDSS_J235619-101246_irg_cont_mom0_v3.png')




