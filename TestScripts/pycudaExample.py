#!/home/moita/anaconda3/bin/python3

import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

import numpy

a = numpy.random.randn(20,20)

a = a.astype(numpy.float32)

a_gpu = cuda.mem_alloc(a.nbytes)

cuda.memcpy_htod(a_gpu, a)

mod = SourceModule("""
	__global__ void doublify(float *a)
	{
		int idx = threadIdx.x + threadIdx.y*4;
		a[idx] *= 2;
	}
	""")

func = mod.get_function("doublify")
func(a_gpu, block=(20,20,1))

a_doubled = numpy.empty_like(a)
cuda.memcpy_dtoh(a_doubled, a_gpu)

print (a_doubled[:5])
print (a[:5])