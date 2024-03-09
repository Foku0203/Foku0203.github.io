<<<<<<< HEAD
import diffusers
    
from diffusers import DiffusionPipeline as DP
from PIL import Image,ImagDraw, ImagefFront

def text_to_image(text,diffuser_model):
    #defuser = diffuser.lodad_iffuser(diffuser_model)
    #image_data -= diffuser.genrete(textimg)
    #image = Image.fromarray(image_data)
    #image.show()
    df = DP.from_pretrained("runwayml/stable-diffusion-v1-5")

    
if __name__=="__main__":
    input_text = "Hello,World"
    diffuser_model = "exmple_diffuser_model"
=======
import diffusers
    
from diffusers import DiffusionPipeline as DP
from PIL import Image,ImagDraw, ImagefFront

def text_to_image(text,diffuser_model):
    #defuser = diffuser.lodad_iffuser(diffuser_model)
    #image_data -= diffuser.genrete(textimg)
    #image = Image.fromarray(image_data)
    #image.show()
    df = DP.from_pretrained("runwayml/stable-diffusion-v1-5")

    
if __name__=="__main__":
    input_text = "Hello,World"
    diffuser_model = "exmple_diffuser_model"
>>>>>>> 5abdf33380d3fe1729fa10362042f8450881f5a6
    text_to_image(input_text,diffuser_model)