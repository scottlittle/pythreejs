from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Light_autogen import Light

from ..core.Object3D import Object3D

class DirectionalLight(Light):
    """DirectionalLight
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Lights/DirectionalLight 
    """

    def __init__(self, color="#ffffff", intensity=1, **kwargs):
        kwargs['color'] = color
        kwargs['intensity'] = intensity
        super(Light, self).__init__(**kwargs)

    _view_name = Unicode('DirectionalLightView').tag(sync=True)
    _model_name = Unicode('DirectionalLightModel').tag(sync=True)

    target = Instance(Object3D, allow_none=True).tag(sync=True, **widget_serialization)
    castsShadow = Bool(False).tag(sync=True)

