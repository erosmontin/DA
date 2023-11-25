from rt.r import *


RT=[[5,5,5,0,0,0]]
RT.append([15,15,15,0,0,0])
RT.append([15,15,15,2,0,0])

RototanslateData(labelmapFilename="tests/data/labelmap.nii.gz",imageFileName="tests/data/image.nii.gz",rototranslations=RT,outputDirectory="/tmp/TEST",referenceImageFileName=None)