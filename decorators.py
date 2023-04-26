from time import time

def delta_time(n):
    def count_elapsed_time(f):
       
        def w(*args, **kwargs):
            # Start counting.
            start_time = time()
            # Take the original function's return value.
            ret = f(*args, **kwargs)
            # Calculate the elapsed time.
            elapsed_time = (time()) - start_time
            print(n+"--> Tardo: %.8f Seconds."% elapsed_time)
            return ret
        
        return w
    return count_elapsed_time