var INSTALLED_NODE_ID = 'my-extension-installed';
var CLIENT_EXIST_ID = 'client-application-installed';
var retry = 0;
var getNode = function (myid) 
{
  return document.getElementById(myid);
};

var insertNode = function (myid) 
{
  	var isInstalledNode = document.createElement('div');
    isInstalledNode.id = myid;
    isInstalledNode.style.visibility = 'hidden';
    document.body.appendChild(isInstalledNode);
};

var deleteNode = function (myid) 
{
  	var isInstalledNode = document.createElement('div');
    isInstalledNode.id = myid;
    isInstalledNode.style.visibility = 'hidden';
    document.body.removeChild(isInstalledNode);
};

function checkClinet()
{

	chrome.runtime.sendMessage({greeting: "hello"}, function(response)
	{
    try{
      if (response.farewell == "1")
      {
          if(!getNode(CLIENT_EXIST_ID))
              insertNode(CLIENT_EXIST_ID);
      }
      else if(response.farewell == "2")
      {
          if(getNode(CLIENT_EXIST_ID))
    					deleteNode(CLIENT_EXIST_ID);
      }
      else
      {
          if(retry < 3)
    			{
      				retry++;
      				setTimeout('checkClinet()',500);
    			}
      }
      
    }
    catch(e)
    {
      alert(e);
    }
  
	});
};

if(!getNode(INSTALLED_NODE_ID))
	insertNode(INSTALLED_NODE_ID);

checkClinet();

/*
document.addEventListener('myCustomEvent', function(evt) {
  chrome.runtime.sendMessage({greeting: "hello"}, function(response)
	{
    try{
      if (response.farewell == "1")
      {
          alert("Success!");
          //if(!getNode(CLIENT_EXIST_ID))
          //    insertNode(CLIENT_EXIST_ID);
              
      }
      else if(response.farewell == "2")
      {
          alert("Please install WebStart!");
          //if(getNode(CLIENT_EXIST_ID))
    			//		deleteNode(CLIENT_EXIST_ID);
      }
      
      else
      {
          if(retry < 3)
    			{
      				retry++;
      				setTimeout('checkClinet()',500);
    			}
      }
      
    }
    catch(e)
    {
      alert(e);
    }
    
	});
}, false);
*/