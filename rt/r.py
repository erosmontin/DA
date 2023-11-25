import pyable_eros_montin.imaginable as ima
import pyable_eros_montin.dev as dev
import pynico_eros_montin.pynico as pn
def RototanslateData(labelmapFilename=None,roifileName=None,imageFileName=None,rototranslations=[[5,5,5,0,0,0]],outputDirectory="/tmp/",referenceImageFileName=None):
    """_summary_

    Args:
        labelmapFilename (_type_, optional): _description_. Defaults to None.
        roifileName (_type_, optional): _description_. Defaults to None.
        imageFileName (_type_, optional): _description_. Defaults to None.
        rototranslations (list, optional): _description_. Defaults to [[5,5,5,0,0,0]]. (deg,deg,deg,mm,mm,mm)
        outputDirectory (str, optional): _description_. Defaults to "/tmp/".
        referenceImageFileName (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    TOROT=[]
    FILENAMES=[]
    resample=False
    if referenceImageFileName is not None:
        REFERENCE=ima.Imaginable(referenceImageFileName)
        resample=True
    
    if labelmapFilename is not None:
        L=dev.LabelMapable(labelmapFilename)
        if resample:
            L.resampleOnTargetImage(REFERENCE   )
        TOROT.append(L)
        FILENAMES.append(labelmapFilename)
    if roifileName is not None:
        L=ima.Roiable(roifileName)
        if resample:
            L.resampleOnTargetImage(REFERENCE)
        TOROT.append(L)
        FILENAMES.append(roifileName)
    if imageFileName is not None:
        L=ima.Imaginable(imageFileName)
        if resample:
            L.resampleOnTargetImage(REFERENCE)
        TOROT.append(L)
        FILENAMES.append(imageFileName)
    OUT=[]
    for n,rt in enumerate(rototranslations):
        im=[]
        for i in range(len(TOROT)):  
            TOROT[i].rotateImage(rotation=rt[:3],translation=rt[3:])
            P=pn.Pathable(FILENAMES[i])
            P.changePath(outputDirectory)
            P.appendPath(f"{n:06d}")
            P.ensureDirectoryExistence()
            filename=P.getPosition()
            TOROT[i].writeImageAs(filename=filename)
            im.append(filename)
        target="self"
        if resample:
            target=referenceImageFileName

        OUT.append({"images":im,"rototranslation":rt,"resample":target})
    
    P.changePath(outputDirectory)
    
    P.changeBaseNameSafe("rototranslations.json")
    P.writeJson(OUT)  
    return OUT

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='rototranlate an image/roi/labelmap.\npython mroptimum/r.py --roi /data/MYDATA/Eros_143TKR_143NonTKR/1_T2ValuesMaps/TKR/9071781.nii.gz --reference /data/MYDATA/Eros_143TKR_143NonTKR/3_DESS_data/TKR/9071781.nii.gz --rototranslation 0 10 0 0 0 0 --outputDirectory /g/CEMtest/')
    parser.add_argument('--labelmap', type=str, default=None,
                    help='labelmap file name')
    parser.add_argument('--roi', type=str, default=None,
                    help='roi file name')
    parser.add_argument('--image', type=str, default=None,
                    help='image file name')
    parser.add_argument('--rototranslation', type=float, nargs='+', default=[5,5,5,0,0,0],
                    help='(deg,deg,deg,mm,mm,mm)')
    parser.add_argument('--outputDirectory', type=str, default="/tmp/",
                    help='directory to save the output')
    parser.add_argument('--referenceimage', type=str, default=None,
                    help='(optional) if you want to resample all the images in a reference image space')
    args = parser.parse_args()
    RototanslateData(labelmapFilename=args.labelmap,roifileName=args.roi,imageFileName=args.image,rototranslations=[args.rototranslation],outputDirectory=args.outputDirectory)

    
    
