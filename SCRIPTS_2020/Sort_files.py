import os
copy_csv_to = str("/run/user/1001/gvfs/smb-share:server=r-zfssvr01,share=grplucy/Videos_GRETI/")
pp = os.walk(copy_csv_to)
print(pp)

import os
for root, dirs, files in os.walk(copy_csv_to, topdown=False):
   for name in files:
      print(os.path.join(name))
      





