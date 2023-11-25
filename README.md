# DA
## installation
```
#create an environment 
python3 -m venv DA
source DA/bin/activate
pip install git+https://github.com/erosmontin/DA.git

```
## usage Example

### rt
rigid rototranslations based on itk

```
from rt.r import *

#define a 3D rototranlation array
rt=[5,5,5,0,0,0] (deg,deg,deg,mm,mm,mm) (itk rototranslation class)
RT=[rt]
# append other rototranslations if needed
RT.append([15,15,15,0,0,0])
RT.append([15,15,15,2,0,0])

#decide if you want to RT a roi, a labelmap or an image (in case multiple selected they will be RTed of the same quantity and placed in a directory specified by outputDirectory)
a summary is made in a json file



# you can also specify a refence image where all the roi,labelmap or images will be resampled

RototanslateData(labelmapFilename="tests/data/labelmap.nii.gz",imageFileName="tests/data/image.nii.gz",rototranslations=RT,outputDirectory="/tmp/TEST",referenceImageFileName=None)



```

## command line


    
[*Dr. Eros Montin, PhD*](http://me.biodimensional.com)
**46&2 just ahead of me!**

