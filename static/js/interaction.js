
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
 $("document").ready(function(){
  console.log("hello world!");
    $.post("/start",
    {
    },
    function(data,status){
      //alert("数据：" + data + "\n状态：" + status);
      if(data.code==100){
      document.getElementById("username").value =data.content;
      document.getElementById("password").style.visibility = "hidden";
      document.getElementById("btn_signIn").style.visibility = "hidden";
      document.getElementById("index_signUp").style.visibility = "hidden";
      document.getElementById("btn_logout").style.visibility = "visible";
    }else{
      // alert(data.content);
      // document.getElementById("username").value ="";
      // document.getElementById("password").value ="";
     }
    });
  });

 $("#btn_signIn").click(function(){
 	console.log("hello world!");
    $.post("/signin",
    {
      username:$('#username').val(),
      userpassword:$('#password').val()
    },
    function(data,status){
      //alert("数据：" + data + "\n状态：" + status);
      if(data.code==100){
      document.getElementById("password").style.visibility = "hidden";
      document.getElementById("btn_signIn").style.visibility = "hidden";
      document.getElementById("index_signUp").style.visibility = "hidden";
      document.getElementById("btn_logout").style.visibility = "visible";
    }else{
      alert(data.content);
      document.getElementById("username").value ="";
      document.getElementById("password").value ="";
     }
    });
  });


 $("#btn_signUp").click(function(){
  console.log("hello world!");
    $.post("/signup",
    {
      username:$('#rusername').val(),
      userpassword:$('#rpassword').val()
    },
    function(data,status){
      //alert("数据：" + data + "\n状态：" + status);
      if(data.code==100){
      alert(data.content);
      window.location.reload ="index.html";

    }else alert(data.content);
      
     
    });
});


$("#btn_logout").click(function(){
      console.log("hello world!");
      document.getElementById("username").value ="";
      document.getElementById("password").value ="";
      document.getElementById("password").style.visibility = "visible";
      document.getElementById("btn_signIn").style.visibility = "visible";
      document.getElementById("index_signUp").style.visibility = "visible";
      document.getElementById("btn_logout").style.visibility = "hidden";
});

$("#btn_back").click(function(){
      console.log("hello world!");
      window.location.href ="index.html";
});



 $("#btn_search").click(function(){
  console.log("hello world!");
    $.post("/searchcommodity",
    {
      searchitem:$('#search').val(),
    },
    function(data,status){
      console.log(data.content[0]);
      if(data.code==100)
      {
        console.log(data);
        window.location.href ="work-template.html"+ "?id="+data.content[0].id;
      }
      else{
        alert("查询失败！\n无此商品！");
        document.getElementById("search").value ="";
      }
     
    });
});

function init(sort){ 
  // if(document.title=="phone display"){
    console.log("111111");
  
   $.post("/getdata",
    {
      sort:sort,
    },
    function(data,status){
      if(data.code==100)
      {
        if(data.content[0].sort==0){
        console.log(data);
        var i=1;
        var j="";
        for(j in data.content){
        document.getElementById("img_p"+i).src = data.content[j].piclinks[0];
        document.getElementById("phone"+i).innerHTML = data.content[j].name;
        document.getElementById("href_p"+i).href +="?id=" + data.content[j].id;
        i++;
          }
        } 
         if(data.content[0].sort==1){
        console.log(data);
        var i=1;
        var j="";
        for(j in data.content){
        document.getElementById("img_pc"+i).src = data.content[j].piclinks[0];
        document.getElementById("computer"+i).innerHTML = data.content[j].name;
         document.getElementById("href_pc"+i).href +="?id=" + data.content[j].id;
        i++;
          }
        } 
         if(data.content[0].sort==2){
        console.log(data);
        var i=1;
        var j="";
        for(j in data.content){
        document.getElementById("img_c"+i).src = data.content[j].piclinks[0];
        document.getElementById("camera"+i).innerHTML = data.content[j].name;
         document.getElementById("href_c"+i).href +="?id=" + data.content[j].id;
        i++;
          }
        } 
      }
      else{
        alert("查询失败！\n无此商品！");
      }
     
    });
 // }
}

function details(){ 
  // if(document.title=="phone display"){
    console.log("22222");
  
   $.post("/searchbyid",
    {
      id:GetQueryString('id'),
    },
    function(data,status){
      if(data.code==100)
      {
        
        console.log(data);
        var i=1;
        var j=0;
        while(j <4){
        document.getElementById("img_d"+i).src = data.content[0].piclinks[j];
        document.getElementById("details"+i).innerHTML = data.content[0].name;
        document.getElementById("intro"+i).innerHTML = data.content[0].intro;
        i++;j++;
          }
      }
      else{
        alert("尚无详细信息！");
      }
     
    });
 // }
}

function GetQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}