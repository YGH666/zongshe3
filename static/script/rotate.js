var radius = 150;
var dtr = Math.PI/180;
var d=300;

var mcList = [];
var active = false;
var lasta = 1;
var lastb = 1;
var distr = true;
var tspeed=2;
var size=250;

var mouseX=0;
var mouseY=0;

var howElliptical=1;

var aA=null;
var oDiv=null;

window.onload=function ()
{
	///////////////////////////////////////////////
	document.getElementById('showSignin2').onclick = document.getElementById('btn_showlogin').onclick =document.getElementById('showSignin1').onclick = showLogin;
      document.getElementById('close_minilogin').onclick = closeLogin;
      document.getElementById('showSignup').onclick = showSignup;
      document.getElementById('close_minisignup').onclick = closeSignup;
      document.getElementById('showFindpass').onclick = showFindpass;
      document.getElementById('close_findpass').onclick = closeFindpass;


      var mini_login = document.getElementsByClassName('mini_login')[0];
      var cover = document.getElementsByClassName('cover')[0];
      var mini_signup = document.getElementsByClassName('mini_signup')[0];
      var mini_findpass = document.getElementsByClassName('mini_findpass')[0];

      function showLogin() {
        mini_signup.style.display = 'none';
        mini_login.style.display = 'block';
        mini_findpass.style.display = 'none'
        cover.style.display = 'block';

        mini_login.style.left = (document.body.clientWidth - mini_login.clientWidth) / 2 + "px";
        mini_login.style.top = (document.body.clientHeight - mini_login.clientHeight) / 3 + "px";
      }

      function closeLogin() {
        mini_login.style.display = 'none';
        cover.style.display = 'none';
      }

      function showSignup() {
        mini_login.style.display = 'none';
        mini_signup.style.display = 'block';
        mini_findpass.style.display = 'none'
        cover.style.display = 'block';

        mini_signup.style.left = (document.body.clientWidth - mini_signup.clientWidth) / 2 + "px";
        mini_signup.style.top = (document.body.clientHeight - mini_signup.clientHeight) / 4 + "px";
      }


      function closeSignup() {
        mini_signup.style.display = 'none';
        cover.style.display = 'none';
      }

      function showFindpass() {
        mini_findpass.style.display = 'block'
        mini_login.style.display = 'none';
        mini_signup.style.display = 'none';
        cover.style.display = 'block';

        mini_findpass.style.left = (document.body.clientWidth - mini_findpass.clientWidth) / 2 + "px";
        mini_findpass.style.top = (document.body.clientHeight - mini_findpass.clientHeight) / 3 + "px";
      }

      function closeFindpass() {
        mini_findpass.style.display = 'none';
        cover.style.display = 'none';
      }

      function isEmail(str) {
        var myReg = /^[-_A-Za-z0-9]+@([_A-Za-z0-9]+\.)+[A-Za-z0-9]{2,3}$/;
        if (myReg.test(str)) {
          return true;
        } else {
          return false;
        }

      }

      signin = function () {
        var right = true;
        document.getElementsByClassName('usrerrempty')[0].style.visibility = 'hidden';
        document.getElementsByClassName('usrerrformat')[0].style.visibility = 'hidden';
        document.getElementsByClassName('paserr')[0].style.visibility = 'hidden';
        var username = document.getElementById('username').value;
        var pass = document.getElementById('password');
        if (username == '') {
          document.getElementsByClassName('usrerrempty')[0].style.visibility = 'visible';
          right = false;
        } else if (isEmail(username) == false) {
          document.getElementsByClassName('usrerrformat')[0].style.visibility = 'visible';
          right = false;
        }

        if (pass.value == '') {
          document.getElementsByClassName('paserr')[0].style.visibility = 'visible';
          right = false;
        }

        if (right) {
          var fields = $('#login_form').serializeArray();
          var obj = {}; //声明一个对象
          $.each(fields, function (index, field) {
            obj[field.name] = field.value; //通过变量，将属性值，属性一起放到对象中
          })
          console.log(obj);

          $.ajax({
            type: "post",
            url: "http://148.70.200.102:11250/user/login",
            async: true,
            contentType: 'application/json',
            dataType: 'JSON',
            xhrFields: {
              withCredentials: false
            },
            crossDomain: true,
            data: JSON.stringify(obj), //将对象转为json字符串
            success: function (data) {
              console.log(data);
              if (data.tag == 'success') {
                alert('登陆成功')
                closeLogin()
              } else if (data.tag == "account doesn't exist") {
                alert('账户不存在!')
              } else if (data.tag == 'password error') {
                alert('密码错误!')
              }
              // window.location.href="localhost"
            }
          });

        }
      }

      var checkcode = '00000';
      var findpasscode = '00000';
      var clock = '';
      var nums = 10;
      var clock1 = '';
      var nums1 = 10;
      var btn = document.getElementsByClassName('orange')[0];
      var btn1 = document.getElementsByClassName('orange')[1];
      sendCode = function () {
        var user = document.getElementById('username_signup').value;
        var data = {
          data: JSON.stringify({
            "value": user
          })
        }

        $.ajax({
          type: 'POST',
          url: "/sendemailcode",
          data: data,
          success: function (ans) {
            console.log(ans)
            checkcode = ans;
          }
        });


        btn.disabled = true;
        btn.value = nums + 's to wait';
        clock = setInterval(doLoop, 1000);
      }

      sendCode1 = function () {
        var user = document.getElementById('username_findpass').value;
        var data = {
          data: JSON.stringify({
            "value": user
          })
        }

        $.ajax({
          type: 'POST',
          url: "/sendemailcode",
          data: data,
          success: function (ans) {
            console.log(ans)
            findpasscode = ans;
          }
        });


        btn1.disabled = true;
        btn1.value = nums + 's to wait';
        clock1 = setInterval(doLoop1, 1000);
      }


      function doLoop() {
        nums--;
        if (nums > 0) {
          btn.value = nums + 's to wait';
        } else {
          clearInterval(clock);
          btn.disabled = false;
          btn.value = '点击发送验证码';
          nums = 10;
        }
      }

      function doLoop1() {
        nums1--;
        if (nums1 > 0) {
          btn1.value = nums1 + 's to wait';
        } else {
          clearInterval(clock1);
          btn1.disabled = false;
          btn1.value = '点击发送验证码';
          nums1 = 10;
        }
      }


      signup = function () {
        var correct = true;
        document.getElementsByClassName('usrerrempty')[1].style.visibility = 'hidden';
        document.getElementsByClassName('usrerrformat')[1].style.visibility = 'hidden';
        document.getElementsByClassName('paserr')[1].style.visibility = 'hidden';
        document.getElementsByClassName('paserr')[2].style.visibility = 'hidden';
        document.getElementsByClassName('repaserr')[0].style.visibility = 'hidden';
        document.getElementsByClassName('ecode')[0].style.visibility = 'hidden';


        var username_signup = document.getElementById('username_signup').value;
        var papassword_signup = document.getElementById('password_signup');
        var repass = document.getElementById('repassword_signup');
        var vccode = document.getElementById('VerificationCode');
        if (username_signup == '') {
          document.getElementsByClassName('usrerrempty')[1].style.visibility = 'visible';
          correct = false;
        } else if (isEmail(username_signup) == false) {
          document.getElementsByClassName('usrerrformat')[1].style.visibility = 'visible';
          correct = false;
        }

        if (papassword_signup.value == '') {
          document.getElementsByClassName('paserr')[1].style.visibility = 'visible';
          correct = false;
        } else if (papassword_signup.value.length < 6 || papassword_signup.value.length > 12) {
          document.getElementsByClassName('paserr')[2].style.visibility = 'visible';
          correct = false;
        }

        if (repass.value != papassword_signup.value) {
          document.getElementsByClassName('repaserr')[0].style.visibility = 'visible';
          correct = false;
        }

        if (vccode.value == '') {
          document.getElementsByClassName('ecode')[0].style.visibility = 'visible';
          correct = false;
        } else if (vccode.value != checkcode) {
          alert('验证码不对！')
          correct = false;
        }

        if (correct) {
          var fields = $('#signup_form').serializeArray();
          var obj = {}; //声明一个对象
          $.each(fields, function (index, field) {
              // if (field.name!='')
            obj[field.name] = field.value; //通过变量，将属性值，属性一起放到对象中
          })

          console.log(obj);

          $.ajax({
            type: "post",
            url: "http://148.70.200.102:11250/user/register",
            async: true,
            contentType: 'application/json',
            dataType: 'JSON',
            xhrFields: {
              withCredentials: false
            },
            crossDomain: true,
            data: JSON.stringify(obj), //将对象转为json字符串
            success: function (data) {
              console.log(data);
              if (data.tag == 'success') {
                alert('注册成功！')
                showLogin();
              } else if (data.tag == 'repeat')
                alert('邮箱已被注册!')
              document.getElementById('signup_form').reset()
              // window.location.href="localhost"
            }
          });


        }
      }

      findbackpass = function () {
        var correct = true;
        document.getElementsByClassName('usrerrempty')[2].style.visibility = 'hidden';
        document.getElementsByClassName('usrerrformat')[2].style.visibility = 'hidden';
        document.getElementsByClassName('paserr')[3].style.visibility = 'hidden';
        document.getElementsByClassName('paserr')[4].style.visibility = 'hidden';
        document.getElementsByClassName('repaserr')[1].style.visibility = 'hidden';
        document.getElementsByClassName('ecode')[1].style.visibility = 'hidden';


        var username_signup = document.getElementById('username_findpass').value;
        var papassword_signup = document.getElementById('password_findback');
        var repass = document.getElementById('repassword_findback');
        var vccode = document.getElementById('VerificationCode1');

        if (username_signup == '') {
          document.getElementsByClassName('usrerrempty')[2].style.visibility = 'visible';
          correct = false;
        } else if (isEmail(username_signup) == false) {
          document.getElementsByClassName('usrerrformat')[2].style.visibility = 'visible';
          correct = false;
        }

        if (papassword_signup.value == '') {
          document.getElementsByClassName('paserr')[3].style.visibility = 'visible';
          correct = false;
        } else if (papassword_signup.value.length < 6 || papassword_signup.value.length > 12) {
          document.getElementsByClassName('paserr')[4].style.visibility = 'visible';
          correct = false;
        }

        if (repass.value != papassword_signup.value) {
          document.getElementsByClassName('repaserr')[1].style.visibility = 'visible';
          correct = false;
        }

        if (vccode.value == '') {
          document.getElementsByClassName('ecode')[1].style.visibility = 'visible';
          correct = false;
        } else if (vccode.value != findpasscode) {
          alert('验证码不对！')
          correct = false;
        }

        if (correct) {
          var fields = $('#findpass_form').serializeArray();
          var obj = {}; //声明一个对象
          $.each(fields, function (index, field) {
            obj[field.name] = field.value; //通过变量，将属性值，属性一起放到对象中
          })

          console.log(obj);
          $.ajax({
            type: "post",
            url: "http://148.70.200.102:11250/user/exchangepasswd",
            async: true,
            contentType: 'application/json',
            dataType: 'JSON',
            xhrFields: {
              withCredentials: false
            },
            crossDomain: true,
            data: JSON.stringify(obj), //将对象转为json字符串
            success: function (data) {
              console.log(data);
              if (data.tag == "account doesn't exist") {
                alert('该邮箱未被注册！')
                document.getElementById('findpass_form').reset()
              } else if (data.tag == 'success') {
                alert('重置密码成功!')
                showLogin()
              }



            }
          });

        }
      }
	///////////////////////////////////////////////////////
	var i=0;
	var oTag=null;

	oDiv=document.getElementById('rotate');
	
	aA=oDiv.getElementsByTagName('a');
	
	for(i=0;i<aA.length;i++)
	{
		oTag={};
		
		oTag.offsetWidth=aA[i].offsetWidth;
		oTag.offsetHeight=aA[i].offsetHeight;
		
		mcList.push(oTag);
	}
	
	sineCosine( 0,0,0 );
	
	positionAll();
	
	oDiv.onmouseover=function ()
	{
		active=true;
	};
	
	oDiv.onmouseout=function ()
	{
		active=false;
	};
	
	oDiv.onmousemove=function (ev)
	{
		var oEvent=window.event || ev;
		
		mouseX=oEvent.clientX-(oDiv.offsetLeft+oDiv.offsetWidth/2);
		mouseY=oEvent.clientY-(oDiv.offsetTop+oDiv.offsetHeight/2);
		
		mouseX/=5;
		mouseY/=5;
	};
	
	setInterval(update, 30);
};

function update()
{
	var a;
	var b;
	
	if(active)
	{
		a = (-Math.min( Math.max( -mouseY, -size ), size ) / radius ) * tspeed;
		b = (Math.min( Math.max( -mouseX, -size ), size ) / radius ) * tspeed;
	}
	else
	{
		a = lasta * 0.98;
		b = lastb * 0.98;
	}
	
	lasta=a;
	lastb=b;
	
	if(Math.abs(a)<=0.01 && Math.abs(b)<=0.01)
	{
		return;
	}
	
	var c=0;
	sineCosine(a,b,c);
	for(var j=0;j<mcList.length;j++)
	{
		var rx1=mcList[j].cx;
		var ry1=mcList[j].cy*ca+mcList[j].cz*(-sa);
		var rz1=mcList[j].cy*sa+mcList[j].cz*ca;
		
		var rx2=rx1*cb+rz1*sb;
		var ry2=ry1;
		var rz2=rx1*(-sb)+rz1*cb;
		
		var rx3=rx2*cc+ry2*(-sc);
		var ry3=rx2*sc+ry2*cc;
		var rz3=rz2;
		
		mcList[j].cx=rx3;
		mcList[j].cy=ry3;
		mcList[j].cz=rz3;
		
		per=d/(d+rz3);
		
		mcList[j].x=(howElliptical*rx3*per)-(howElliptical*2);
		mcList[j].y=ry3*per;
		mcList[j].scale=per;
		mcList[j].alpha=per;
		
		mcList[j].alpha=(mcList[j].alpha-0.6)*(10/6);
	}
	
	doPosition();
	depthSort();
}

function depthSort()
{
	var i=0;
	var aTmp=[];
	
	for(i=0;i<aA.length;i++)
	{
		aTmp.push(aA[i]);
	}
	
	aTmp.sort
	(
		function (vItem1, vItem2)
		{
			if(vItem1.cz>vItem2.cz)
			{
				return -1;
			}
			else if(vItem1.cz<vItem2.cz)
			{
				return 1;
			}
			else
			{
				return 0;
			}
		}
	);
	
	for(i=0;i<aTmp.length;i++)
	{
		aTmp[i].style.zIndex=i;
	}
}

function positionAll()
{
	var phi=0;
	var theta=0;
	var max=mcList.length;
	var i=0;
	
	var aTmp=[];
	var oFragment=document.createDocumentFragment();
	
	//�������
	for(i=0;i<aA.length;i++)
	{
		aTmp.push(aA[i]);
	}
	
	aTmp.sort
	(
		function ()
		{
			return Math.random()<0.5?1:-1;
		}
	);
	
	for(i=0;i<aTmp.length;i++)
	{
		oFragment.appendChild(aTmp[i]);
	}
	
	oDiv.appendChild(oFragment);
	
	for( var i=1; i<max+1; i++){
		if( distr )
		{
			phi = Math.acos(-1+(2*i-1)/max);
			theta = Math.sqrt(max*Math.PI)*phi;
		}
		else
		{
			phi = Math.random()*(Math.PI);
			theta = Math.random()*(2*Math.PI);
		}
		//����任
		mcList[i-1].cx = radius * Math.cos(theta)*Math.sin(phi);
		mcList[i-1].cy = radius * Math.sin(theta)*Math.sin(phi);
		mcList[i-1].cz = radius * Math.cos(phi);
		
		aA[i-1].style.left=mcList[i-1].cx+oDiv.offsetWidth/2-mcList[i-1].offsetWidth/2+'px';
		aA[i-1].style.top=mcList[i-1].cy+oDiv.offsetHeight/2-mcList[i-1].offsetHeight/2+'px';
	}
}

function doPosition()
{
	var l=oDiv.offsetWidth/2;
	var t=oDiv.offsetHeight/2;
	for(var i=0;i<mcList.length;i++)
	{
		aA[i].style.left=mcList[i].cx+l-mcList[i].offsetWidth/2+'px';
		aA[i].style.top=mcList[i].cy+t-mcList[i].offsetHeight/2+'px';
		
		aA[i].style.fontSize=Math.ceil(12*mcList[i].scale/2)+8+'px';
		
		aA[i].style.filter="alpha(opacity="+100*mcList[i].alpha+")";
		aA[i].style.opacity=mcList[i].alpha;
	}
}

function sineCosine( a, b, c)
{
	sa = Math.sin(a * dtr);
	ca = Math.cos(a * dtr);
	sb = Math.sin(b * dtr);
	cb = Math.cos(b * dtr);
	sc = Math.sin(c * dtr);
	cc = Math.cos(c * dtr);
}



