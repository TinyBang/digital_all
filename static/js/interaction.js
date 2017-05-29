
/*
//主要就是ajax部分，这里用到了JQuery中的$.ajax函数，详细用法请参照JQ文档
$.ajax({
    'url':'login.php',//第一个参数url，PHP脚本的位置，我要把参数传到什么位置
    'data':{"username":$('#userName').val(),"password":$('#password').val(),},//传递什么数据，这里我用的是json格式，如果不知道什么是json数据，可以自己搜索一下
    'success':function(data){//success表示，当服务器返回数据成功后，该做什么，返回的数据储存在data中，我们直接把data传入函数中。
        switch(data.type){
            case 0:alert('账户不存在');break;
            case 1:{
                $('#userMsg').children('li').eq(2).find('span').html(' '+data.gouwuchenum+' ');
                $('#loginMsg li').eq(1).empty().html('<span>'+data.name+'</span>');
                $('#loginMsg li').eq(2).empty().html('<a href="javascript:tuichu()">退出</a>');
                $('.login').animate({right:-180,opacity:0},400,function(){
                    $(this).css('display','none');
                });
                break;
            }
            case 2:alert('密码错误');break;
        }
    },
    'type':'post',//type是ajax的方法，可以用post可以用get，两种方法的区别可以自己查阅资料
    'dataType':'json',//传递的数据类型，对应我上面的数据格式，这里用json。数据类型也可以是html/xml等
});
*/

$(document).ready(function(){

 //console.log("Hello World!");
 $("#btn_signIn").click(function(){
 	console.log("hello world!");
    $.post("/signup",
    {
      username:"Donald Duck",
      userpassword:"Duckburg"
    },
    function(data,status){
      //alert("数据：" + data + "\n状态：" + status);
      console.log(data.code+"\n"+status);



    });
  });

  $("#test").click(function(){
 	console.log("hello world!");


  });

});