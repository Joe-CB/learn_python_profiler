Cite: https://stackify.com/top-5-python-memory-profilers/
https://pypi.org/project/memory-profiler/


memory profile的方法：
1. pympler
    监控object或type的大小。
2. guppy3
    监控堆上的数据
3. memory_profile
    

python3 -m pip install pympler
python3 -m pip install guppy3
python3 -m pip install -U memory_profiler


## pympler

1. The asizeof module provides basic size information for one or several Python objects
2. The muppy is used for on-line monitoring of a Python application
3. Module Class Tracker provides off-line analysis of the lifetime of selected Python objects.


### `asizeof`
下载

### `muppy`
实时监控

### `tracker`

tracker 可以被用来离线监控object和Class


## guppy3
监视Heap上的大小
> Partition of a set of 38113 objects. Total size = 4443553 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10927  29   970456  22    970456  22 str
     1   9483  25   767104  17   1737560  39 tuple
     2   2478   7   358376   8   2095936  47 types.CodeType
     3   4940  13   344949   8   2440885  55 bytes
     4    444   1   338488   8   2779373  63 type
     5   2286   6   329184   7   3108557  70 function
     6    444   1   248360   6   3356917  76 dict of type
     7    100   0   175088   4   3532005  79 dict of module
     8    253   1   119608   3   3651613  82 dict (no owner)
     9   1090   3    95920   2   3747533  84 types.WrapperDescriptorType
<116 more rows. Type e.g. '_.more' to view.>

## memory_profile

```shell
mprof run <script>
mprof plot

```

### Decorator
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3  40.7734 MiB  40.7734 MiB           1   @profile(precision=4)
     4                                         def my_func():
     5  48.4609 MiB   7.6875 MiB           1       a = [1] * (10 ** 6)
     6 201.0859 MiB 152.6250 MiB           1       b = [2] * (2 * 10 ** 7)
     7  48.5273 MiB -152.5586 MiB           1       del b
     8  48.5273 MiB   0.0000 MiB           1       return a
