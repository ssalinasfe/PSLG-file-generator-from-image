#To execute you need install docker: https://github.com/PyMesh/PyMesh
#docker run -it --rm -v `pwd`:/root pymesh/pymesh bash 
#python3 drawpikachu.py

from webbrowser import get
from xml.dom import minidom
import itertools
import numpy as np

def write_poly(points, segments, holes, name):
    n_points =len(points)
    n_segments = len(segments)
    f = open(name + '.poly', 'w')
    f.write("{} 2 0 0\n".format(n_points))
    for i in range(0, n_points):
        f.write('{0} {1} {2}\n'.format(i, points[i][0], points[i][1]))
    f.write("{} 0\n".format(n_segments))
    for i in range(0, n_segments):
        f.write( '{0} {1} {2}\n'.format(i, segments[i][0], segments[i][1]))
    f.write("{} 0\n".format(len(holes)))
    if(len(holes) > 0):
        for i in range(0, len(holes)):
            f.write( '{0} {1} {2}\n'.format(i, holes[i][0], holes[i][1] ))
    else:
        f.write( '0\n')
    f.write('\n')
    f.close()


def write_node(vertices, filename):
    largo =len(vertices)
    f = open(filename, 'w')
    f.write("{} 2 0 0\n".format(largo))
    for i in range(0, len(vertices)):
        #print(i +1, vertices[i][0], vertices[i][1])
        f.write('{0} {1} {2}\n'.format(i, vertices[i][0],vertices[i][1]))
    f.write('\n')
    f.close()
    print("File store as ", filename)

def get_points_from_file(filename):
    #Detecta donde esta el path en el svg
    doc = minidom.parse(filename)  # parseString also exists
    path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
    doc.unlink()

    #Elimina las operaciones M C y Z del inicio y final del svg
    points_string = path_strings[0][path_strings[0].find('C') + 1: path_strings[0].find('Z') - 1]
    remove_duplicates_spaces = ' '.join(points_string.split())
    l = remove_duplicates_spaces.split(' ')
    points = []
    for i in range(len(l)):
        pair = l[i].split(',')
        pair[0] = int(float(pair[0]))
        pair[1] = -1*int(float(pair[1])) #Invierte el eje y
        points.append([pair[0], pair[1]])

    #Elimina puntos repetidos continuous, el ultimo y el primer punto esta repetido
    points = [g for g, _ in itertools.groupby(points)][:-1]

    return points


#Read square
#square = get_points_from_file('square.svg')

print("Reading files")

ext_contour = get_points_from_file('ext_contour.svg')
inter_contour = get_points_from_file('inter_contour.svg')
forehead = get_points_from_file('forehead.svg')
face = get_points_from_file('face.svg')
left_eye = get_points_from_file('left_eye.svg')
right_eye = get_points_from_file('right_eye.svg')
neck = get_points_from_file('neck.svg')
body = get_points_from_file('body.svg')
letter_U = get_points_from_file('letter_U.svg')


print("Generating points for poly file")
letters = [ext_contour, inter_contour, forehead, face, left_eye, right_eye, neck, body, letter_U]
points = ext_contour + inter_contour + forehead + face + left_eye + right_eye + neck + body + letter_U

hole_white = (760, -732)
hole_left_eye = (768, -472)
hole_right_eye = (1207, -490)
hole_letter_U = (789, -1380)

holes = [hole_white, hole_left_eye , hole_right_eye, hole_letter_U]

print("Converting coordinates to indices")
mesh = []
for letter in letters:
    polygon = []
    for coord in letter:
        polygon.append(points.index(coord))
    mesh.append(polygon)

print("Adding constrains")
constrains = []
for poly in mesh:
    for i in range(0, len(poly)):
        constrains.append([poly[i], poly[(i+1)%len(poly)]])

print("Writing poly file")
write_poly(points, constrains, holes, "bullita")