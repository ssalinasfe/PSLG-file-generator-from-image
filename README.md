# PSLG file generator from image

Script to generate a Planar straight-line graph as a Poly file from a image.

## Image preparation

The scripts reads points in counterclock wise from svg files, those files can be generate using path tool from gimp.

[[Example-image]]

## Poly file generation

You should use the function get_points_from_file to add each svg, this will read the points of the svg and generate a list with those points.

To add holes, select one point inside the hole to add and add it to the hole list. The y-coordinate of the hole must be negative. You can check the coordinate of each pixel of an image in left corner of gimp.

## Triangle

After generate the poly file, you can generate a triangulation using the the software [Triangle](https://www.cs.cmu.edu/~quake/triangle.html) 

The file example was generate using the command

```
triangle -a2000n bullita.poly && showme bullita.poly
```


