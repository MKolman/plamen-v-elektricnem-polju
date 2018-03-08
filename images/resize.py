import Image
import glob

NEW_WIDTH = 230
images = glob.glob("CAM*.jpg")
for i in images:
    print i,
    if "_s" in i:
        print "already small"
        continue

    s_i = i.split(".")[0]
    s_i += "_s.jpg"

    if s_i in images:
        print "already has small"
        continue
    print "resizing...",
    im = Image.open(i)
    resize_factor = 1.0*NEW_WIDTH/im.size[0]
    n_size = (NEW_WIDTH, int(round(im.size[1]*resize_factor)))
    im_s = im.resize(n_size, Image.ANTIALIAS)

    im_s.save(s_i)
    print "done."

