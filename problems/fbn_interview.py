from collections import namedtuple

'''basically, given a class and a particular image (that looks like a maze)
we want to know whether

'''
class pixel_location(namedtuple):
    x = int()
    y = int()

# black=0
# white=1
# image is a list of rows
#image is a set of pixel_locations
# i think image is a list of rows 0f pixel_locations 
# that can be either black or white 
# 
# #start and end are x,y location coordinates

def isPossible(image, start, end):
    visited= set()
    width = len(image)
    height = len(image[0])
    '''
    1 do all the checks.
    a.  check to see if a given position is in the image
        aa. need to check if any are 0 (4 checks)
        aa. check if start_location.x > height
    then check if any are black
    b. check to see start_location.x  == 0
    bb check to see start_location.y == =0 

3 recursive call  we need to do  4 checks
pixel_location.x + 1, pixel_location.y
pixel_location.x - 1, pixel_location.y
pixel_location.x 1, pixel_location.y+1
pixel_location.x, pixel_location.y



    '''

