medida = float(input('uma medida em metros:'))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
print(' {}m equivale a {}mm\n {}cm\n {}dm\n {}km\n {}hm\n {}dam'.format(medida, mm, cm, dm, km, hm, dam))