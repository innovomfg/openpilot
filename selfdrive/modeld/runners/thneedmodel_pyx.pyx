# distutils: language = c++
<<<<<<< HEAD
# cython: c_string_encoding=ascii, language_level=3
=======
# cython: c_string_encoding=ascii
>>>>>>> 8b9791041 (sunnypilot v2024.06.11-2039)

from libcpp cimport bool
from libcpp.string cimport string

from .thneedmodel cimport ThneedModel as cppThneedModel
from selfdrive.modeld.models.commonmodel_pyx cimport CLContext
from selfdrive.modeld.runners.runmodel_pyx cimport RunModel
from selfdrive.modeld.runners.runmodel cimport RunModel as cppRunModel

cdef class ThneedModel(RunModel):
  def __cinit__(self, string path, float[:] output, int runtime, bool use_tf8, CLContext context):
    self.model = <cppRunModel *> new cppThneedModel(path, &output[0], len(output), runtime, use_tf8, context.context)
