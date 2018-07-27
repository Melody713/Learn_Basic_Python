import glob
import athletemodel
import yate

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_stroe(data_files)

print(yate.start_response())
#连接类型
print(yate.include_header("Coach Kelly's List of Athletes"))
#生成网页tittle
print(yate.start_form("generate_timing_data.py"))
#开始生成表单
print(yate.para("Select an athlete from the list to work with :"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))

print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))