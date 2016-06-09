#!/bin/sh
latitude=$(gdalinfo IMG_20160602_150913.jpg  | grep "GPSLatitude=" | awk -F'[=(&)]' '{print $3}')
longitude=$(gdalinfo IMG_20160602_150913.jpg  | grep "GPSLongitude=" | awk -F'[=(&)]' '{print $3}')
echo $latitude
echo $longitude

for filename in /home/bharat/GeoImaging/*.jpg
do
  photo=${filename##*/}
  latitude=$(gdalinfo $photo  | grep "GPSLatitude=" | awk -F'[=(&)]' '{print $3}')
  longitude=$(gdalinfo $photo  | grep "GPSLongitude=" | awk -F'[=(&)]' '{print $3}')
  echo $photo
  echo "latitude="$latitude
  echo "longitude="$longitude
done;
lati="latitude"
longi="longitude"
latitude=$latitude
longitude=$longitude
sed -i "s/${lati}/${latitude}/g" test.html
sed -i "s/${longi}/${longitude}/g" test.html
