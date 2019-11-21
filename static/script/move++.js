function getStyle(obj,name){
    if(obj.currentStyle)
    {
        return obj.cuurentStyle[name];
    }
    else{
        return getComputedStyle(obj,false)[name];
    }
}

function move(obj,json,fnEnd)
{
    clearInterval(obj.timer);
    
    obj.timer=setInterval(function(){
        var check=true;
        
        for(var type in json)
        {
            var cur=0;  //cur 对象当前的属性值
            if(type=='opacity')
            {
                cur=Math.round(parseFloat(getStyle( obj,type))*100);
            }
            else{
                cur=parseInt(getStyle( obj,type));  
            }
    
            var speed=(json[type]-cur)/6;
            speed=speed>0?Math.ceil(speed):Math.floor(speed);
             if(cur!=json[type])
            {
                check=false;}

                if(type=='opacity')
                {
                cur+=speed;
                obj.style.filter='alpha(opacity='+cur+')';
                obj.style.opacity= cur/100;
                }
                else{
                obj.style[type]=cur+speed+'px';  
                }  
        }
        if(check){
                clearInterval(obj.timer);
                
               if(fnEnd)fnEnd();
           }
    },30);
}