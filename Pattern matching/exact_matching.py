
from cgr_code import File_method
import cv2
import numpy as np


def orb_similarity(img1, img2):

    orb= cv2.ORB_create()
    kp_a, desc_a= orb.detectAndCompute(img1, None)
    kp_b, desc_b= orb.detectAndCompute(img2, None)

    bf= cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches= bf.match(desc_a, desc_b)
    similar_regions= [i for i in matches if i.distance < 60]
    
    if len(matches)==0:
        return 0
    return len(similar_regions)/len(matches)

def calculate_score(img1, img2):

    similarity= orb_similarity(img1, img2)
    
    threshold= 0.10
    if similarity > threshold:
        return 'Matching is found with confidence {}%, using threshold 10%'.format(similarity*100)
    else:
        return 'Matching is not found, using threshold 10%'

if __name__ == "__main__":
    ref_file_name= File_method()
    pattern_file_name= File_method()

    ref_img= cv2.imread('{}.png'.format(ref_file_name), 0)
    pattern_img= cv2.imread('{}.png'.format(pattern_file_name), 0)

    handling= calculate_score(ref_img, pattern_img)
    print(handling)   

    diff_img= cv2.absdiff(ref_img, pattern_img)
    cv2.imshow('The difference indication between the 2 images', diff_img)

    cv2.waitKey()
    cv2.destroyAllWindows()
