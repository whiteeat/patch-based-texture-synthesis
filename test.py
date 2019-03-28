from patchBasedTextureSynthesis import patchBasedTextureSynthesis

if __name__ == '__main__':
    # PARAMS
    exampleMapPath = "imgs/test.png"
    outputPath = "out/test/"
    patchSize = 50  # size of the patch (without the overlap)
    overlapSize = 10  # the width of the overlap region
    outputSize = [512, 512]

    pbts = patchBasedTextureSynthesis(exampleMapPath, outputPath, outputSize, patchSize, overlapSize,
                                      in_windowStep=5, in_mirror_hor=True, in_mirror_vert=True, in_shapshots=False)

    pbts.resolveAll()
