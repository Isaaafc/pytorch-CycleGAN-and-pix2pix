import os
import argparse
import shutil
import random
import subprocess

dataroot = os.path.join('./datasets/faces2animes/')

cmd = 'python test.py --dataroot {} --name faces2animes --model cycle_gan --gpu_ids -1'.format(dataroot)

parser = argparse.ArgumentParser()
parser.add_argument('infile', help='image of a cropped face')
parser.add_argument('--outfile', help='output file name')
args = parser.parse_args()

testA = os.path.join(dataroot, 'testA')
testB = os.path.join(dataroot, 'testB')

if os.path.exists(testA):
    shutil.rmtree(testA)

if os.path.exists(testB):
    shutil.rmtree(testB)

os.mkdir(testA)
os.mkdir(testB)

shutil.copy2(args.infile, os.path.join(testA, os.path.basename(args.infile)))

# Use a random default stlye
def_styles = os.listdir(os.path.join(dataroot, 'default'))
rand_style = def_styles[random.randrange(0, len(def_styles))]
shutil.copy2(os.path.join(dataroot, 'default', rand_style), os.path.join(testB, rand_style))

process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
out, err = process.communicate()

if err is not None:
    print(err)
else:   
    in_split = os.path.splitext(os.path.basename(args.infile))
    outfile = args.outfile if args.outfile is not None else '{}_out.png'.format(in_split[0])

    shutil.move(os.path.join('results/faces2animes/test_latest/images', '{}_fake_B.png'.format(in_split[0])), outfile)
    shutil.rmtree('results/faces2animes/test_latest')