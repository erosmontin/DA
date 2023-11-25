# DA
## Cite us

<div>
<div style="background-color: lightgray; padding: 10px">
<span style="color: black;">
Montin E, Kijowski R, Youm T, Lattanzi R. A radiomics approach to the diagnosis of femoroacetabular impingement. Front Radiol. 2023;3:1151258. Published 2023 Mar 20. doi:10.3389/fradi.2023.1151258
<div>
</div>
</div>




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


## outputs
N diretories where N is the number of RT requested
and json file that summrize the RT

in the form of
[{"images": ["/g/CEMtest/000000/9071781.nii.gz"], "rototranslation": [0.0, 10.0, 0.0, 0.0, 0.0, 0.0], "resampled": "self"}]


    
[*Dr. Eros Montin, PhD*](http://me.biodimensional.com)
**46&2 just ahead of me!**

