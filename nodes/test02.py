import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import measure, feature, exposure, segmentation, color, graph, img_as_float
from skimage.util import random_noise
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage.morphology import convex_hull_image
from skimage.util import invert
from skimage.feature import hog
from skimage.feature import peak_local_max
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)
from skimage.color import label2rgb
from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import expand_labels, watershed
from skimage.morphology import disk
from skimage.segmentation import watershed
from skimage import data, io
from skimage.filters import rank
from skimage.util import img_as_ubyte
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)

import cv2 as cv

from PIL import Image
import numpy as np
from pathlib import Path

from custom_nodes.comfyui_ricklove.nodes.ext.TemporalKit.optical_flow_raft import (apply_flow_based_on_images)

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    img_arr = np.array(img) #are all you need
    # print(img_arr.shape)
    # plt.imshow(img_arr)
    # plt.show()
    # data = np.asarray( img, dtype="int32" )
    return img_arr

def apply_flow(to_index, from_index):
    # img_from = f"D:/Projects/ai/data/unclean/lz-01/lz-01-enhanced/video/out{from_index:05}.png"
    # img_to = f"D:/Projects/ai/data/unclean/lz-01/lz-01-enhanced/video/out{to_index:05}.png"
    # img_from_ref = f"D:/Projects/ai/data/unclean/lz-01/lz-01-enhanced/video/out{from_index:05}.png"
    # # img_from_ref = f"D:/Projects/ai/data/unclean/lz-01/lz-01-enhanced/keys/seq_{from_index:05}.png"
    # output_path = f"D:/Projects/ai/data/unclean/lz-01/lz-01-enhanced/_out_test/w{to_index:05}_{from_index:05}.png"

    # img_from = f"D:/Projects/ai/data/unclean/lz-13/IMG_5804/video/out{from_index:05}.png"
    # img_to = f"D:/Projects/ai/data/unclean/lz-13/IMG_5804/video/out{to_index:05}.png"
    # img_from_ref = f"D:/Projects/ai/data/unclean/lz-13/IMG_5804/video/out{from_index:05}.png"
    # # img_from_ref = f"D:/Projects/ai/data/unclean/lz-13/IMG_5804/keys/seq_{from_index:05}.png"
    # output_path = f"D:/Projects/ai/data/unclean/lz-13/IMG_5804/_out_test/w{to_index:05}_{from_index:05}.png"

    # img_from = f"D:/Projects/ai/data/unclean/lz-50/IMG_8416/video/out{from_index:05}.png"
    # img_to = f"D:/Projects/ai/data/unclean/lz-50/IMG_8416/video/out{to_index:05}.png"
    # # img_from_ref = f"D:/Projects/ai/data/unclean/lz-50/IMG_8416/video/out{from_index:05}.png"
    # img_from_ref = f"D:/Projects/ai/data/unclean/lz-50/IMG_8416/keys/seq_{from_index:05}.png"
    # output_path = f"D:/Projects/ai/data/unclean/lz-50/IMG_8416/_out_test/w{to_index:05}_{from_index:05}.png"


    img_from = f"D:/Projects/ai/data/unclean/kn-05/MVI_3833/video/out{from_index:05}.png"
    img_to = f"D:/Projects/ai/data/unclean/kn-05/MVI_3833/video/out{to_index:05}.png"
    # img_from_ref = f"D:/Projects/ai/data/unclean/kn-05/MVI_3833/video/out{from_index:05}.png"
    img_from_ref = f"D:/Projects/ai/data/unclean/kn-05/MVI_3833/seq_blend/seq_blend_{from_index:05}.png"
    output_path = f"D:/Projects/ai/data/unclean/kn-05/MVI_3833/_out_test/w{to_index:05}_{from_index:05}.png"

    if Path(output_path).exists():
        print(f'apply_flow: SKIPPING {output_path}')
        return output_path

    apply_flow_based_on_images(img_from, img_to, img_from_ref, output_path)


i_first = 1
i_last = 20
r = 5

for to_index in range(i_first,i_last+1):
    for from_index in range(to_index-r,to_index+r+1):
        if from_index < i_first: continue
        if from_index > i_last: continue
        apply_flow(to_index,from_index)


# apply_flow(3,1)
# apply_flow(3,2)
# # apply_flow(3,3)
# apply_flow(3,4)
# apply_flow(3,5)
# apply_flow(3,6)
# apply_flow(3,7)
# apply_flow(3,8)
# apply_flow(3,9)

# apply_flow(7,1)
# apply_flow(7,2)
# apply_flow(7,3)
# apply_flow(7,4)
# apply_flow(7,5)
# apply_flow(7,6)
# # apply_flow(7,7)
# apply_flow(7,8)
# apply_flow(7,9)
# apply_flow(7,10)
# apply_flow(7,11)
# apply_flow(7,12)
# apply_flow(7,13)
