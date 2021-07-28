var port = null;
var result =  "0";
function onNativeMessage(message) 
{
    if (JSON.stringify(message)  == '{"text":"application/x-gamania.beanfun.webstart.mozilla.1.0.0.2"}' )
    {
        result = "1";
    }
    
}

function onDisconnected() {
    if (chrome.runtime.lastError.message == "Specified native messaging host not found.")
    { 
        result = "2" ;
    }
    port = null;

}



chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) 
    {  
        port = chrome.runtime.connectNative("beanfun");
        if (port != null)
        {
          	port.onMessage.addListener(onNativeMessage);
          	port.onDisconnect.addListener(onDisconnected);
            setTimeout(function(){},500);
          	sendResponse({farewell: result});
        }
        else
        {
          alert('port is null');
        }

    });

// Check whether new version is installed
chrome.runtime.onInstalled.addListener(function(details){
    if(details.reason == "install"){
        console.log("This is a first install!");
        //alert('This is a first install!');
        chrome.tabs.getSelected(null, function(tab) {
            var code = 'window.location.reload();';
            chrome.tabs.executeScript(tab.id, {code: code});
            console.log("window.location.reload();" + tab.id);
        });
    }else if(details.reason == "update"){
        var thisVersion = chrome.runtime.getManifest().version;
        console.log("Updated from " + details.previousVersion + " to " + thisVersion + "!");
    }
});