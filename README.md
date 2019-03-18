Preliminary code for GSOC
=========================

Introduction
------------

The issue https://github.com/ESIPFed/gsoc/issues/14 contains a conversation around a possible
project for GSOC 2019, concerning interactive data visualisation in the context of 
[Intake](https://intake.readthedocs.io) and [PyViz](http://pyviz.org/index.html), under
the auspices of ESIP.

This repo contains a small amount of code as a starting point, and addresses only a part of the
concept, but one that students are likely not familiar with.

The Task
--------

To form some familiarity with the tools and GUI interacttivy with python in the browser,
we ask that potential students extend the code in this repo, via github PR. The goal is:

- for the given data volume, to be able to select among the three axes of projection, XY, XZ, YZ
- for each of those axes to be able to select any index of plane to show
- to resize the plot axes to accurately reflect the current selection
- (bonus) to provide a choice of colour-maps to render with (see 
  [plettes](https://bokeh.pydata.org/en/latest/docs/reference/palettes.html))
- (bonus) to rewrite the code using [parameters](https://panel.pyviz.org/user_guide/Param.html)

The Existing Code
-----------------

The file `app.py` contains the reference to be built upon. It sets up an interactive application which
runs in a browser. To run:
```bash
python app.py
```
Dependencies can be installed with the command
```bash
conda install -c conda-forge panel bokeh numpy scikit-image param
```

The layout contains one button, which causes the `make()` function to be run every time, and flips
the image in the x-direction. In this version, the specific slice of the image being shown and the
colour-map are fixed.

The code is not meant to be an example of good design! It is just the simplest interaction that we
could come up with, demonstrating a Panel callback. To see a real example of a GUI being built with
Panel, see [this PR](https://github.com/intake/intake/pull/286).
