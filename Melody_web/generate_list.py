import glob
from Melody_web import athletemodel
from Melody_web import yate

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_stroe(data_files)



print(yate.include_footer({"Home": "/index.html"}))