import torch
import math

class OrientationMate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "New Longest Edge": (
                    "INT", 
                    {
                        "default": 512, 
                        "min": 16, 
                        "max": 8192, 
                        "step": 16, 
                        "display": "number"
                    }
                ),
            },
        }

    # These are the labels seen on the node pins
    RETURN_TYPES = ("INT", "INT", "FLOAT", "FLOAT", "INT", "INT")
    RETURN_NAMES = (
        "Original Width", 
        "Original Height", 
        "Aspect Ratio", 
        "Resized Scale", 
        "Resized Width", 
        "Resized Height"
    )
    
    FUNCTION = "compute"
    CATEGORY = "image/transform"

    def compute(self, image: torch.Tensor, **kwargs):
        # Safely extract our user input using the exact string match
        new_longest_edge = kwargs.get("New Longest Edge", 512)        
        
        # Extract dimensions from tensor [Batch, Height, Width, Channels]
        _, orig_height, orig_width, _ = image.shape
        
        aspect_ratio = float(orig_width) / float(orig_height)
        
        # Ensure the target edge is a multiple of 16 (Ceiling)
        target_edge = int(math.ceil(new_longest_edge / 16.0) * 16)
        
        if orig_width >= orig_height:
            resized_width = target_edge
            scale = float(resized_width) / float(orig_width)
            # Calculate height and snap to upper multiple of 16
            resized_height = int(math.ceil((orig_height * scale) / 16.0) * 16)
        else:
            resized_height = target_edge
            scale = float(resized_height) / float(orig_height)
            # Calculate width and snap to upper multiple of 16
            resized_width = int(math.ceil((orig_width * scale) / 16.0) * 16)

        return (orig_width, orig_height, aspect_ratio, scale, resized_width, resized_height)

NODE_CLASS_MAPPINGS = {"OrientationMate": OrientationMate}
NODE_DISPLAY_NAME_MAPPINGS = {"OrientationMate": "Orientation Mate 📐"}
