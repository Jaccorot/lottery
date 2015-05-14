$(function(){
   var nodes=$("tbody>tr").get().reverse();
    $.each(nodes,function(k,v){
    	//判断本次开奖号码的类型
	   	if(($(this).find(".td_num1").text() == $(this).find(".td_num2").text()) && ($(this).find(".td_num1").text() == $(this).find(".td_num3").text())){
	    		$(this).find(".baozi").text("豹子").addClass("analysis").removeClass("interval");
	    	}else if(($(this).find(".td_num1").text() != $(this).find(".td_num2").text()) && ($(this).find(".td_num1").text() != $(this).find(".td_num3").text()) && ($(this).find(".td_num2").text() != $(this).find(".td_num3").text())){
	    		$(this).find(".zusan").text("组三").addClass("analysis").removeClass("interval");
	    	}else{
	    		$(this).find(".chongfu").text("重复").addClass("analysis").removeClass("interval");
	    }
	    //记录该位置号码的未出现情况，出现归零，下一次从1开始
		if(k==0){
        	$(this).find("td").each(function(){
            	if($(this).html()==""){
             	 	$(this).text("1");
             	}
            });
    
        }else{
        	$(this).find("td").each(function(){
        		if($(this).html()==""){
        			if($(this).parent().next().find("td").eq($(this).index()).is(".analysis")){
                    	$(this).text("1");
                    }else{
                		$(this).text(eval($(this).parent().next().find("td").eq($(this).index()).text()+"+"+1))
                	}
        		}
	        });
            
            //增加绘图
            draw_line(v,'td_canvas_100');
            draw_line(v,'td_canvas_10');
            draw_line(v,'td_canvas_1');
       	}
	});
});
//接受节点和类名称，在#canvas_draw中增加一个canvas节点，并绘图
function draw_line(node_v, class_name) {
	var str_class_name = "."+class_name;
	var node = $(node_v).find(str_class_name);
    var node_x = node.offset().left + node.outerWidth() * 0.5;
	var node_y= node.offset().top + node.outerHeight() * 0.5;
	var pre_node = node.parent().next().find(str_class_name);
	var pre_node_x = pre_node.offset().left + pre_node.outerWidth() * 0.5;
	var pre_node_y = pre_node.offset().top + pre_node.outerHeight() * 0.5;
	var new_node = $("<canvas></canvas>").css({"width":Math.abs(pre_node_x - node_x),"height":Math.abs(pre_node_y - node_y),"position":"absolute","left":Math.min(pre_node_x,node_x),"top":node_y - $(node_v).parent().parent().offset().top}).addClass(class_name);
	$('#canvas_draw').append(new_node);
	var ctx = new_node.get(0).getContext('2d');
	ctx.beginPath();
/*	ctx.moveTo(0,0);
	ctx.lineTo(45,45);*/
	
	ctx.moveTo((node_x >= pre_node_x ? new_node.width():0), 0);
	ctx.lineTo((node_x < pre_node_x ? new_node.width():0), new_node.height());
	ctx.lineWidth = 1.0;
	ctx.strokeStyle = "#CC0000";
	ctx.stroke(); 

/*	console.log("start_x:"+start_x+ " start_y:"+0+" end_x:"+end_x+" end_y:"+ Math.abs(pre_node_y - node_y)+"###");
*/

}