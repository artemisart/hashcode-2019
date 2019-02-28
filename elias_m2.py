from utils import *
from tqdm  import tqdm

def slideshowToStr(slideshow) :
    tmp = []
    tmp.append(' ' + '\n')
    i = 0
    nbSlides = 0
    while i < len(slideshow) :
        nbSlides += 1
        if slideshow[i].vertical :
            if i+1 < len(slideshow) :
                tmp.append(str(slideshow[i].id)+" "+str(slideshow[i+1].id)+'\n')               
                i += 2  
        else :
            tmp.append(str(slideshow[i].id)+'\n')
            i += 1
    tmp[0] = str(nbSlides)+'\n'
    return ''.join(tmp)

def model(nbPhotos, photos) :
    sorted_pics = sorted(photos, key=lambda x: len(x.tags))
    slideshow = []
    used = set()
    pbar = tqdm(total = nbPhotos)
    while len(sorted_pics) > 0 :
        pbar.update(len(sorted_pics))
        p = sorted_pics.pop()
        p2 = None
        tags = p.tags
        if p.vertical :
            j = 0
            min_common = len(p.tags)
            best_sofar = None
            for pic in sorted_pics :
                if pic.vertical and pic.id != p.id :
                    common = len(tags - pic.tags)
                    if common < min_common : 
                        min_common = common
                        best_sofar = pic
                    j = j+1
                    if j > nbPhotos/4 : break

            if best_sofar != None :
                p2 = best_sofar
            else :
                p2 = next((pic for pic in sorted_pics if (pic.vertical and pic.id != p.id)), None)
            if p2 == None : continue
            else : 
                tags = tags | p2.tags
                sorted_pics.remove(p2)
        best_sofar = p
        max_common = 0
        for candidate in sorted_pics :
            if candidate.vertical : continue
            common = len(tags - candidate.tags)
            if common > max_common : 
                max_common = common
                best_sofar = candidate
                if common >= (len(tags)/2 - 1) : break
        slideshow.append(p)
        if p.vertical : slideshow.append(p2)
        if best_sofar.id != p.id :
            sorted_pics.remove(best_sofar)
            slideshow.append(best_sofar)
    print(slideshowToStr(slideshow))





