# start 
chrome扩展程序至少存在清单文件 manifest.json 
浏览器开发者模式加载扩展程序，即为加载清单文件所在的目录：
chrome://extensions/  --> 开发者模式 --> 加载已解压的扩展程序

 

# demo  
manifest.json 
```json
{
  "manifest_version": 2,  
  "name": "MyApp",
  "version": "0.7",
  "author": "wdg",
  "description": "this is MyApp description",
  "permissions": [                                   // 权限
    "clipboardWrite",                                //
    "contextMenus",                                  //
    "activeTab"                                      //
  ],                                                 //
  "icons": {                                         // 图标
    "16": "images/MyApp16.png",                      //
    "32": "images/MyApp32.png",                      //
    "48": "images/MyApp48.png",                      //
    "128": "images/MyApp128.png"                     //
  },                                                 //
  "minimum_chrome_version": "80",                    // 
                                                     // 以下块并不全部都需要
  "background": {                                    // 后台运行 浏览器运行期始终运行
    "persistent": false,                             //
    "scripts": ["background.js"]                     // 入口脚本需要调用执行chrome的api
  },                                                 //
  "browser_action": {                                // 地址栏右侧图标弹出页面
    "default_icon": "image/MyApp16.png",             //
    "default_title": "My Test",                      //
    "default_popup": "html/browser.html"             //
  },                                                 //
  "content_scripts": [{                              // 指定要向Web页面内注入的脚本，对web页面进行修改
    "matches": ["https://*","http://*"],             // 
    "css": ["css/mystyles.css"],                     // 
    "js": ["lib/jquery-3.3.1.min.js",                // 
           "js/content.js"]                          // 
  }]
}
```


# chrome api demo
```js
function quoteOnClick(info) {
console.log(info.pageUrl);          // 当前url
console.log(info.selectionText);    // 长按鼠标左键选择的文字
console.log(info.menuItemId);       // 点击动作的id
}

// 单击菜单栏的动作
chrome.contextMenus.onClicked.addListener(quoteOnClick);

// 长按鼠标左键选择的文字后右击的菜单栏
chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create({
    title: 'MyApp Action',
    id: 'my_parent',
    contexts: ['selection']
  });
  chrome.contextMenus.create({
    title: 'Copy',
    id: 'my_copy',
    parentId: 'my_parent',
    contexts: ['selection']
  });
  chrome.contextMenus.create({
    title: 'Open',
    id: 'my_open',
    parentId: 'my_parent',
    contexts: ['selection']
  });
});
```




 

