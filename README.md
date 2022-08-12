# PSLG file generator from image

Script in python to generate a Planar straight-line graph as a Poly file from a image.

![Poly example](https://github.com/ssalinasfe/PSLG-file-generator-from-image/blob/main/polyexample.png?raw=true)

## Image preparation

The scripts reads points in counterclock wise from svg files, those files can be generate using path tool from gimp.

![image preparation](https://raw.githubusercontent.com/ssalinasfe/PSLG-file-generator-from-image/main/Screenshot%20from%202022-08-12%2015-13-59.png)

## Poly file generation

You should use the function get_points_from_file to add each svg, this will read the points of the svg and generate a list with those points.

To add holes, select one point inside the hole to add and add it to the hole list. The y-coordinate of the hole must be negative. You can check the coordinate of each pixel of an image in left corner of gimp.

## Triangle

After generate the poly file, you can generate a triangulation using the the software [Triangle](https://www.cs.cmu.edu/~quake/triangle.html) 

The file example was generate using the command

```
triangle -a2000n bullita.poly && showme bullita.poly
```

To visualize the triangulation you can use the program showme include in triangle.

```
showme bullita.poly
```

![Poly example](https://github.com/ssalinasfe/PSLG-file-generator-from-image/blob/main/triangulationexample.png?raw=true)



