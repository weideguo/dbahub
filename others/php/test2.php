<?php
/*
require 会生成致命错误（E_COMPILE_ERROR）并停止脚本
include 只生成警告（E_WARNING），并且脚本会继续
*/

require("test.php");
//include("test.php");

f();
?>