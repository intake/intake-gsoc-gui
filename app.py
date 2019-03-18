import panel as pn
from bokeh.plotting import figure
pn.extension()


def make_volume():
    """Thie function makes a 3D array of data, a brain scan"""
    from skimage import io
    vol = io.imread(
        "https://s3.amazonaws.com/assets.datacamp.com/blog_assets"
        "/attention-mri.tif")
    return vol


TOOLTIPS = [
    ("x", "$x"),
    ("y", "$y"),
    ("value", "@image"),
]
shape = (157, 189, 68)
volume = make_volume()
inverted = False


def make():
    """Here we make a figure widget with a 2D image and put it in the layout"""
    global inverted
    p1 = figure(width=400, height=400, tools='hover,wheel_zoom',
                tooltips=TOOLTIPS,
                x_range=[0, 157], y_range=[0, 189])
    if inverted:
        p1.image(image=[volume[:, ::-1, 30]], x=[0], y=[0], dw=[157], dh=[189])
    else:
        p1.image(image=[volume[:, :, 30]], x=[0], y=[0], dw=[157], dh=[189])
    widgets[1] = p1
    inverted = not inverted


if __name__ == "__main__":
    button = pn.widgets.Button(name='Invert')
    button.on_click(lambda *_: make())
    widgets = pn.Column(button, button, width=400)
    make()
    widgets.show()
