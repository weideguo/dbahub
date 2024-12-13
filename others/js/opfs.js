// Origin Private File System
// 只能用与https页面

opfsRoot= await navigator.storage.getDirectory();
// 创建目录
dirHandle = await opfsRoot.getDirectoryHandle('opds_dir_test_20241129', {create: true,});
// 创建文件
fileHandle = await dirHandle.getFileHandle('opds_file_test_20241129.txt', {create: true,});

// 写入文件
const writable = await fileHandle.createWritable();
await writable.write('这是OPFS测试数据');
await writable.close();

// 读取文件
const file = await fileHandle.getFile();
// 获取内容，blob
blob_content = await file.slice(0, file.size);
// blob转成文本
blob_content.text()

// 获取内容，文本格式
str_content = await file.text()


