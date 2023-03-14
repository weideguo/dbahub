#include <Python.h>

// 原始的cpp函数
double plus(double x, double y)
{
    return x + y;   
}

////////////////////////////////////////////////////////////////////////////////////////////
// 以下是封装以供python调用
// 把原始的函数封装Python函数，函数名并不需要固定格式，跟methods匹配即可
static PyObject *py_plus(PyObject *self, PyObject *args) 
{
    double x = 0;
    double y = 0;
    double result = 0;
    // 参数解析
    // 第二个参数为字符串，指定解析的格式
    PyArg_ParseTuple(args, "dd", &x, &y);
    // PyArg_ParseTuple(args, "d", &x);     // 只解析一个参数
    result = plus(x,y);
    // Py_BuildValue("dd", result, 4);      // python调用函数时有两个返回值的情况
    return Py_BuildValue("d", result);
    
}
// 参数类型参考
// https://docs.python.org/3/c-api/arg.html


// 模块函数列表

// 函数名 
// cpp函数的封装函数 
// METH_VARARGS告诉Python此函数一个典型的PyCFunction 
// 函数的说明 help(函数名) 看到
static PyMethodDef methods[] = {
{"plus", py_plus, METH_VARARGS, "arg1: int\narg2: int"},     
//{0,0,0,0},
};

// 定义模块
static struct PyModuleDef module = {
PyModuleDef_HEAD_INIT, //
"extenddemo",          // 模块名
"extend demo",         // 模块描述
-1,                    // size of per-interpreter state of the module, or -1 if the module keeps state in global variables. 
methods              
};

// 定义模块的初始化方法
PyMODINIT_FUNC PyInit_maths(void)
{
    return PyModule_Create(&module);
}