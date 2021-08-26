import random
# Fetches random image from unsplash
import urllib.request
import string
def get_random_image():
    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=12))
    img_file = open(f"Images/random/{file_name}.png", "w")
    img_file.write(urllib.request.urlopen('https://source.unsplash.com/user/c_v_r/800x600'))
    img_file.close()
    return file_name
