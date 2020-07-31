
//控制台中引入脚本
var script = document.createElement('script');
script.src = "http://html2canvas.hertzen.com/dist/html2canvas.min.js";
document.getElementsByTagName('head')[0].appendChild(script)



var ele = document.getElementsByClassName("screenshotable")[0]

html2canvas(ele, {
  onrendered: function(canvas) {
    var url = canvas.toDataURL();
    //canvas.toDataURL("png")
    document.body.appendChild(canvas);
    console.log(url)
  }
});


html2canvas(document.body).then(canvas => {
    var imgData = canvas.toDataURL();
    document.body.appendChild(canvas)
    console.log(imgData)
    
});



////////////////////////////////////////////////////
/*

url="data:image/png;base64,iVBOR...="

*/

var saveFile = function(data, filename){
    //var save_link = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
    var save_link = document.createElement('a');
    save_link.href = data;
    save_link.download = filename;
   
    var event = document.createEvent('MouseEvents');
    event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    save_link.dispatchEvent(event);
    
};
   
   
   
var filename = (new Date()).getTime() + '.png' ;

imgData =url
imgData = imgData.replace('image/png','image/octet-stream');

// download
saveFile(imgData,filename);




