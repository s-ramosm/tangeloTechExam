import datetime


class metricsGenerator():
    
    def __init__(self) -> None:
        pass

    def get_process_time(self,function,*args,**kwargs):

        start_time = datetime.datetime.now()

        function(*args,**kwargs)

        end_time = datetime.datetime.now()

        return start_time-end_time ,

mc = metricsGenerator()

@mc.get_process_time
def _function():
    for item in range(10000):
        print (item)



print (_function())