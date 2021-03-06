[![BuildTest](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/build_test.yml/badge.svg)](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/build_test.yml)
[![CodeQL](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/codeql-analysis.yml)
[![PypiPublish](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/pypi_publish.yml/badge.svg)](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/pypi_publish.yml)
[![TestPypiPublish](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/testpypi_publish.yml/badge.svg)](https://github.com/LAPKT-dev/val-wrapper/actions/workflows/testpypi_publish.yml)

# val-wrapper
A python wrapper over KCL-VAL binaries compiled from [source](https://github.com/KCL-Planning/VAL)

Install
-------

        python3 -m pip install val-wrapper

How does it work?
=================

The entire build and python packaging is handled by cmake. The VAL github source is added as an external project which is compiled on the target system. The python wrapper is a script which calls the Validate executable.

LICENSE
-------
The *wrapper* source code in this repository is released under MIT license. On the other hand, the pypi release, which redistributes the VAL binaries, carries the original [license](https://github.com/KCL-Planning/VAL/blob/3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4/LICENSE) under which VAL source is released.

# BUILD

        cmake -B<build_dir> -S<this repo's root path> -DCMAKE_INSTALL_PREFIX=<installation dir>
        cmake --build <build_dir> --target install

## Build a platform specific wheel
        python3 setup.py bdist_wheel --plat-name=<platform tag>

  - Platform tags are based on the platform on which the binaries were built, for example:
    - `win_amd64`
    - `manylinux1_x86_64`
    - `manylinux_x_y_x86_64`
    - ... many more, lookup the documentation

## PIP install using locally built binaries

        cd <installation dir>/pypi_release
        python3 -m pip install .


# USAGE

- Command line 

    `validate.py` is installed as a python script, a wrapper around `Validate` executable, which can be run from the command line. The pypi script installation directory is generally in system `PATH`, if not, it should be added manually.

        validate.py -h

- From another python module

    You can import `val_main` from `val_wrapper` and use it to run VAL binaries. 
    
    SYNTAX: `val_main("<executable name>", [<arg1>, <arg2>, ...])`

        from val_wrapper import val_main
        val_main("Validate", ["-h"])

- Google colab notebook

        !pip install val-wrapper wurlitzer --upgrade

        from val_wrapper import val_main
        from wurlitzer import sys_pipes

        with sys_pipes():
            val_main("Validate", ["-h"])