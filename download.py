import requests
url = '''http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/srtm_'''
for i in range(10, 73):
    if i < 10:
        i = '0' + str(i)
    for j in range(1, 25):
        if j < 10:
            j = '0' + str(j)
        r = requests.get(url + str(i) + '_' + str(j) + '.zip')
        if r.status_code == 200:
            print("Downloading srtm_"  + str(i) + '_' + str(j) + '.zip')
            with open('data/srtm_' + str(i) + '_' + str(j) + '.zip', 'wb') as f:
                f.write(r.content)
        else:
            print('strm_'  + str(i) + '_' + str(j) + '.zip not found')
