import psutil

def check_cpu():
        metric=input("enter the metric: ")
        
        if metric=="cpu":
            cpu_threshold=float(input("Enter the threshold: "))
            current_cpu=psutil.cpu_percent(interval=1)
            if current_cpu > cpu_threshold:
                  print("current cpu %: ", current_cpu )
            else:
                  print("CPU in safe state")

        elif metric=="memory":
            memory_threshold=float(input("Enter the threshold: "))
            memory_usage=psutil.virtual_memory().percent
            if memory_usage > memory_threshold:
                  print("memory usage %: ", memory_usage )
            else:
                  print("memory is ok")

        elif metric=="disk":
            
            disk_threshold=float(input("Enter the threshold: "))
            disk_usage=psutil.disk_usage('/').percent
            if disk_usage > disk_threshold:
                  print("memory usage %: ", disk_usage )
            else:
                  print("memory is ok")
              
              
    
check_cpu()

#metric=input("enter the metric: ")