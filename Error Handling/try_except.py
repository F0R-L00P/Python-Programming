# check for errors using try-except
# search for the most speciffic errors and move to ore general errors
# Never use silent block, using pass statement as the error will be skipped
# this can cuase further issues down the line when running longer code

try:
    method1()
    method2()
    method3()
except ConnectionError as ce:
    # handel network error
except ValueError:
    # handel incorrect values
except Exception as ex:
    # handel general error