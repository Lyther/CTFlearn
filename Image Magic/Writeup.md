# Image Magic

Programming Hard Rating: 4.38 / 5

[Link](https://ctflearn.com/challenge/89) address here.

## Description

It looks like someone messed up my picture! Can anyone reorganize the pixels? The python module PIL (Python Imaging Library) might be useful!

https://mega.nz/#!OKxByZyT!vaabCJRG5D9zAUp7drTekcA5pszu67r_TbQMtxEzqGE

Update: I think whoever messed up my image took every column of pixels and put them side by side. Update: I think the width of the image was 304 before they messed with it.

## Solution

1. Check the given picture, find out its a 27968 x 1 pixels picture.

2. Divide the width 304 from 27968, get the height 92.

3. Write the following python program to reformat the picture (Pillow is required).

   ```python
   from PIL import Image
   
   image = Image.open('out copy.jpg')
   output = Image.new('RGB', (304, 92))
   for i in range(304):
       part = image.crop((i * 92, 0, (i + 1) * 92, 1))
       part = part.transpose(Image.ROTATE_270)
       output.paste(part, (i, 0, i + 1, 92))
   output.save('flag.jpg')
   ```

4. Run the python program, reformat the picture to `flag.jpg`, and find out the flag.

