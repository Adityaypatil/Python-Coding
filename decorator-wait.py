import  time
def retry_on_error(max_retries):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for attempt in range(1,max_retries+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed with error: {e}")
                    if attempt < max_retries:
                        delay = attempt  # 1s, 2s, 3s
                        print(f"Retrying in {delay} second(s)...")
                        time.sleep(delay)
                    else:
                        print("All retries failed.")
                        return None  # or re-raise or custom value
        return wrapper
    return decorator

@retry_on_error(max_retries=3)
def divide(a, b):
    print(f"Dividing {a} by {b}")
    return a / b


result = divide(10,0)
