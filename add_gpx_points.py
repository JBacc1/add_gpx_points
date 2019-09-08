# -*- coding: utf-8 -*-

from sys import argv
from sys import exit
import math
import gpxpy
import gpxpy.gpx


def distance_points(p1,p2):
	return math.sqrt((p1.latitude-p2.latitude)**2+(p1.longitude-p2.longitude)**2)
def mid_point(p1,p2,proportion=0.5):
	return gpxpy.gpx.GPXTrackPoint(p1.latitude+(p2.latitude-p1.latitude)*proportion, p1.longitude+(p2.longitude-p1.longitude)*proportion)

try : gpx_name=argv[1]
except:
	print('Usage : python add_gpx_points.py gpx_file.gpx\n OR\n        python add_gpx_points.py gpx_file.gpx distance_between_points_approx_metres')
	exit()
	

gpx_file=open(gpx_name)
gpx=gpxpy.parse(gpx_file)

try : insert_every_m=argv[2]
except: insert_every_m=100

insert_every=float(insert_every_m)*0.000009
dont_insert_if_inferior=0.05 #dont insert point if remains less than 1+#% of distance insert_every

new_gpx=gpxpy.gpx.GPX()

for track in gpx.tracks:
	gpx_track = gpxpy.gpx.GPXTrack()
	new_gpx.tracks.append(gpx_track)
	for segment in track.segments:
		gpx_segment = gpxpy.gpx.GPXTrackSegment()
		gpx_track.segments.append(gpx_segment)
		last_point, new_point=None, None
		for point in segment.points: 
			last_point=new_point
			new_point=point
			while last_point!=None:
				this_interval=distance_points(last_point,new_point)
				if (this_interval)<insert_every/(1-dont_insert_if_inferior):
					last_point=None
				else:
					proportion=insert_every/this_interval
					insert_point=mid_point(last_point,new_point,proportion)
					gpx_segment.points.append(insert_point)
					last_point=insert_point
			gpx_segment.points.append(point)

with open(gpx_name.replace(".gpx","_inserted.gpx"),"w") as new:
	new.write(new_gpx.to_xml())

gpx_file.close()
