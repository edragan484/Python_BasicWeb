try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
    