window.onload=function(){
    document.getElementById('showSignin2').onclick=document.getElementById('btn_showlogin').onclick=document.getElementById('showSignin1').onclick=showLogin;
    document.getElementById('close_minilogin').onclick=closeLogin;
    document.getElementById('showSignup').onclick=showSignup;
    document.getElementById('close_minisignup').onclick=closeSignup;
    document.getElementById('showFindpass').onclick=showFindpass;
    document.getElementById('close_Findpass').onclick=closeFindpass;
    var mini_login=document.getElementsByClassName('mini_login')[0];
    var cover=document.getElementsByClassName('cover')[0];
    var mini_signup=document.getElementsByClassName('mini_signup')[0];
    var mini_findpass=document.getElementsByClassName('mini_findpass')[0];


    function showLogin(){
        mini_login.style.display='block';
        mini_findpass.style.display='none';
        mini_signup.style.display='none';
        cover.style.display='block';

        mini_login.style.left=(document.body.clientWidth-mini_login.clientWidth)/2+"px";
        mini_login.style.top=(document.body.clientHeight-mini_login.clientHeight)/3+"px";
    }

    function closeLogin(){
        mini_login.style.display='none';
        cover.style.display='none';
    }

    function showSignup(){
        mini_login.style.display='none';
        mini_findpass.style.display='none';
        mini_signup.style.display='block';
        cover.style.display='block';

        mini_signup.style.left=(document.body.clientWidth-mini_signup.clientWidth)/2+"px";
        mini_signup.style.top=(document.body.clientHeight-mini_signup.clientHeight)/7+"px";
    }


    function closeSignup(){
        mini_signup.style.display='none';
        cover.style.display='none';
    }

    function showFindpass(){
        mini_login.style.display='none';
        mini_signup.style.display='none';
        mini_findpass.style.display='block';
        cover.style.display='block';

        mini_findpass.style.left=(document.body.clientWidth-mini_findpass.clientWidth)/2+"px";
        mini_findpass.style.top=(document.body.clientHeight-mini_findpass.clientHeight)/7+"px";
    }

    function closeFindpass() {
        mini_signup.style.display='none';
        cover.style.display='none';
    }

    function isEmail( str ){
        var myReg = /^[-_A-Za-z0-9]+@([_A-Za-z0-9]+\.)+[A-Za-z0-9]{2,3}$/;
        if(myReg.test(str)){
            return true;
        }
        else{
            return false;
        }

}

    signin=function(){
        var right=true;
        document.getElementsByClassName('usrerrempty')[0].style.visibility='hidden';
        document.getElementsByClassName('usrerrformat')[0].style.visibility='hidden';
        document.getElementsByClassName('paserr')[0].style.visibility='hidden';
        var username=document.getElementById('username').value;
        var pass=document.getElementById('password');
        if(username==''){
            document.getElementsByClassName('usrerrempty')[0].style.visibility='visible';
            right=false;
        }
        else if(isEmail(username)==false){
            document.getElementsByClassName('usrerrformat')[0].style.visibility='visible';
            right=false;
        }

        if(pass.value==''){
            document.getElementsByClassName('paserr')[0].style.visibility='visible';
            right=false;
        }

        if(right){
            var fields = $('#login_form').serializeArray();
            var obj = {}; //声明一个对象
            $.each(fields, function(index, field) {
                obj[field.name] = field.value; //通过变量，将属性值，属性一起放到对象中
            })
            console.log(obj);

            // $.ajax({
            //         type: "post",
            //         url: "https://148.70.200.102:443",
            //         async: true,
            //         contentType: 'application/json',
            //         dataType: 'JSON',
            //         data: JSON.stringify(obj),//将对象转为json字符串
            //         success: function() {
            //             console.log('success');
            //             // window.location.href="localhost"
            //         }
            //     });

        }
    }

    var clock = '';
    var nums = 10;
    var btn=document.getElementsByClassName('orange')[0];
    sendCode=function ()
    {
        $.ajax({
        type: "POST",
        url: "/sendemailcode/sendemailcode",
        success:function (data) {
        if (data)
            print("邮件发送成功")
        else
            print("邮件发送失败")
            // console.log('success!');
        }
        });


        btn.disabled = true;
        btn.value = nums+'s to wait';
        clock = setInterval(doLoop, 1000);
    }


    function doLoop()
    {
    nums--;
    if(nums > 0){
    btn.value = nums+'s to wait';
    }else{
    clearInterval(clock);
    btn.disabled = false;
    btn.value = '点击发送验证码';
    nums = 10;
    }
    }


    signup=function(){
        var correct=true;
        document.getElementsByClassName('usrerrempty')[1].style.visibility='hidden';
        document.getElementsByClassName('usrerrformat')[1].style.visibility='hidden';
        document.getElementsByClassName('paserr')[1].style.visibility='hidden';
        document.getElementsByClassName('repaserr')[0].style.visibility='hidden';
        document.getElementsByClassName('ecode')[0].style.visibility='hidden';
        document.getElementsByClassName('paserr')[2].style.visibility='hidden';

        var username_signup=document.getElementById('username_signup').value;
        var papassword_signup=document.getElementById('password_signup');
        var repass=document.getElementById('repassword_signup');
        var vccode=document.getElementById('VerificationCode');
        if(username_signup==''){
            document.getElementsByClassName('usrerrempty')[1].style.visibility='visible';
            correct=false;
        }
        else if(isEmail(username_signup)==false){
            document.getElementsByClassName('usrerrformat')[1].style.visibility='visible';
            correct=false;
        }

        if(papassword_signup.value==''){
            document.getElementsByClassName('paserr')[1].style.visibility='visible';
            correct=false;
        }

        else  if(papassword_signup.value.length<6||papassword_signup.value.length>12){
            document.getElementsByClassName('paserr')[2].style.visibility='visible';
            correct=false;
        }

        if(repass.value!=papassword_signup.value){
            document.getElementsByClassName('repaserr')[0].style.visibility='visible';
            correct=false;
        }

        if(vccode.value==''){
            document.getElementsByClassName('ecode')[0].style.visibility='visible';
            correct=false;
        }

        if(correct){
            var fields = $('#signup_form').serializeArray();
            var obj = {}; //声明一个对象
            $.each(fields, function(index, field) {
                obj[field.name] = field.value; //通过变量，将属性值，属性一起放到对象中
            })

            console.log(obj);

            // $.ajax({
            //         type: "post",
            //         url: "https://148.70.200.102:6666",
            //         async: true,
            //         contentType: 'application/json',
            //         dataType: 'JSON',
            //         data: JSON.stringify(obj),//将对象转为json字符串
            //         success: function() {
            //             console.log('success!');
            //         }
            //     });


        }
    }
}