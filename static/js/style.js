var main_color;


layui.use('element', function(){
    var $ = layui.jquery
    ,element = layui.element; //Tab的切换功能，切换事件监听等，需要依赖element模块
    //触发事件
    var active = {
        tabAdd: function(){
          //新增一个Tab项
                element.tabAdd('demo', {
                    title: '新选项'+ (Math.random()*1000|0) //用于演示
                    ,content: '内容'+ (Math.random()*1000|0)
                    ,id: new Date().getTime() //实际使用一般是规定好的id，这里以时间戳模拟下
                })
        }
        ,tabDelete: function(othis){
            //删除指定Tab项
            element.tabDelete('demo', '44'); //删除：“商品管理”
            othis.addClass('layui-btn-disabled');
        }
        ,tabChange: function(){
            //切换到指定Tab项
            element.tabChange('demo', '22'); //切换到：用户管理
        }
    };

    $('.site-demo-active').on('click', function(){
        var othis = $(this), type = othis.data('type');
        active[type] ? active[type].call(this, othis) : '';
    });

    //Hash地址的定位
    var layid = location.hash.replace(/^#test=/, '');
    element.tabChange('test', layid);

    element.on('tab(test)', function(elem){
    location.hash = 'test='+ $(this).attr('lay-id');
    });
});

//弹出层
layui.use('layer', function(){ //独立版的layer无需执行这一句
  var $ = layui.jquery, layer = layui.layer; //独立版的layer无需执行这一句
  //触发事件
  var active = {
    notice: function(){
      //示范一个公告层
      layer.open({
        type: 1
        ,title: false //不显示标题栏
        ,closeBtn: false
        ,area: '350px;'
        ,shade: 0.8
        ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
        ,btn: ['好的👌']
        ,btnAlign: 'c'
        ,moveType: 1 //拖拽模式，0或者1
        ,content: '<div style="padding: 20px;font-family: \'FZXiJinLJW\';;line-height: 22px; background-color: #ffffff; color: var(--main);font-size: 17px;border-radius:5px;text-align: center">一次搜索太多会很卡，三思而后行</br></br>温馨提示😊</br>1.按esc键清除全部选中</br>2.点击logo跳转到导航页面</div>'
        ,success: function(layero){
          var btn = layero.find('.layui-layer-btn');//在btn中可以设置几个按钮，可以检测按钮后执行相应的程序
          btn.find('.layui-layer-btn0').attr({
            // href: 'http://www.layui.com/'
            // ,target: '_blank'
          });
        }
      });
    }
  };
  $('.layui-btn').on('click', function(){
    var othis = $(this), method = othis.data('method');
    active[method] ? active[method].call(this, othis) : '';
  });
});



//弹出层
layui.use('layer', function(){ //独立版的layer无需执行这一句
  var $ = layui.jquery, layer = layui.layer; //独立版的layer无需执行这一句
  //触发事件
  var active = {
    notice: function(){
      //示范一个公告层
      layer.open({
        type: 1
        ,title: false //不显示标题栏
        ,closeBtn: false
        ,area: '350px;'
        ,shade: 0.8
        ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
        ,btn: ['好的👌']
        ,btnAlign: 'c'
        ,moveType: 1 //拖拽模式，0或者1
        ,content: '<div style="padding: 20px;font-family: \'FZXiJinLJW\';;line-height: 22px; background-color: #ffffff; color: var(--main);font-size: 17px;border-radius:5px;text-align: center">请选择要搜索的网站</div>'
        ,success: function(layero){
          var btn = layero.find('.layui-layer-btn');//在btn中可以设置几个按钮，可以检测按钮后执行相应的程序
          btn.find('.layui-layer-btn0').attr({
            // href: 'http://www.layui.com/'
            // ,target: '_blank'
          });
        }
      });
    }
  };
  $('.layui-btn2').on('click', function(){
    var othis = $(this), method = othis.data('method');
    active[method] ? active[method].call(this, othis) : '';
  });
});












    //选中多个标签
    var all_lable=new Array();
    var all_lable_text=new Array();


    function existLable() {
        var insertLable="<ul class=\"insert-lable-text\">";
        for(var i=0;i<all_lable_text.length;i++)
            insertLable=insertLable+"<li data-lable="+all_lable_text[i]+"><div class=\"lable_char\">#</div>"+all_lable_text[i]+"<span class='lable-svg-class' onclick='deleteLable(this)'><svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"feather feather-x\"><line x1=\"18\" y1=\"6\" x2=\"6\" y2=\"18\"></line><line x1=\"6\" y1=\"6\" x2=\"18\" y2=\"18\"></line></svg></span></li>"
        insertLable=insertLable+"</ul>";
        $(".nsert-lable").html(insertLable);
    }


    //实现点击添加或者删除url
    $('.lable').click(function() {
            var url=$(this).attr('data-url');
            var lable=$(this).attr('data-lable');
            $(this).toggleClass(function(){
                if($(this).hasClass('lable'))
                {
                    if(all_lable.length>4)
                    {
                        $(".layui-btn").click();

                        $(this).removeClass('lable');

                        return 'lable';
                    }
                    all_lable.push(url);
                    all_lable_text.push(lable);
                    existLable();
                    $(this).removeClass('lable');
                    return 'lable-change';
                }else
                {
                    position=all_lable.indexOf(url);//查看这个url的位置，并且删除它
                    if (position > -1) 
                        all_lable.splice(position, 1);
                    position=all_lable_text.indexOf(lable);//查看这个url的位置，并且删除它
                    if (position > -1)
                        all_lable_text.splice(position, 1);
                    existLable();
                    $(this).removeClass('lable-change');
                    // $(this).children().first().css('display', 'initial');//把js添加的内联样式设置初始化
                    //  $(this).children().first().css("color","red");
                    return 'lable';
                }
            })
        });
//打开选择网页
function openLable(){
    var text=$('.input-text').val();
    var str="1";
    text = text.replace(/(^\s*)|(\s*$)/g, '');//把首尾的空格去掉
    if(text == '' || text == undefined || text == null)
    {
        $(".input-text").val("");
        document.getElementById("input-text").focus();
        return;
    }
    if(all_lable.length===0)
    {
        $(".layui-btn2").click();
        return;
    }
    // if(all_lable.length>3)
    //     alert("注意:一次开启四个的搜索可能会导致卡顿");
    
    for(var i=0;i<all_lable.length;i++)
    {
    		str=str+"1";
            var url=all_lable[i];//map中的内容一定要和页面上的一致于
            url=url.replace("关键字",text);
            window.open(url,str);
            //delay(0.3);
    }
        
}




//记录点击次数
function countClik(cardHead) {
  //根据点击获取到这个链接的唯一标识
  // 根据唯一标识从python获取数据
  //把从python获取数据的数据加一
  //根据唯一标识写回python
  //移除被点击的那个card
  //使用ajax请求新的card元素
    var id = cardHead.getAttribute("data-id");
    $.get('click_number',{'card_id':id},     //post函数到后端
        function(data){              //回调函数
    });
}



//点赞的特效,图片来回切换
function swith_like(like){
    var number = like.getAttribute("data-number");
    if(number!='0') return;
    var id = like.getAttribute("data-id");
    $.get('click_awesome',{'card_id':id},     //post函数到后端
        function(data){              //回调函数
            $(like).attr("src", "/static/icons/1.svg");//改变属性
            var pre=$(like).prev()[0];
            $(pre).html(data);
            $(like).attr("data-number","1");
    });
    //切换版
    // if (toggle)
    // {
    //     $(like).attr("src", "/static/icons/1.svg");//改变属性
    //     $(like).attr("data-swith","0");
    //     number++;
    //
    // }
    // else
    // {
    //     $(like).attr("src", "/static/icons/2.svg")
    //     $(like).attr("data-swith","1");
    //     number--;
    // }
}





// $("input").keydown(function (e) {//当按下按键时
// if (e.which == 13) {//.which属性判断按下的是哪个键，回车键的键位序号为13
//     $('button.searchBtn').trigger("click");//触发搜索按钮的点击事件
//     }
// });

document.onkeydown = function (event) {
    var e = event || window.event || arguments.callee.caller.arguments[0];
    if (e && e.keyCode == 27) { // 按 Esc重置
      //[id=lable]是选中全部id=lable的元素
        $("[id=lable]").removeClass("lable-change");//要用id才能正常移除，类移除后可能导致元素没有类名了
        $("[id=lable]").addClass("lable");
        all_lable=[]
        all_lable_text=[]
        $(".nsert-lable").html("");

    }
            
}; 











    /*设置监听事件，向输入框中输入内容，当键盘按键弹起的时候，将输入的内容作为参数传入到函数info中*/  
    $("#value").bind("keyup",function(event){  
        /*当键盘按下上下键的时候，不进行监听，否则会与keyup事件起冲突*/  
        if(event.keyCode == 38 || event.keyCode == 40){  
            return false;  
        }  
        var value = $("#value").val();  
            info(value);  
    })  
    /*将ajax封装到函数中*/  
    function info(value){  
        /*百度搜索框智能提示的接口*/  
        var url = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su";  
        /*需要传入的参数，cb是callback的缩写*/  
        var data = {  
            wd : value,  
            cb : "helloword"  
        }  
        /*因为涉及跨域，这里使用jsonp*/  
        $.ajax({  
            url : url,  
            data : data,  
            type : "GET",  
            dataType : "jsonp",  
            jsonpCallback : "helloword",  
            /*跨域成功的时候返回的数据*/  
            success : function (result){  
                /*返回成功之后可以在开发者工具里的Console打印看一下*/  
                console.log(result);  
                /*将获取的数据整理后返回到页面*/  
                var a = result.s;  
                var list = "";  
                for(var i in a ){  
                    var l = a[i];  
                    list += "<option>"+l+"</option>";  
                }  
                $("#languageList").html(list);  
            },  
            /*跨域失败的时候返回的数据*/  
            error : function(){  
                console.log("error");  
            }  
        })  
    }  







//智能提示

function suggestSearch(value){
                var sugurl = "https://sug.so.360.cn/suggest?encodein=utf-8&encodeout=utf-8&format=json&word=#content#&callback=window.so.sug";
                sugurl = sugurl.replace("#content#", value);

                  window.so = {
                    sug: function(json) {
                        if(json.hasOwnProperty("result"))
                        {

                            var arr = json.result;
                            var list = "";
                            for(var i in arr ){
                                var data=arr[i].word
                                list += "<li class=\"suggest-item-search\">"+data+"</li>";
                            }
                            if(list != '' && list != undefined && list != null && list!=" ")
                            {
                                $(".suggest").show(0);
                                $("#suggest_ul").html(list);
                                // $("#languageList").html(list);
                            }

                        }

                    }
                }
                //动态添加JS脚本
                var script = document.createElement("script");
                script.src = sugurl;
                document.getElementsByTagName("head")[0].appendChild(script);
}

function suggestMovie(value){
  $.get('suggest_movie',{'key':value},     //post函数到后端
        function(data){              //回调函数
            data = data.replace(/(^\s*)|(\s*$)/g, '');
            if(data != '' && data != undefined && data != null && data!=" ")
            {
                $(".suggest").show(0);
                $("#suggest_ul").html(data);
                // $("#languageList").html(list);
            }
    });

}

function suggestBook(value){
    $.get('suggest_book',{'key':value},     //post函数到后端
        function(data){              //回调函数
            data = data.replace(/(^\s*)|(\s*$)/g, '');
            if(data != '' && data != undefined && data != null && data!=" ")
            {
                $(".suggest").show(0);
                $("#suggest_ul").html(data);
                // $("#languageList").html(list);
            }
    });


}



var flagAddData=0;
 $(function(){
        //载入时隐藏下拉li
        $(".suggest").hide(0);
    });

$(".input-text").keyup(function(){
    //如果文本框为空，不发送请求
    var value=$(".input-text").val();
    if(value.length === 0){
        $(".delete_btn").attr("style","display:none;");
        $(".suggest").hide(0);
        return false;
    }
    $(".delete_btn").attr("style","display:block;");
    flagAddData=0;
    var number = {};
    $(".lable-change").each(function(){
        var index=$(this).attr('data-class');
        number[index]=(number[index]+1)||1;//如果要对某个分类下的某个网站进行优化的话需要记录这个网站名，不是单纯的计数
    });
   //查看字典大小，如果是1说明只有1类。可以智能提示
   //Object.keys(number).length==1 && Object.keys(number)[0]=="影视"
    if($(".layui-this").text()=="影视") {
        suggestMovie(value);
        flagAddData=1;
    }
    else if($(".layui-this").text()=="书籍") {
        suggestBook(value);
        flagAddData=2;
    }
    else
        suggestSearch(value);
    });


//获取ul下的li的值要用这种办法.点击某个提示框然后跳转
$("ul.suggest_ul").on("click","li",function(){
    if(flagAddData)
        $(".input-text").val($(this).children().children(".suggest-title").html());
    else
        $(".input-text").val($(this).html());
    $(".suggest").hide(0);
    document.getElementById("input-text").focus();
    $(".delete_btn").attr("style","display:block;");
});

//点击页面任何其他地方 搜索结果框消失
function clearContent() {
    $(".suggest").hide();
    $(".setting").hide(300);
};
document.onclick = () => clearContent();


//页面加载完后点击Google实现默认搜索
window.onload = function() {
     $(".lable_name").each(function(){
         var data=$(this).html();
         //注意这里
         if (data=="Google")
             $(this).parent().click();
    });
}


$("#options").click(function(){
    if($(".setting").css("display")=="none"){
            $(".setting").show(300);
            return false;
    }else{
        $(".setting").hide(300);
    }
});



$(".noappear").click(function(){
    //[id=lable]是选中全部id=lable的元素
    $("[id=lable]").removeClass("lable-change");//要用id才能正常移除，类移除后可能导致元素没有类名了
    $("[id=lable]").addClass("lable");
    all_lable=[]
    all_lable_text=[]
    $(".nsert-lable").html("");
});

document.getElementById("input-text").focus();

function deleteLable(obj) {//点击事件尽量在html中使用onlick，而不使用jqueryd点击事件
   var key=obj.parentNode.getAttribute('data-lable');//原生js获取父节点的自定义属性
    position=all_lable_text.indexOf(key);//查看这个url的位置，并且删除它
    if (position > -1)
    {
        all_lable.splice(position, 1);
        all_lable_text.splice(position, 1);
    }
    existLable();
    //遍历去找到这个节点
    $(".lable-change").each(function(){
        var lable=$(this).attr('data-lable');
        if(lable==key)//改变这个节点的类
        {
            $(this).toggleClass(function(){
                $(this).removeClass('lable-change');
                return 'lable';
            })
        }
    });
}

function deleteInput()
{
    $(".input-text").val("");
    document.getElementById("input-text").focus();
    $(".delete_btn").attr("style","display:none;");
}

