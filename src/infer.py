import os
import json
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from tqdm import tqdm
from config import *


# Get Tensor data from images
test_transforms = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])

def load_images(files):
    images = []
    for file in files:
        img = Image.open(os.path.join(IMAGES_DIR, file))
        img = test_transforms(img)
        images.append(img)
    return torch.stack(images)


device = torch.device("cuda:"+DEVICE if torch.cuda.is_available() else "cpu")

# Load the model
model = torch.load(MODEL_PATH, map_location=device)
model.to(device)
model.eval() 


results = {}



files = os.listdir(IMAGES_DIR)
num_batches = int(np.ceil(len(files) / BATCH_SIZE))

for batch_idx in tqdm(range(num_batches)):
    start_idx = batch_idx * BATCH_SIZE
    end_idx = min((batch_idx + 1) * BATCH_SIZE, len(files))
    batch_files = files[start_idx:end_idx]

    # Load images in batch
    batch_images = load_images(batch_files)
    batch_images = batch_images.to(device)

    # Get predictions for batch
    with torch.no_grad():
        output = model(batch_images, None, return_preds=True)

    # Store predictions
    for idx, file in enumerate(batch_files):
        results[file] = output['preds'][idx][0]

    
    
#sort results json numerically by filename
results = {k: v for k, v in sorted(results.items(), key=lambda item: int(item[0].split('.')[0]))}


# Save the results
with open(RESULTS_FILE, 'w') as f:
    json.dump(results, f, indent=4)
    

    
        
