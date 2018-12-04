# conan-muparser

![conan-muparser image](/images/conan-muparser.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/muparser%3Aconan/images/download.svg?version=2.2.6%3Astable)](https://bintray.com/conan-community/conan/muparser%3Aconan/2.2.6%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-muparser.svg?branch=stable%2F2.2.6)](https://travis-ci.org/conan-community/conan-muparser)
[![Build status](https://ci.appveyor.com/api/projects/status/jyeh443gn0l0f3bi/branch/stable/2.2.6?svg=true)](https://ci.appveyor.com/project/<appveyor_user>/conan-muparser/branch/stable/2.2.6)

[Conan.io](https://conan.io) package for [muparser](http://beltoforion.de/article.php?a=muparser) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/muparser%3Aconan).

## Basic setup

    $ conan install muparser/2.2.6@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    muparser/2.2.6@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)