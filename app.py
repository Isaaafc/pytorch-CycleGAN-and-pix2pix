import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model

def convert(model, img, save_path):
    pass

if __name__ == '__main__':
    # Set up options
    opt = TestOptions().parse()
    opt.num_threads = 0
    opt.batch_size = 1
    opt.serial_batches = True
    opt.no_flip = True
    opt.display_id = -1

    dataset = create_dataset(opt)
    
    model = create_model(opt)
    model.setup(opt)

    convert(model, img, save_path)
