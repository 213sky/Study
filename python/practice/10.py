'''
题目：暂停一秒输出，并格式化当前时间。
'''

import time


#利用localtime() -- convert seconds since Epoch to local time tuple的结构体自己组装
'''
|  Data descriptors defined here:
|  
|  tm_hour
|      hours, range [0, 23]
|  
|  tm_isdst
|      1 if summer time is in effect, 0 if not, and -1 if unknown
|  
|  tm_mday
|      day of month, range [1, 31]
|  
|  tm_min
|      minutes, range [0, 59]
|  
|  tm_mon
|      month of year, range [1, 12]
|  
|  tm_sec
|      seconds, range [0, 61])
|  
|  tm_wday
|      day of week, range [0, 6], Monday is 0
|  
|  tm_yday
|      day of year, range [1, 366]
|  
|  tm_year
|      year, for example, 1993
'''
t = time.localtime()
print("%s-%02d-%s %s:%s:%s" %(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))

#利用自带函数strftime() -- convert time tuple to string according to format specification
'''
strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
'''
print(time.strftime("%Y-%m-%d %H:%M:%S"))
