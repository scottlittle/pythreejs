from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from ..core.Object3D import Object3D


class Light(Object3D):
    """Light
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Lights/Light 
    """

    def __init__(self, color="#ffffff", intensity=1, **kwargs):
        kwargs['color'] = color
        kwargs['intensity'] = intensity
        super(Object3D, self).__init__(**kwargs)

    _view_name = Unicode('LightView').tag(sync=True)
    _model_name = Unicode('LightModel').tag(sync=True)

    color = Unicode("#ffffff").tag(sync=True)
    intensity = CFloat(1).tag(sync=True)

